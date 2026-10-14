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
  documents the dedicated `gemini-3.5-transcribe` route, uploaded or inline
  audio, word and speaker timestamps, custom vocabulary, verbatim mode and
  smart cleanup. Verbatim mode preserves fillers, repetitions, false starts
  and pauses as text; smart cleanup changes that representation. The page's
  timestamp and diarization fields do not establish acoustic prosody.
- Google, [Live transcription](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe):
  documents interim and final input transcription, utterance timing, a
  ten-minute transcription session limit, and live smart cleanup/custom
  vocabulary behavior. It documents no word timestamps or diarization for
  this route. These limits are kept separate from general Live API claims.
- Google, [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing):
  current published transcribe and live-transcribe token rates support only
  estimates under stated token assumptions; they are not an all-in per-minute
  guarantee for a keyboard, markup, model analysis, backend or network path.
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
  storage controls, and changing plan/limit claims. The September 4 Play
  listing says free unlimited for now, while the September 29 Android help
  page says 1,000 mobile words/week shared by Android and iOS with soft and
  hard caps; the October 11 troubleshooting page confirms a weekly limit.
  These dated claims remain a source ambiguity, not one universal quota.
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
  local audio-in-memory and provider privacy claims remain product claims.
- [Dictus](https://github.com/getdictus/dictus-android) describes an open-source
  Android IME using local Whisper/whisper.cpp and Parakeet/sherpa-onnx, with
  no-account/no-cloud claims. Its source and README document no prosody
  annotation or device benchmark.
- [HeliMic](https://github.com/Duro02/HeliMic) and
  [Deskdrop](https://github.com/SvReenen/Deskdrop) are possible customizable
  forks/endpoints, not evidence that a selected license, model, language,
  device or cloud path is suitable.

No matched target-device/language/network trial was run, no audio or userdata
was collected, and no provider API was called. No source establishes an
objectively better-than-Wispr product.
