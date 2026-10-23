---
description: Constructing, reading or interpreting datom text, or giving a Rust type its datom kinds.
dependencies: [knowledge-protos]
---

## A datom is a form at a path

```rust
pub struct Datom { pub path: Path, pub form: Form }
pub enum Form { Struct(Vec<Datom>), Vector(Vec<Datom>), Variant(Symbol, Box<Datom>), Bare(String), String(String), Meaning(Opaque) }
```

## Syntax

A decimal is finite and point-mandatory.

```
; datom, in a position expecting Person: a struct of name String, born Integer, address Address, roles Vector<Role>.
{ Ada 1990 { «12 Rue de la Paix» Paris 75002 } [ Author Reviewer.{ 2024 17 } ] }

; Reply: an enum of Accepted.{ id Integer  at String }, Refused.{ reason String  code Integer }, Pending
Accepted.{ 42 2026-09-03T17:46:20 }          ; the timestamp has no space and no delimiter, so it is bare
Refused.{ «no such file: { } is content» 2 } ; delimited: the string has spaces and braces; inside the guillemets they are content
Pending                                      ; a variant carrying nothing

[ 0 42 -42 ]                                 ; a vector of Integer
Observed.Locks.[]                            ; the Observed variant, its Locks variant, the empty vector
[ Some.42 None ]   Ok.{ Ada 1990 }   Err.«no such lock»   ; Vector, Option and Result read as ordinary variants
```

## The datom composes; the type states its positions

```rust
pub trait Composable {
    fn compose<T: Composing>(&self, budget: &mut Budget) -> Result<T, Error>;
    fn compose_positions<T: Compositional>(&self, budget: &mut Budget) -> Result<T, Error>;
}
pub trait Composing: Sized { fn compose(datom: &Datom, budget: &mut Budget) -> Result<Self, Error>; }
pub trait Compositional: Composing { const ARITY: Integer; fn from_positions(positions: Positions<'_>) -> Result<Self, Error>; }
pub trait Datomizable { fn datomize(&self, at: Path) -> Datom; }
```

## Any Rust type

```rust
#[derive(datom_codec::Datomizable, datom_codec::Composing)]
pub struct Locus { pub path: Path, pub extent: Extent }

impl Compositional for Locus {                              // generated: the positions, in order
    const ARITY: Integer = 2;
    fn from_positions(mut positions: Positions<'_>) -> Result<Self, Error> {
        Ok(Self { path: positions.position()?, extent: positions.position()? })
    }
}
impl Composing for Locus {                                  // generated: the datom reads, spending the budget
    fn compose(datom: &Datom, budget: &mut Budget) -> Result<Self, Error> {
        datom.compose_positions(budget)
    }
}
impl Datomizable for Locus {                                // generated: each child placed as the tree is built
    fn datomize(&self, at: Path) -> Datom {
        Datom { path: at.clone(), form: Form::Struct(vec![self.path.datomize(at.child(0)), self.extent.datomize(at.child(1))]) }
    }
}
```

## From text and back

```rust
let query: Query = Potential::<Query>::from(text).actualize(&mut budget)?;
let out = response.datomize(Path::new()).protosize().textualize();
```

## Errors

```
[ 1 x ]                                  ; read as Vector<Integer>
Error.{ Composition [ 1 ] Value.{ Integer x } }   ; at path 1, the bare string x is not an integer
```

## The interface shape

```sh
orchestrate 'Lock.{ MyLock 6329f1 [ /abs/path ] «why I hold it» }'
# -> Locked.{ 442 MyLock 6329f1 [ /abs/path ] «why I hold it» }
```

## A datom needs a type

A datom is written only against a type that already exists. When none exists, the type is declared first, in Ethos through the `vision:ethos` context module; there is no ad hoc datom and no field label standing in for a type.
