# Store: working plan

The store starts on GitHub: developers submit their app as a small manifest in a public repository, IT DeXt reviews it, and LuxyOS signs and distributes it. A developer portal of our own comes later.

Store terms for developers: [terms.md](terms.md#2-store-terms-for-developers). Decision: [0012](decisions/0012-store-starts-on-github.md).

## Decisions (16 November 2026)

| Question | Decision |
| --- | --- |
| How do developers submit apps? | On GitHub first, like Flathub and winget. Own developer portal in phase 2 |
| How do we check developers? | Free apps: a GitHub account with two-factor authentication. Paid apps: also trader details (name, address, email, phone, trade register number, ID), required by the Digital Services Act |
| Who reviews apps? | IT DeXt. The review process is worked out when the build starts |
| Domains and servers | Later, once the plan works |

## How an app gets into the store (phase 1)

1. The developer opens a pull request in the store repository, with one folder per app:
    - the manifest: name, version, permissions, network use, the data the app collects, and whether the app uses AI (local or online);
    - a link to the package or the source code, with a checksum;
    - icon, description, screenshots and licence;
    - for a paid app: the price and the link to the developer's own website.
2. Automatic checks in GitHub Actions: complete manifest, checksum, malware scan, licence, and a sandbox test that checks the app does nothing outside its manifest.
3. IT DeXt reviews each developer's first app, and every app with sensitive permissions (camera, microphone, all files, online AI). The decision and its reasons are written in the pull request.
4. Approved: the build server signs the package with the LuxyOS key and adds it to the catalogue.
5. Rejected: the developer fixes the app in the same pull request. Appeals go through an issue.
6. Updates take the same route, or arrive automatically with a new GitHub release. An update that asks for no new permissions only needs the automatic checks. New permissions mean a new review by IT DeXt.

Trader details for paid apps never go into the public repository. The developer sends them to a fixed email address (to be created), IT DeXt checks them, and the store page shows only what the Digital Services Act requires.

## How a user downloads an app

1. Open the store and choose an app. The page shows what the app does, its permissions, Windows or Linux, the compatibility label, where it comes from (*Verified* or *From GitHub*) and, for paid apps, the price with a link.
2. Install: the user confirms the permissions.
3. LuxyOS checks the signature, IT DeXt Antivirus scans the app, and the app runs in its own sandbox.
4. Updates install by themselves.

No account is needed to download. The store sends nothing about the user and only counts downloads per app per day, without storing IP addresses.

## What we build

| Part | What it does | Reuse |
| --- | --- | --- |
| Store repository | One folder per app, plus the rules for submitting | Layout of winget-pkgs and Flathub |
| Checks | Manifest, checksum, malware scan, licence, sandbox test | GitHub Actions, flatpak-builder, ClamAV, the IT DeXt scanner |
| Build and signing server | Builds and signs packages; the key is kept in a hardware security module | flat-manager (Flathub) |
| Catalogue | All apps and their details, for the store app | AppStream |
| Download server | Packages and updates, in the EU | Flatpak repository; mirrors later |
| Store app in LuxyOS | Search, install, updates, permissions | Own, in Rust and Qt, with the `app` package manager |

Windows programs from other makers are downloaded from the maker's own website with a fixed checksum, as winget does. That costs LuxyOS no traffic.

## Order of work

1. Fix the manifest format, the same as the SDK manifest.
2. The store repository with its rules and automatic checks.
3. The build and signing server and the download server. Create the domains at this step.
4. The store app in LuxyOS, for the 2027 test version.
5. Phase 2: own developer portal with accounts and an overview per developer. Phase 3: web store.

## Still open

- How IT DeXt reviews apps and which tooling it uses.
- Domains, servers and the email address for developers.
- Name of the store repository on GitHub.
