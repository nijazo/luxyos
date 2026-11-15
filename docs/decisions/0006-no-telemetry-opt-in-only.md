# 0006 No telemetry; everything that sends data is opt-in

**Status:** Proposed

## Context
Privacy is a core promise: nothing leaves the system without the user's permission.

## Decision
No telemetry and no advertising ID. Crash reports, sync and cloud backup are off by default. Update checks download the version list and compare locally, so the list of installed programs never leaves the computer. A privacy overview shows every connection per program, with per-app internet switches.

## Consequences
- We need other ways to learn about problems: opt-in crash reports, public issue tracker, compatibility reports filled in by users.
- Windows programs can still send data themselves; the OS makes this visible and blockable.
