---
description: Source map and measurements for provider caching, compaction triggers, wait costs, and long-context quality.
---

## Scope and method

This evidence was re-read on 2026-10-14 from the linked provider documentation and benchmark sources. It is evidence for knowledge modules; it does not establish a runtime handover policy. Provider documentation describes API behavior, while Claude Code and Codex CLI behavior also depends on the installed client, model, gateway, and account configuration.

## Claude Code compaction

The installed Claude Code witness was version 2.1.294 (`claude --version`). Its help exposed `--autocompact <auto|tokens>` and token values from 100K through 1M. No paid or live compaction probe was run.

The current Claude Code model configuration documentation says that Sonnet 4.6 and Opus 4.6 without extended context compact at the 200K boundary. Models with a native 1M window compact at about 967K by default. It also says a gateway can impose a lower limit that Claude Code cannot detect, and exposes `CLAUDE_CODE_AUTO_COMPACT_WINDOW` for setting a lower boundary. These are configured/default boundaries, not a universal observed request-trigger count or a reserved-buffer measurement.

Source: [Claude Code model configuration](https://code.claude.com/docs/en/model-config), lines 684-685, 692-694, 733-737, read 2026-10-14.

The Claude context-window documentation describes compaction as replacing history with a summary while restoring selected files, skills, plans, and other context separately. It gives no fixed compression ratio. Existing module measurements remain the primary local sample: four boundaries of 336,492 to 22,932, 286,071 to 26,396, 334,233 to 22,952, and 281,533 to 21,803, with first subsequent request inputs of 59,499, 63,691, 58,649, and 58,196. Boundary estimates and subsequent request inputs are different metrics and must not be mixed into a billing or universal reduction claim.

Source: [Claude Code context window](https://code.claude.com/docs/en/context-window), read 2026-10-14; local `skills/knowledge-compaction.md`, four named transcript boundaries.

Claude's prompt-caching documentation says compaction can read a warm prefix and documents an optional idle compaction shortly before expiry on a one-hour cache path. Idle compaction can be disabled. This is evidence for that one-hour idle path only; ordinary automatic compaction is separate, and the documentation does not establish that all automatic or manual compaction is TTL-scheduled.

Source: [Claude prompt caching](https://code.claude.com/docs/en/build-with-claude/prompt-caching), compaction section, read 2026-10-14.

## Claude API cache timing and accounting

The Claude API default cache lifetime is 5 minutes. An optional 1-hour TTL is available. Reuse refreshes the entry without a new write charge. Lifetime starts when the request that writes or reads the entry starts, and generation time consumes that lifetime; a four-minute response therefore leaves about one minute for the next request to hit. A cache entry becomes available after the first response begins, so a concurrent request sent before that point cannot rely on a hit.

The documented usage fields are `cache_creation_input_tokens` and `cache_read_input_tokens`; ordinary `input_tokens` excludes cached input. The current pricing documentation gives, generally, 1.25x base input price for 5-minute writes, 2x for 1-hour writes, and 0.1x for reads, with model-specific exceptions. These are API billing rules, not Claude Code subscription accounting.

Sources: [Claude prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), lines 104-121, 161-173, 325-333, read 2026-10-14.

No provider-documented advance-warning signal for cache expiry was found. A response usage record proves a hit or write after the request; it does not warn that the next request will miss. A long tool wait can therefore outlast the remaining TTL. The wait itself does not create input or output token usage; the next request is charged according to its ordinary, cache-read, and cache-write usage fields.

## OpenAI API cache timing and compaction

For newer supported models, OpenAI documents `prompt_cache_options.ttl` with the only supported value `30m` as the default. A cached prefix remains eligible for at least 30 minutes after its latest write or reuse, and may be retained longer. For earlier models, `in_memory` typically remains active for around 5-10 minutes of inactivity, up to one hour; `24h` typically remains available around 30 minutes and may remain up to 24 hours. For models supporting both, the default depends on the organization's data-retention policy: `24h` without Zero Data Retention and `in_memory` with it. These are retention guarantees and typicals, not a promise that every entry survives the maximum period.

For GPT-5.6 and later, OpenAI documents `cache_write_tokens`; writes cost 1.25x the uncached input rate, reads cost 0.1x on most of those models, and GPT-6.1 Sol reads cost 0.05x. Earlier generations have no additional cache-write charge, and cached-input rates are model-dependent. Therefore the 1.25x/0.1x pair must not be applied universally across OpenAI generations. OpenAI's usage-cost example defines `ordinary_input_tokens = input_tokens - cached_tokens - cache_write_tokens`, then weights cached reads and writes by model-specific multipliers. It explicitly says to compare `cached_tokens`, `cache_write_tokens`, latency, and total cost. No advance expiry signal is documented. Cache location and routing matter: entries are machine-local; prefix keys influence routing but do not guarantee a hit.

Sources: [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching), lines 1381-1400, 1424, 1716-1733, 1807-1813, read 2026-10-14.

OpenAI server-side compaction is separately opt-in through Responses `context_management` with `compact_threshold`. When the streamed context crosses that threshold, the server emits a compaction output item and prunes context before continuing inference. The standalone compact endpoint is stateless and returns a context for a later request. This is context management, not a cache-TTL scheduler.

Source: [OpenAI compaction](https://developers.openai.com/api/docs/guides/compaction), lines 947-960 and 1345-1351, read 2026-10-14.

The local Codex CLI witness supplied for this research was 0.158.0-alpha.9, while the existing module's prior evidence is for 0.161.0-alpha.2. Current upstream source names `auto_compact_token_limit` and derives a missing limit from the resolved context with a 90% clamp, but upstream main is not proof of installed-binary behavior. No Codex CLI TTL scheduler or exact local model threshold was witnessed.

## Quality versus context measurements

These studies measure task-specific behavior, not a universal handover threshold or agent coding quality.

NoLiMa's published table reports GPT-4o at 99.3% short-context baseline, 98.1%, 98.0%, 95.7%, 89.2%, 81.6%, 69.7%, 62.4%, and 56.0% at 1K through 128K. Its effective length is defined as the longest context retaining at least 85% of the short-context baseline; GPT-4o is listed at 8K. The 64K and 128K points use fewer placements and have token-limit constraints. This is semantic retrieval, not coding success.

Source: [NoLiMa results](https://github.com/adobe-research/NoLiMa#results), table and methodology, read 2026-10-14.

LongCodeBench reports LongSWE executable patch success for Claude 3.5 Sonnet at 29%, 19%, 15%, and 3% in its 32K, 64K, 128K, and 256K buckets; GPT-4o is reported at 11%, 6%, and 5% at 32K, 64K, and 128K. The buckets also change corpus/file-set size, and the paper's model/context labels and API tokenization are not an independent certification of provider capacity. The benchmark reports coding task success, but it cannot yield a universal handover percentage.

Source: [LongCodeBench](https://arxiv.org/html/2505.07897v3), Table 3 and sections 4.2-4.4, read 2026-10-14.

## Boundaries

Cache eviction removes prefix reuse; compaction changes transcript state; long-context quality degradation is a third phenomenon. A new handover thread may alter the prefix and may omit details, but these sources do not prove that it saves cache cost or preserves every fact. No current source supplies a universal expiry-warning signal, safe deadline margin, or quality-preserving handover threshold.

## Sources

- Claude Code 2.1.294 local `--version` and `--help`, observed 2026-10-14.
- `skills/knowledge-compaction.md`, prior local Claude and Codex measurements, retained unchanged except for cross-links added by the landing.
- Provider and benchmark links cited in each section, re-read 2026-10-14.
