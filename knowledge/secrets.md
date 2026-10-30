---
description: A secret must reach a program without reaching the agent; load before any command that handles a credential.
dependencies: []
---

Verify the consumer’s official stdin or file-descriptor interface first.
Pipe GoPass producer output directly to that consumer.
Use `set -o pipefail`.
Use absolute or verified executables where appropriate.
Suppress secret-bearing output. A secret travels by pipe from GoPass straight into the consumer’s verified stdin
or file-descriptor interface, and by that path alone.
Name the unavoidable crypto-backend, kernel, and consumer boundary as the exact extent of isolation held.
Persistent import is allowed when the consumer’s supported contract requires it and the task authorizes credential setup.

A secret or pairing code reaches the living only through its own device flow.
