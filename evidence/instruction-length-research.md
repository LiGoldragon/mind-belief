# Instruction length and adherence research

Research date: 2026-10-14. This is a source ledger for the accompanying
knowledge and inquiry modules. The reviewed evidence does not establish a
universal ideal context-module size in words, lines, or tokens.

## Primary empirical studies

ComplexBench, arXiv 2407.03978v3, describes four constraint types, 19
constraint dimensions, and four composition types, and evaluates 15 models.
Its results report that performance drops as composition complexity increases,
including for nested selection. The benchmark's reported DRFR aggregates
scoring questions through composition dependencies; it is not a direct count
of failed instructions. The benchmark varies constraint composition, not an
authored module's length while holding constraints fixed. Source:
<https://arxiv.org/html/2407.03978v3>, abstract and sections 3, 4.3, and 5.2
(accessed 2026-10-14).

SIFo, arXiv 2406.19999v2, evaluates sequential instruction following and
reports that performance changes with instruction order; the best positional
pattern differs by model and instruction type. Its sequence and permutation
experiments concern order and dependent steps, not an optimized module-length
threshold. Source: <https://arxiv.org/html/2406.19999v2>, section 3 and
section 5 (accessed 2026-10-14).

LIFEBench, arXiv 2505.16234v2, evaluates 10,800 instances with requested
output lengths from 16 to 8,192 words and extended settings to 32,768 words.
It measures output-length adherence and its failure curves, not input-module
size. Source: <https://arxiv.org/html/2505.16234v2>, sections 1 and E.3
(accessed 2026-10-14).

LIFBench, arXiv 2411.07037v3, keeps the instruction short and places it at
the end while varying long input context from 4K through 128K tokens across
models and tasks. It reports model- and task-dependent degradation as context
grows, but it does not vary isolated module length while holding the rest of
the workload fixed. Source: <https://arxiv.org/html/2411.07037v3> (accessed
2026-10-14).

LongIns, arXiv 2406.17588v3, concatenates synthetic instruction questions at
256 through 16,384 tokens and varies question density. It reports density and
length effects in that synthetic task, not a general skill-execution optimum
or a universal 16K boundary. Source: <https://arxiv.org/html/2406.17588v3>
(accessed 2026-10-14).

The Instruction Hierarchy, arXiv 2404.13208, studies how privileged
instructions and conflicts affect prompt-injection robustness. It establishes
instruction hierarchy as a separate variable; it does not measure an ideal
module size. Source: <https://arxiv.org/abs/2404.13208> (accessed
2026-10-14).

## Provider guidance

Anthropic's Agent Skills overview describes progressive disclosure: metadata
is always loaded, the skill body loads when triggered, and bundled resources
load as needed. The Anthropic-maintained skill-creator guide calls under 500
lines ideal for the `SKILL.md` body and recommends additional hierarchy near
that limit. This is provider authoring guidance, not a controlled adherence
experiment or a token-equivalent cutoff. Sources:
<https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
and
<https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md>
(accessed 2026-10-14; the latter states the under-500-lines guidance at its
Skill Writing Guide).

The same official overview gives provider loading-cost guidance: Level 1
metadata is approximately 100 tokens per Skill and always loaded; Level 2
instructions are under 5,000 tokens and load when triggered; Level 3 resources
have no token cost until accessed. These values describe Anthropic's provider
architecture and budget model. They are not a measured adherence optimum, a
local enforced loader cap, or a words-to-tokens conversion.

## Local loader witnesses

The following source files were read at the listed revisions on 2026-10-14.
They establish loader mechanics, not runtime equivalence across deployments.

| Source | Revision | Observed fact |
| --- | --- | --- |
| `/git/github.com/LiGoldragon/Curriculum/src/registry.rs:67-124,136-169` | `73414b6` | Complete Markdown roots are indexed and validated. |
| `/git/github.com/LiGoldragon/Curriculum/src/registry.rs:306-349` | `73414b6` | Requested roots expand through dependencies once, dependency first. |
| `/git/github.com/LiGoldragon/Curriculum/src/projection.rs:391-405` | `73414b6` | Complete generated skill bodies are projected. |
| `/git/github.com/LiGoldragon/Curriculum/src/projection.rs:408-431` | `73414b6` | Complete standing bodies are placed in role packets. |
| `/git/github.com/LiGoldragon/Curriculum/src/roles.rs:85-124` | `73414b6` | Role packets carry their selected module bodies. |
| `/home/li/primary/flow/crates/flow-nexus/src/herdr/launch.rs:753-773` | `28a78d2` | Claude expansion strips frontmatter and uses the selected body. |
| `/home/li/primary/flow/crates/flow-nexus/src/herdr/launch.rs:1018-1075` | `28a78d2` | Claude selected source paths and hashes are recorded. |
| `/home/li/primary/flow/crates/flow-nexus/src/codex.rs:612-716` | `28a78d2` | Codex resolves selected skills by name and canonical path. |
| `/home/li/primary/flow/crates/flow-nexus/src/codex.rs:718-744` | `28a78d2` | Codex submits typed selected skill inputs. |
| `/home/li/primary/flow/crates/flow-nexus/src/herdr/launch.rs:1239-1257` | `28a78d2` | Claude launch verifies complete expansions in its transcript. |
| `/home/li/primary/flow/crates/flow-nexus/src/composition.rs:42-53,388-453` | `28a78d2` | Initial and later Claude skill invocation forms are composed. |
| `/home/li/primary/config/context-refresh.json:1-9` | `28a78d2` | The 200000-token value is a context warning, not a module limit. |
| `/home/li/primary/tools/field-census/README.md:20-38` | `28a78d2` | Context census supports exact/proxy totals, not per-skill contribution. |

The current launch configuration pins Psyche
`bf03117b424413cea4c3df7cf76a279127c8567d`, Mind
`0f990b61bc6f89b60f05a34cc1c4a36709406f70`, and Field
`5a542ba4f87365df5eebda2e85338bb553c00fcb` in
`/home/li/primary/config/main-flow/shared.edn:4-12` and
`/home/li/primary/flake.nix:21-35`, observed 2026-10-14. These are configured
source pins, not proof that generated or deployed runtime contexts are
equivalent to them.

## Boundary

The defensible conclusion is conditional: loaded input must fit the available
context budget, while adherence depends on constraints and composition,
dependencies, position, hierarchy, task, model version, and output demand.
The useful split threshold remains an open measurement question for the target
model and workload.
