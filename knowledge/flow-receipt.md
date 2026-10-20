---
description: Startup and queue delivery receipts in Flow 0.37.1.
dependencies: [vision-flow, knowledge-flow]
---

Source: Flow 0.37.1, `fc53f4f`, `crates/flow-nexus/src/herdr/launch.rs`, `sending.rs` and `waking.rs`.

Launch and Send receipts describe different operations. `Launch` composes declared modules and a brief into a native start. `Send` answers `Queued` or `Delivered` on its successful paths. Neither a queue receipt nor an interrupt witness proves that a recipient completed the request.

During startup, Flow records the SHA-256 of each submitted prompt part and reads the native transcript for the expected session. Each observed user part must match the next recorded hash. A differing part refuses as `PartDiffers`; an accepted launch additionally requires the expected native model and effort evidence.

Claude pasted parts are checked by reconstructing the recorded `pasted_content` element. The reconstruction preserves a part's trailing newline and applies the native tag escape; it must equal the transcript element byte for byte. The former newline-stripping failure is not the selected 0.37.1 implementation.

For a fresh Codex start, the implementation materializes the named thread's rollout before the TUI resumes it, without starting its first turn. The first turn follows attachment; creating a thread alone is not a startup receipt.

Queue delivery has its own durable attempt and receipt. Claude uses the correlated native session, submitted-prompt evidence and transcript; Codex uses its app-server turn history. An uncertain delivery stays unresolved until native evidence or an explicit supported resolution settles it. A Send result alone is not evidence that an uncertain attempt was absent.

```sh
flow 'Current.{ Psyche core Secondary }'
flow-meta 'ReadQueueDeliveries.{ Psyche core Secondary }'
```

The first query reads the metaflow's current state. The second reads its attempted queue deliveries. Neither query sends a new body, repeats a launch or resolves an uncertain delivery.

The source observations here do not certify a fresh native launch. Installed version, source checks, startup receipt, queue receipt and recipient response remain distinct evidence.
