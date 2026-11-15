# 0005 Wayland and Qt 6 for the desktop

**Status:** Proposed

## Context
The desktop must feel familiar to Windows users, be fast, support HDR, multiple monitors with different scaling, touch and pen, and offer Remote Desktop (RDP) as server and client.

## Decision
Build our own desktop shell on Wayland with Qt 6 (QML for the interface), with XWayland for older applications. Reuse proven parts where possible (for example KDE components for RDP and window management) instead of writing everything from scratch.

## Consequences
- Mature toolkit with good translation (Qt Linguist) and accessibility support.
- The look is our own; Microsoft's design and icons are not copied.
