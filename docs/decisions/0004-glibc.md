# 0004 glibc as C library

**Status:** Proposed

## Context
Smaller C libraries (musl) are attractive for a minimal system, but Steam, Wine, NVIDIA drivers, RMM agents and most commercial Linux software are built against glibc.

## Decision
Use glibc.

## Consequences
- Maximum compatibility with existing Linux software.
- Slightly larger base system; acceptable.
