# 0002 Windows software via Wine and Proton

**Status:** Proposed

## Context
Users must be able to run their Windows programs. A compatibility layer in user space is proven (Wine, Proton on Steam Deck). Professional software (Adobe, AutoCAD, AVEVA) depends heavily on Windows services, .NET/WPF, DCOM and licensing services.

## Decision
Ship Wine, DXVK, VKD3D-Proton and Wine Mono, hidden behind normal double-click installation. Use NTSYNC for performance. Show honest compatibility labels. Set up a "Proton for work" effort (with CodeWeavers) for professional software. An integrated Windows VM is a temporary fallback only.

## Consequences
- Most programs and games work; kernel anti-cheat games do not.
- A compatibility test lab for the top 50 business programs is needed.
- Dual boot ("next to Windows") and cloud gaming cover games that cannot work.
