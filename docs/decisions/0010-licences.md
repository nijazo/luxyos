# 0010 Licences: GPL-3.0 for the system, Apache-2.0 for the SDK, CC BY 4.0 for documents

**Status:** Accepted

## Context
Developers only contribute to a project with a clear open-source licence. LuxyOS builds on GPL and LGPL software (Linux, Wine, Qt). App developers, including companies with closed-source apps, must be able to build for LuxyOS. The documentation and designs should be reusable.

## Decision
- Operating system components: **GPL-3.0-or-later**.
- SDK (libraries, templates, sample code, developer tools): **Apache-2.0**.
- Documentation, designs and diagrams: **CC BY 4.0**.
- The LuxyOS name and logo are trademarks, covered by [TRADEMARKS.md](../../TRADEMARKS.md), not by the licences.
- Contributions use the licence of the part they change, with an SPDX header in every source file and a DCO sign-off.

Details: [LICENSING.md](../../LICENSING.md).

## Consequences
- Improvements to the system stay open: whoever distributes a changed version must share the source.
- Commercial app makers can use the SDK without opening their apps.
- GPL-3.0 code cannot be combined with GPL-2.0-only code in one program; the Linux kernel stays a separate program, so this is no problem.
- Rules for partners (EU law, privacy) are enforced through the trademark policy and partner agreements, not through the licence.
