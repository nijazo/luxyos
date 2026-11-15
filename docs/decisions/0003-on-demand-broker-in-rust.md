# 0003 On-demand broker written in Rust

**Status:** Proposed

## Context
The core promise is that only what is needed runs. Existing init systems start many services at boot by default. LuxyOS also needs real closing of programs and permission-based background running.

## Decision
Write our own broker in Rust. It starts only the display and login at boot, activates services on first request (socket and D-Bus style), stops idle services, runs each app in its own cgroup, freezes idle background apps, and offers a systemd-compatible interface for third-party agents.

## Consequences
- Memory safety and good performance for a core component.
- Extra work: compatibility with software that expects systemd.
- The broker is the first prototype to build and test in QEMU.
