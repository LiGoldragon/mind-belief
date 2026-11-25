# VisualPage section bodies

The renderer takes `page.datom` and a new output directory. Each section has a module struct followed by one body. Existing picture bodies are vectors of units; their syntax and output are unchanged. A bare empty vector is still a picture body with no units.

An archived module has the explicit body `Archive.SourcePath`. For example, this is one section in the page’s section vector:

```datom
{ { Intent opus 0 } Archive.«archive/intent/opus/0.md» }
```

Place the complete UTF-8 module from the revision being removed at that path, relative to `page.datom`. The path must stay inside the manifest’s directory and end in the module’s own `kind/topic/version.md`. Use the module file itself, including its front matter, rather than copying the proposal’s removal summary.

The output for that section is the module heading, the Archive mark, and the entire module as escaped source with a red margin. It has no image and adds no entry to the picture asset map. A missing or invalid source refuses the build.

A whole-module replacement uses `ReplaceModule.{ SourcePath [ Unit... ] }`. Its
source path has the same requirements as Archive, and the vector contains the
proposed replacement picture units in order:

```datom
{ { Vision sema 0 }
  ReplaceModule.{ «archive/vision/sema/0.md»
                   [ { Added.«pictures/sema.svg» 12 None } ] } }
```

This section has one module heading. The complete removed source comes first,
with the red margin and without an image or Archive mark. The proposed picture
units follow. The picture asset map contains the picture files alone.
