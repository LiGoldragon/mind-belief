---
description: Reading or writing any protos dialect, or touching the protos crate.
dependencies: []
---

Protos owns the only character reader and the only character writer.

## Four layers

```
; textual: these characters, uninterpreted
{ Ada 1990 }
```
```rust
// protosic: an enclosure of two bare runs, each structure at its extent in the text
Protos::Enclosed { extent: Extent { start: 0, end: 12 }, enclosure: Braced, children: vec![
    Protos::Bare { extent: Extent { start: 2, end: 5 }, text: "Ada".to_owned() },
    Protos::Bare { extent: Extent { start: 6, end: 10 }, text: "1990".to_owned() } ] }
// conceptual, here datomic: a struct of two positions, each datom at its path
Datom { path: vec![], form: Form::Struct(vec![
    Datom { path: vec![0], form: Form::Bare("Ada".to_owned()) },
    Datom { path: vec![1], form: Form::Bare("1990".to_owned()) } ]) }
// compositional: the meaning fully absorbed; no position, because the tree is consumed
Person { name: String::from("Ada"), born: 1990 }
```

## Delimiters

## Structure

## Kinds

| type | kind | becomes |
|---|---|---|
| composition | `Composing` | read from a datom; a struct form states its positions through `Compositional` |

```rust
pub enum Protos {
    Headed { extent: Extent, head: Symbol, constraints: Option<Box<Protos>>, separator: Separator, body: Box<Protos> },
    Enclosed { extent: Extent, enclosure: Enclosure, children: Vec<Protos> },
    Opaque { extent: Extent, boundary: Boundary, content: String },
    Bare { extent: Extent, text: String },
}
pub enum Enclosure { Braced, Bracketed, Angled }
pub enum Boundary  { Guillemets, Parentheses }
pub enum Separator { Period, Exclamation, Colon }
pub struct Extent { pub start: usize, pub end: usize }
pub struct Error  { pub extent: Extent, pub problem: Problem }
pub struct ReaderBudget { pub remaining: usize }

pub trait Protosizable    { type Output; fn protosize(&self) -> Self::Output; }  // String -> Result<Protos, Error>; Datom -> Protos
pub trait Textualizable   { fn textualize(&self) -> String; }
pub trait Canonicalizable { fn canonicalize(&mut self); }

let text = person.datomize(Path::new()).protosize().textualize();
```

## Canonical print

A single `;` opens a comment to end of line; comments are not printed.
