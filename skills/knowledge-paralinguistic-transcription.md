---
description: Verified current facts about Android speech transcription, prosody-related output, providers, and IME insertion.
dependencies: [knowledge-context-strata]
---

Google's current Gemini audio documentation exposes transcription, translation,
speaker diarization, timestamps and emotion detection. Its structured example
uses speaker, timestamp, content, language and an emotion enum. These are model
judgments in a requested schema; they are not documented acoustic measurements
of pitch, loudness, speaking rate, pause duration, prosody contours or
calibrated confidence. [Evidence](../evidence/android-paralinguistic-transcription-sources.md)

The dedicated Gemini transcription documentation describes verbatim output,
which preserves fillers, repetitions, false starts and pauses as text, and
smart cleanup, which changes that representation. Its documented word and
speaker timestamps do not establish prosody annotations. The Live
transcription route documents interim and final input transcription, utterance
timing, a ten-minute transcription session limit, and smart cleanup/custom
vocabulary behavior; it documents no word timestamps or diarization for that
route. General Live API capabilities and affective dialogue must not be
substituted for these route-specific facts.

Published Gemini token rates can estimate provider input/output cost under
stated token assumptions. They do not establish an all-in per-minute cost or
end-to-end latency for a keyboard, markup, model analysis, backend or network
path. No matched accuracy or latency comparison with Wispr was found. Wispr's
Android product is an accessibility/overlay flow whose listing describes
removing fillers, stutters, false starts and self-corrections; that documents
cleanup behavior rather than preserved prosody. Its dated Play and help pages
currently conflict about free/unlimited use versus a 1,000-word mobile weekly
limit, so the conflict remains explicit. vBoard documents Gemini through
OpenRouter; this is not evidence of direct paid Gemini API routing. Loquela and
Dictus document local-leaning alternatives, but their model catalogs and
privacy claims are not device accuracy or latency measurements.

Android's documented custom keyboard path is `InputMethodService` plus
`InputConnection` composing and `commitText`. A custom tag can be committed as
literal text and consumed by a downstream machine, while ordinary target apps
still treat it as text rather than shared prosody semantics. Microphone and
foreground-service restrictions, IME lifecycle, OEM behavior and sensitive
field policy require target-device verification. Long-lived provider keys
belong off-device; restricted Live ephemeral tokens still require a backend and
do not automatically cover every API route.

A minimal implementation shape remains a design option: microphone button or
bounded utterance capture, stop/VAD, a model adapter, separate raw words and
annotation result, user review, and `commitText` of accepted text or literal
markup. A local ASR route may improve privacy but does not itself produce
prosody. Literal markup and a separate display/export representation are both
open choices. [Primary evidence and URLs](../evidence/android-paralinguistic-transcription-sources.md)
