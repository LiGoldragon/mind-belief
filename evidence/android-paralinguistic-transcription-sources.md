# Android paralinguistic transcription research evidence

Checked 2026-10-14. This file preserves the primary source trail for the
knowledge and inquiry modules. A provider's documented field or product claim
is not an acoustic measurement, and a marketing claim is not a matched trial.

## Primary API and platform sources

- Google, [Audio understanding](https://ai.google.dev/gemini-api/docs/audio):
  documents transcription, translation, speaker diarization, timestamps and
  emotion detection; its structured example uses speaker, timestamp, content,
  language and an emotion enum. Those are model output judgments. The page
  does not document returned pitch, loudness, speaking rate, pause duration,
  prosody contours or calibrated confidence.
- Google, [Audio transcription](https://ai.google.dev/gemini-api/docs/transcribe):
  documents `gemini-3.5-transcribe` through `interactions.create`, uploaded or
  inline audio, word and speaker timestamps, custom vocabulary, verbatim mode
  and smart cleanup. Verbatim mode preserves fillers, repetitions, false
  starts and pauses as text; smart cleanup changes that representation. Smart
  mode cannot combine with word timestamps or diarization. `custom_vocabulary`
  accepts up to 1,000 terms but cannot combine with speaker diarization or
  word-level timestamps. The page's fields do not establish acoustic prosody.
- Google, [Live transcription](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe):
  documents the `gemini-3.5-transcribe-live` route, interim and final input
  transcription, utterance timing, a ten-minute session limit, and live smart
  cleanup/custom vocabulary behavior. It documents no word timestamps or
  diarization for this route. These limits are kept separate from general Live
  API claims, whose current general model listing names `gemini-3.8-live`.
- Google, [Models](https://ai.google.dev/gemini-api/docs/models) and
  [Audio understanding](https://ai.google.dev/gemini-api/docs/audio): the
  current model/API pages name the dedicated transcription routes above and
  general `gemini-3.8-live`; the audio-understanding structured example uses
  speaker, timestamp, content, language and an emotion enum. Emotion labels
  are model judgments, not calibrated acoustic measures. The absence of named
  pitch, loudness, speaking-rate, pause-duration or prosody fields does not
  prove a model cannot infer them; timing gaps can also support derived pause
  or pace proxies that still require validation.
- Google, [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing):
  current published dedicated-transcript estimates are about $0.005/min for
  batch `gemini-3.5-transcribe` and $0.009/min for live
  `gemini-3.5-transcribe-live`, based on 25 audio tokens/second and 175 text
  tokens/minute assumptions. They are not an all-in per-minute cost for a
  keyboard, richer annotation, markup, model analysis, backend or network
  path. The paid rows say prompts/responses are not used to improve products;
  limited abuse and safety logging still applies.
- Google, [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview),
  [logs and datasets](https://ai.google.dev/gemini-api/docs/logs-datasets),
  [terms](https://ai.google.dev/gemini-api/terms) and
  [usage policies](https://ai.google.dev/gemini-api/docs/usage-policies):
  Interactions defaults to 55-day paid or 1-day free storage; `store=false`
  opts out of Interaction storage but does not erase all abuse/safety logs and
  disables `previous_interaction_id` and background execution. Paid-service
  data is not used for product improvement, while unpaid use may be. EEA, UK
  and Switzerland paid-service/data-use exceptions must be checked for the
  account and route; these terms do not transfer to OpenRouter or vBoard.
- Android, [Create an input method](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method):
  documents `InputMethodService`, the input-method service declaration and
  `EditorInfo` lifecycle.
- Android, [`InputConnection`](https://developer.android.com/reference/android/view/inputmethod/InputConnection):
  documents `commitText` and composing/selection operations. A custom
  paralinguistic tag can therefore be inserted as literal text, but target
  applications do not thereby acquire shared prosody semantics.
- Android, [Sharing audio input](https://developer.android.com/media/platform/sharing-audio-input)
  and [foreground-service types](https://developer.android.com/develop/background-work/services/fgs/service-types):
  document microphone and foreground-service restrictions. Whether a given
  IME lifecycle and OEM permits capture needs device testing; a visible IME is
  not treated as a universally visible Activity.
- Google, [API key guidance](https://ai.google.dev/gemini-api/docs/api-key) and
  [Live ephemeral tokens](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens):
  support keeping long-lived keys off-device and issuing restricted short-lived
  Live tokens from a backend. Live-token guidance is not assumed to cover every
  non-Live interaction route.

## Product and implementation surfaces

- [Wispr Flow Android listing](https://play.google.com/store/apps/details?id=com.wispr.flowapp)
  and [Android setup](https://docs.wisprflow.ai/articles/8858845757) describe an
  Android 13+ accessibility/overlay flow with microphone, accelerometer,
  overlay, accessibility and internet requirements. The listing's cleanup
  language (fillers, stutters, false starts and self-corrections) is evidence
  of intentional cleanup, not preservation of prosody annotations. No
  selectable backend/model or matched accuracy/latency trial was found.
- [Wispr privacy](https://wisprflow.ai/privacy), [security FAQ](https://docs.wisprflow.ai/articles/3467817258-security-and-compliance-faq),
  [pricing](https://wisprflow.ai/pricing), [plans](https://docs.wisprflow.ai/articles/9559327591-flow-plans-and-whats-included),
  and [Android limits](https://docs.wisprflow.ai/articles/4877130308-plans-upgrades-and-word-limits-on-android)
  document cloud transcription, separate model-improvement and dictation
  storage controls, and changing plan/limit claims. The Pro pricing view is
  $15/month or $12/month when billed annually. The September 4 Play listing
  says free unlimited for now, while the September 29 Android help page says
  1,000 mobile words/week shared by Android and iOS, a 1,000-word soft limit
  and 1,500-word hard cap; the October 11 troubleshooting page confirms a
  weekly limit. These dated claims remain a source ambiguity, not one
  universal quota.
- [vBoard](https://www.srizon.com/vboard) describes an actual Android keyboard
  whose audio/text is sent to Gemini through OpenRouter. It does not establish
  direct paid Gemini API use, a selectable model, prosody fields, or a public
  accuracy/latency benchmark.
- [WhisperToInput](https://github.com/aptdnfapt/whisper-gemini-to-input) is a
  GitHub APK keyboard README claiming OpenAI Whisper or Google Gemini API
  options. Current code, license, route, retention, pricing and model need
  inspection before they become stronger claims; no prosody benchmark is
  documented.
- [Loquela](https://www.getloquela.com/) describes a Play-distributed Android
  keyboard with local ASR by default and optional remote providers. Its model
  catalog and 454/5529 MB labels are catalog facts, not device benchmarks;
  local audio-in-memory and provider privacy claims remain product claims; the
  paid Full unlock amount was not publicly established in the checked source.
- [Dictus](https://github.com/getdictus/dictus-android) describes an open-source
  Android IME using local Whisper/whisper.cpp and Parakeet/sherpa-onnx, with
  no-account/no-cloud claims and a free project claim. Its source and README
  document no prosody annotation or device benchmark.
- [HeliMic](https://github.com/Duro02/HeliMic) and
  [Deskdrop](https://github.com/SvReenen/Deskdrop) are possible customizable
  forks/endpoints, not evidence that a selected license, model, language,
  device or cloud path is suitable.

No matched target-device/language/network trial was run, no audio or userdata
was collected, and no provider API was called. No source establishes an
objectively better-than-Wispr product.
