# 0012 The store starts on GitHub; IT DeXt reviews apps

**Status:** Accepted

## Context
LuxyOS needs a store where users download apps and developers register to offer their own software. A full developer portal with accounts, dashboards and identity checks is a lot of work and server cost before the first test version exists. Flathub and winget show that a public Git repository with automatic checks works well for submitting apps.

## Decision
- Phase 1: developers submit apps with a manifest in a public GitHub repository, by pull request. Automatic checks run in GitHub Actions. A developer portal of our own follows in phase 2, a web store in phase 3.
- Free apps need a GitHub account with two-factor authentication. Paid apps also need trader details as the Digital Services Act requires; these are sent privately and never stored in the public repository.
- IT DeXt reviews each developer's first app and every app with sensitive permissions. Reasons for decisions are written in the pull request.
- Domains and servers are chosen later, once the plan works.

Working plan: [store.md](../store.md).

## Consequences
- Developers can start without any LuxyOS account or server, and the review history is public.
- The signing key and the download server must still be set up before the 2027 test version.
- Developers without a GitHub account cannot submit until the portal exists in phase 2.
