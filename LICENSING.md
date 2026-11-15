# Licensing

LuxyOS uses three licences, one for each kind of work. All three are free and open.

| What | Licence | File |
| --- | --- | --- |
| **The operating system**: the broker, desktop, settings, store, installer, migration assistant and every other LuxyOS component | GNU General Public License v3.0 or later (`GPL-3.0-or-later`) | [LICENSE](LICENSE) |
| **The SDK**: libraries, headers, templates, sample code and tools that app developers build with (later in `sdk/`) | Apache License 2.0 (`Apache-2.0`) | [LICENSE-APACHE](LICENSE-APACHE) |
| **Documentation and designs**: everything in `docs/`, including the screen designs and diagrams | Creative Commons Attribution 4.0 International (`CC-BY-4.0`) | [LICENSE-CC-BY](LICENSE-CC-BY) |

## Why these three

- **GPL-3.0 for the system.** Anyone may use, study, change and share LuxyOS. Anyone who distributes a changed version must publish their changes under the same licence, so improvements stay open for everyone.
- **Apache-2.0 for the SDK.** App developers, including companies with closed-source apps, can build for LuxyOS without having to open their own code. Apache-2.0 also includes a patent grant.
- **CC BY 4.0 for documents and designs.** Anyone may reuse and adapt them, as long as they credit "Nijaz Omanovic and the LuxyOS contributors" and link to this repository.

## Not covered by these licences

- **The LuxyOS name and logo** are trademarks. The files in [brand/](brand/) and the logo in the designs are not covered by CC BY 4.0. How you may use them is described in [TRADEMARKS.md](TRADEMARKS.md).
- **Third-party components** keep their own licences, for example the Linux kernel (GPL-2.0), Wine (LGPL-2.1-or-later), Mesa (MIT) and Qt (LGPL-3.0). Each package records its licence.
- **Example names in the designs** (apps, companies, people) are made up. Product names such as Microsoft Word or Steam belong to their owners and are used only to describe compatibility.

## For contributors

- A contribution is licensed under the licence of the part it changes: system code under GPL-3.0-or-later, SDK code under Apache-2.0, documentation and designs under CC BY 4.0.
- Every new source file starts with an SPDX header, for example `// SPDX-License-Identifier: GPL-3.0-or-later` or `# SPDX-License-Identifier: Apache-2.0`.
- Sign off your commits (`git commit -s`, Developer Certificate of Origin). See [CONTRIBUTING.md](CONTRIBUTING.md).

## Free and non-commercial

LuxyOS is free for everyone and the project is non-commercial ([docs/terms.md](docs/terms.md)). GPL-3.0 does not allow a ban on commercial use, and LuxyOS builds on GPL software (Linux, Wine), so the licence cannot add one. Companies may use LuxyOS freely. What is protected is the name: nobody may charge for LuxyOS itself under the LuxyOS name ([TRADEMARKS.md](TRADEMARKS.md)).

## EU rules

LuxyOS follows EU law in every country ([docs/europe.md](docs/europe.md)). An open-source licence cannot require users to follow EU law, so the rules for partners (distributors, device makers, store developers and managed service providers) are set in the store terms, partner agreements and the [trademark policy](TRADEMARKS.md).

Copyright © 2026 Nijaz Omanovic and the LuxyOS contributors. Ownership and disclaimer: [LEGAL.md](LEGAL.md).
