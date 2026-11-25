# VisualPage section bodies

The renderer takes `page.datom` and a new output directory. Each section has a module struct followed by one body. Existing picture bodies are vectors of units; their syntax and output are unchanged. A bare empty vector is still a picture body with no units.

An archived module has the explicit body `Archive.SourcePath`. For example, this is one section in the page’s section vector:

```datom
{ { Intent opus 0 } Archive.«archive/intent/opus/0.md» }
```

Place the complete UTF-8 module from the revision being removed at that path, relative to `page.datom`. The path must stay inside the manifest’s directory and end in the module’s own `kind/topic/version.md`. Use the module file itself, including its front matter, rather than copying the proposal’s removal summary.

The output for that section is the module heading, the Archive mark, and the entire module as escaped source with a red margin. It has no image and adds no entry to the picture asset map. A missing or invalid source refuses the build.
