---
description: How the production Flow Nexus confirms that a started flow received its startup parts, and why a Claude start whose task ends in a newline is refused.
dependencies: [vision-flow, knowledge-flow]
---

Read on 2026-10-17 in Flow `67b80b3` (0.35.11, installed and running).

## How a start is confirmed

Flow records the SHA-256 of every part it types into a new flow: the
modules and the task. It then reads the flow's own transcript. Each
user text there must hash to the next expected part; any other text
refuses the start with `PartDiffers`, and Flow closes the pane. Claude
records a pasted part inside a paste wrapper, which Flow takes off
before hashing.

```
+--------------------------+
| the parts Flow types:    |
| modules, then the task   |
+------------+-------------+
             |
             | each part's hash is kept in
             v
+--------------------------+
| the launch intent        |
+------------+-------------+
             |
             | is compared with
             v
+--------------------------+
| the transcript's user    |
| texts, wrapper taken off |
+------+-------------+-----+
       |             |
 every |             | one
 hash  |             | differs
 equal |             |
       v             v
+------------+ +--------------+
| started    | | refused:     |
|            | | PartDiffers; |
|            | | pane closed  |
+------------+ +--------------+
```

`crates/flow-nexus/src/herdr/launch.rs`:

```rust
fn text_sha256(&self) -> String {
    format!("{:x}", Sha256::digest(self.as_bytes()))
}

fn claude_pasted_content(&self) -> Option<&str> {
    let rest = self.strip_prefix("\n\n<pasted_content id=\"")?;
    let (identifier, rest) = rest.split_once("\">\n")?;
    if identifier.is_empty()
        || identifier.contains(|c: char| c == '"' || c == '<' || c == '>' || c.is_whitespace())
    {
        return None;
    }
    rest.strip_suffix(&format!("\n</pasted_content id=\"{identifier}\">\n"))
}
```

```rust
if expected.is_some_and(|hash| &text.text_sha256() == hash) {
    self.seen_parts += 1;
    self.last_part_answered = false;
    return Ok(self.seen_parts);
}
Err(NativeLaunchFailure::PartDiffers)
```

## A task that ends in a newline

The deployed unwrapping always takes a newline off before the closing
tag. By the commit message of the repair below, Claude Code 2.1.294
writes that newline only when the part does not already end in one;
so a part ending in a newline loses its own last newline, and its hash
differs. d68c82 recorded the same by hash for its first start of
804eb9 (`/home/li/primary/flows/d68c82/receipts/launch-flow-ethos-2026-10-17.md`):

```sh
# flows/d68c82/launch/flow-ethos-2026-10-17/
#   ethos-start.out
# -> StartRejected.NativeLaunchRefused.{ Receipt
#      PartDiffers }
```

The start that followed trimmed the task's trailing whitespace and was
accepted:

```js
brief: `Address.{ Psyche ${spec.topic} Secondary }\n\n` + fs.readFileSync(new URL(spec.brief, import.meta.url), "utf8").trimEnd(),
```

Primary's `tools/flow-start-adapter.mjs` passes the task as given; it
does not trim it.

## The repair, not deployed

Flow 0.35.15, branch `flow-da2038-receipt` at `517ea88` (pushed, not
merged, not installed), rebuilds Claude's paste element from the part
under the recorded id and accepts the part only when the rebuilt
element equals the transcript row byte for byte.
