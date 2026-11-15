# 0001 Linux kernel with our own user space

**Status:** Proposed

## Context
Writing a new kernel takes decades, mainly because of drivers. Windows compatibility lives mostly in user space (the Win32 API), not in the kernel. ReactOS shows how slow a full NT re-implementation is.

## Decision
Use the Linux LTS kernel without a distribution, and build our own user space on top: broker, desktop, settings, store and installer.

## Consequences
- Drivers for most hardware are available from day one.
- Windows kernel drivers (`.sys`) and kernel anti-cheat will not work.
- A custom kernel stays possible later, but is not a goal.
