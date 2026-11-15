# 0008 Read-only system image with A/B updates

**Status:** Proposed

## Context
Updates must never break a computer, a reset must always give a clean system, and users must be able to roll back with one click.

## Decision
The system part is a read-only, compressed image. Updates are written to the inactive slot (A/B) in the background and activate on the next boot. User data lives on a separate Btrfs volume with snapshots.

## Consequences
- One-click rollback and reliable factory reset ("keep files" or "remove everything").
- Software that writes to system directories must be packaged differently.
