# Made for Europe

LuxyOS is made in and for the European Union. **EU law is the baseline for everything LuxyOS does, in every country.** People and businesses outside the EU are welcome to use it, and they get the same European level of protection.

## Rules

1. **One version, one standard.** There is no weaker version for other countries. Privacy, security and accessibility are the same everywhere.
2. **EU law as the minimum.** Where local law asks for more protection, LuxyOS can do more. It never does less than EU law requires.
3. **Data stays in Europe.** Update servers, the store, registration and backups run in the EU, with EU providers. No data goes outside the EU without the user's explicit permission.
4. **Partners follow EU rules too.** Anyone who distributes LuxyOS, sells devices with it, offers apps in the store or provides managed services must meet EU rules for that work, wherever they are based.
5. **European organisation.** The organisation behind LuxyOS is established in an EU member state.

## EU laws and what they mean for LuxyOS

| Law | What it means for LuxyOS |
| --- | --- |
| **GDPR**, General Data Protection Regulation | Privacy by design and by default. No telemetry or advertising ID. Users can see, export and delete their data. Registration only with consent. |
| **ePrivacy Directive** | No reading from or storing on the user's device without consent, unless strictly needed for the function the user asked for. |
| **Cyber Resilience Act (CRA)** | Operating systems are an "important product" under the CRA. Secure by default, no known exploitable vulnerabilities at release, security updates for the whole support period, a software bill of materials (SBOM), a vulnerability handling process, and reporting of actively exploited vulnerabilities. CE marking before sale. |
| **European Accessibility Act (EAA)** | Operating systems for consumer computers must be accessible: screen reader, keyboard-only use, high contrast, scalable text, captions and accessible documentation. |
| **AI Act** | Clear labels when AI is used, no hidden AI features. Administrators can block AI completely, allow local AI only, or allow everything. |
| **Digital Services Act (DSA)** | Rules for the store as an online marketplace: known and traceable sellers, a way to report illegal apps, clear reasons when an app is removed. |
| **Digital Markets Act (DMA)**, as an example to follow | Free choice of browser, search engine and antivirus (choice screen); default apps can be changed and removed; no self-preferencing in the store. |
| **Digital Content Directive** | Updates to keep LuxyOS working and secure as promised; clear information about what is included. |
| **Product Liability Directive** (new) | Software counts as a product: careful release process, testing and documentation. |
| **eIDAS 2** | Support for qualified certificates, smart cards and the European Digital Identity Wallet. |
| **NIS2** | Features that help business customers meet NIS2: logging, central management, update reports, encryption, incident support. |
| **Ecodesign rules for phones and tablets** | For the later phone version: operating system updates for at least five years after a model leaves the market. |

This table is a starting point, not legal advice. Before the first release, a lawyer specialised in EU digital law must check it.

## What this means in the product

- Privacy overview, opt-in for everything that sends data, per-app internet switches ([requirements](requirements.md#privacy-and-security)).
- Choice screen at first start, see [design 02](design/02-first-start-choices.png).
- Accessibility is part of every design review; issue [#12](https://github.com/nijazo/luxyos/issues/12) includes it.
- Security process: SBOM per release, signed updates, a public security policy ([SECURITY.md](../SECURITY.md)) and support periods stated for each release.
- All official EU languages ([languages](languages.md)).

## Open points

- Choose the EU member state and legal form of the organisation.
- Licences are chosen ([LICENSING.md](../LICENSING.md)). An open-source licence cannot require users to follow EU law, so the rules for partners are set through store terms, partner agreements and the [trademark policy](../TRADEMARKS.md).
- Plan the CRA conformity assessment for the first release.
