"""Build a VisualPage bundle from its positional Datom. Publication is separate."""
import argparse
from dataclasses import dataclass
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import quote


@dataclass(frozen=True)
class SectionMark:
    text: str


@dataclass(frozen=True)
class ReplaceModule:
    units: list


def code_fences(text):
    """Read the language and exact interior of each complete Markdown fence."""
    lines = text.splitlines(keepends=True)
    fences = []
    at = 0
    while at < len(lines):
        if not lines[at].strip():
            at += 1
            continue
        opening = re.fullmatch(r" {0,3}(`{3,}|~{3,})[ \t]*([^\r\n]*)", lines[at].rstrip("\r\n"))
        if not opening:
            raise ValueError("A pictured unit's code may contain complete fences only")
        delimiter, info = opening.groups()
        if delimiter.startswith("`") and "`" in info:
            raise ValueError("Invalid backtick fence opening")
        language = info.split(None, 1)[0] if info.strip() else None
        close = re.compile(r" {0,3}" + re.escape(delimiter[0]) + "{" + str(len(delimiter)) + r",}[ \t]*")
        at += 1
        content_start = at
        while at < len(lines) and not close.fullmatch(lines[at].rstrip("\r\n")):
            at += 1
        if at == len(lines):
            raise ValueError("Unclosed code fence in pictured unit")
        fences.append((language, "".join(lines[content_start:at])))
        at += 1
    if not fences:
        raise ValueError("A pictured unit with code needs a complete fence")
    return fences


def picture_code(language, source):
    """Keep code readable even when the publication supplies its own pre/code theme."""
    language_class = f' class="language-{html.escape(language)}"' if language else ""
    # Inline important rules belong to the component, even inside a publisher's styled wrapper.
    block_style = (
        "color-scheme:light dark!important;"
        "color:#17212b!important;background:#f1f5f9!important;"
        "color:light-dark(#17212b,#e2e8f0)!important;"
        "background:light-dark(#f1f5f9,#141c28)!important;"
        "box-sizing:border-box!important;display:block!important;"
        "inline-size:100%!important;min-inline-size:0!important;max-inline-size:100%!important;"
        "block-size:auto!important;max-block-size:none!important;"
        "margin:0.5rem 0 0!important;padding:0.75rem!important;"
        "overflow:auto!important;text-overflow:clip!important;"
        "white-space:pre!important;font:0.875rem/1.5 monospace!important;"
    )
    code_style = (
        "color:inherit!important;background:transparent!important;"
        "display:inline!important;font:inherit!important;white-space:inherit!important;"
        "overflow:visible!important;padding:0!important;"
    )
    # HTML's input preprocessor normalizes literal CR; a character reference preserves it.
    escaped = html.escape(source).replace("\r", "&#13;")
    return (
        f'<pre tabindex="0" style="{block_style}">'
        f'<code{language_class} style="{code_style}">{escaped}</code></pre>'
    )


class Datom:
    def __init__(self, source):
        self.source = source
        self.at = 0

    def seek(self):
        while self.at < len(self.source) and self.source[self.at].isspace():
            self.at += 1
        return self.source[self.at:self.at + 1]

    def require(self, token):
        self.seek()
        if not self.source.startswith(token, self.at):
            raise ValueError(f"Expected {token!r} at character {self.at + 1}")
        self.at += len(token)

    def atom(self):
        self.seek()
        start = self.at
        while self.at < len(self.source):
            c = self.source[self.at]
            if c.isspace() or c in "{}[].«»":
                break
            self.at += 1
        if self.at == start:
            raise ValueError(f"Expected an atom at character {start + 1}")
        return self.source[start:self.at]

    def text(self):
        if self.seek() != "«":
            return self.atom()
        self.at += 1
        depth = 1
        value = []
        while self.at < len(self.source):
            c = self.source[self.at]
            self.at += 1
            if c == "\\" and self.source[self.at:self.at + 1] in ("«", "»"):
                value.append(self.source[self.at])
                self.at += 1
                continue
            if c == "«":
                depth += 1
            elif c == "»":
                depth -= 1
                if depth == 0:
                    return "".join(value)
            value.append(c)
        raise ValueError("Unclosed guillemet string")

    def vector(self, item):
        self.require("[")
        items = []
        while self.seek() and self.seek() != "]":
            items.append(item())
        self.require("]")
        return items

    def unit(self):
        self.require("{")
        change = self.atom()
        self.require(".")
        if change == "Replaced":
            self.require("{")
            paths = [self.text(), self.text()]
            self.require("}")
        elif change in {"Standing", "Added", "Removed"}:
            paths = [self.text()]
        else:
            raise ValueError(f"Unknown picture change {change!r}")
        words = int(self.atom())
        option = self.atom()
        if option == "None":
            code = None
        elif option == "Some":
            self.require(".{")
            self.text()  # The unit kind; each fence carries its own language.
            code = code_fences(self.text())
            self.require("}")
        else:
            raise ValueError(f"Unknown code option {option!r}")
        self.require("}")
        return change, paths, words, code

    def section(self):
        self.require("{")
        self.require("{")
        module = self.atom(), self.text(), self.atom()
        self.require("}")
        if self.seek() == "[":
            body = self.vector(self.unit)
        else:
            kind = self.atom()
            if kind in {"Archive", "Removed"}:
                body = SectionMark(kind)
            elif kind == "ReplaceModule":
                self.require(".")
                units = self.vector(self.unit)
                if not units:
                    raise ValueError("A module replacement needs picture units")
                body = ReplaceModule(units)
            else:
                raise ValueError(f"Unknown section body {kind!r}")
        self.require("}")
        return module, body

    def page(self):
        self.require("{")
        title, signature = self.text(), self.text()
        sections = self.vector(self.section)
        self.require("}")
        if self.seek():
            raise ValueError(f"Unexpected text at character {self.at + 1}")
        return title, signature, sections


def render(manifest, output):
    title, signature, sections = Datom(manifest.read_bytes().decode("utf-8")).page()
    root = manifest.resolve().parent
    assets = {}
    e = html.escape

    def picture(name, change):
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or path.suffix.lower() not in {
            ".svg", ".png", ".jpg", ".jpeg", ".webp"
        }:
            raise ValueError(f"Expected a relative picture path: {name!r}")
        source = (root / path).resolve(strict=True)
        if not source.is_relative_to(root) or not source.is_file():
            raise ValueError(f"Picture is outside the page directory: {name!r}")
        key = path.as_posix()
        assets[key] = source
        return f'<img class="{change}" src="{quote(key)}" alt="">'

    def section_mark(text):
        return f'<p class="section-mark"><strong>{e(text)}</strong></p>'

    def picture_units(units):
        for change, paths, _words, fences in units:
            marks = ("removed", "added") if change == "Replaced" else (change.lower(),)
            yield '<article><div class="pictures">'
            yield from (picture(path, mark) for path, mark in zip(paths, marks, strict=True))
            yield "</div>"
            for language, source in fences or ():
                yield picture_code(language, source)
            yield "</article>"

    body = [f"<h1>{e(title)}</h1><p>{e(signature)}</p>"]
    for module, section_body in sections:
        body.append(f"<section><h2>{e('{ ' + ' '.join(module) + ' }')}</h2>")
        match section_body:
            case SectionMark(mark):
                body.append(section_mark(mark))
            case ReplaceModule(units):
                body.append(section_mark("Replacement"))
                body.extend(picture_units(units))
            case units:
                body.extend(picture_units(units))
        body.append("</section>")

    output.mkdir(parents=True, exist_ok=False)
    for key, source in assets.items():
        dest = output / key
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
    style = """<style>
:root{color-scheme:light dark}body{max-width:65rem;margin:2rem auto;padding:0 1rem;font:1rem system-ui}
article{margin:1rem 0 2rem}.pictures{display:flex;flex-wrap:wrap;gap:1rem;align-items:flex-start}
img{display:block;max-width:100%;height:auto;box-sizing:border-box}.added{border-inline-start:.4rem solid #38945e}
.removed{border-inline-start:.4rem solid #bd4b57}
</style>"""
    (output / "index.html").write_text(
        f'<!doctype html><html lang="en"><meta charset="utf-8"><title>{e(title)}</title>'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        + style + "<body>" + "\n".join(body) + "</body></html>\n",
        encoding="utf-8",
    )
    (output / "assets.json").write_text(
        json.dumps({k: str((output / k).absolute()) for k in assets}, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("page", type=Path, help="VisualPage Datom")
    ap.add_argument("output", type=Path, help="new scratch bundle directory")
    args = ap.parse_args()
    try:
        render(args.page, args.output)
    except (OSError, ValueError) as err:
        ap.exit(1, f"VisualPage: {err}\n")


if __name__ == "__main__":
    main()
