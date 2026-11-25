# VisualPage publication manifest

Run `python3 -I tools/visual-page.py PAGE.datom NEW_OUTPUT_DIRECTORY`. The
bundle contains `index.html` and the image asset map. The manifest begins
with its Presentation name, signature, and vector of sections.

A section is a module struct followed by one explicit body:

```datom
{ { Intent opus 0 } Archive }
{ { Vision old-module 0 } Removed }
{ { Vision sema 0 } ReplaceModule.[ { Added.«pictures/sema.png» 12 None } ] }
{ { Vision example 0 } [ { Standing.«pictures/example.png» 8 None } ] }
```

Archive and Removed show their module heading and mark alone. ReplaceModule
shows the module heading and Replacement mark, then its nonempty picture
vector. The ordinary picture vector is unchanged, including an empty vector.
These section bodies contain no old module file path or source.

A pictured unit's last field is `None` for a picture alone, or
`Some.{ UnitKind «complete fenced text» }` for a picture followed by code.
The text holds complete Markdown code fences; whitespace may separate them.
Each fence is displayed exactly as supplied, including its opening and
closing lines. Each fence supplies its own language label. The renderer
refuses text outside fences, an incomplete fence, a source-bearing legacy
Archive or ReplaceModule body, and an empty replacement. The unit's word
count remains manifest metadata.
