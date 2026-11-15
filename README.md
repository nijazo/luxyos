<p align="center"><img src="brand/luxyos-logo.svg" width="96" alt="LuxyOS logo"></p>

<h1 align="center">LuxyOS</h1>

<p align="center"><strong>A fast, free and honest operating system.</strong><br>
It only starts what you use, runs your Windows programs, and sends nothing without your permission.</p>

<p align="center"><a href="https://luxyos.com"><strong>luxyos.com</strong></a> · <a href="https://luxyos.com/nl/">Nederlands</a> · <a href="#how-to-help">Help build it</a> · <a href="https://paypal.me/nijazo">Donate to LuxyOS</a></p>

---

> **Status: design phase.** There is no source code yet. This repository holds the plan, the designs and the decisions, so that developers can help shape and build the first version. **Our goal is a first test version in 2027.** We are looking for developers and sponsors; see [How to help](#how-to-help) and [Support LuxyOS](#support-luxyos).

## What LuxyOS is

| Promise | What it means |
| --- | --- |
| **Fast (on-demand)** | At boot only a small *broker* runs. Services and drivers start when an app asks for them and stop when nobody uses them. Closing a program really closes it. |
| **Windows programs** | `.exe` files install with a double click, via Wine and Proton. Honest compatibility labels show what works. |
| **Privacy** | No telemetry, no advertising ID, no ads. Nothing leaves the computer without the user's permission. |
| **Free and non-commercial** | LuxyOS is free for everyone: no paid editions, no ads, no data sales. Registration is optional; security updates are for everyone. |
| **Free store for developers** | Developers list their apps for free, with no commission. Paid apps are sold on the developer's own website. See [docs/terms.md](docs/terms.md). |
| **Choice** | The user picks browser, search engine and antivirus. Administrators decide whether AI is allowed, local only, or blocked. |
| **Business ready** | Active Directory, Remote Desktop (server and client), certificates, PowerShell, a winget-like package manager and remote management. |
| **Familiar** | A desktop layout that Windows users recognise, with its own look. Easy to use without a command line. |
| **Made for Europe** | Built in and for the EU. EU law (GDPR, Cyber Resilience Act, Accessibility Act, AI Act) is the baseline in every country. Anyone may use LuxyOS; partners must follow EU rules. See [docs/europe.md](docs/europe.md). |

## What it will look like

These designs show the end result we are building towards. Names, numbers and apps are examples. All screens: [docs/design/](docs/design/).

<p align="center"><img src="docs/design/01-desktop-start-menu.png" width="860" alt="LuxyOS desktop with the start menu open"></p>

<p align="center"><img src="docs/design/21-file-explorer.png" width="860" alt="LuxyOS Explorer with the familiar Windows layout: folders on the left, files with date, type and size, right-click menu"><br><sub>Explorer: the layout Windows users know, so they find their documents and pictures straight away</sub></p>

<table>
<tr>
<td width="50%"><img src="docs/design/06-store-windows-programs.png" alt="Store with Windows programs and compatibility labels"><br><sub>Store: Windows programs with honest compatibility labels</sub></td>
<td width="50%"><img src="docs/design/04-privacy-overview.png" alt="Privacy overview with per-app connections"><br><sub>Privacy overview: which app connected to what</sub></td>
</tr>
<tr>
<td><img src="docs/design/10-device-manager.png" alt="Device Manager"><br><sub>Device Manager: drivers in plain language</sub></td>
<td><img src="docs/design/11-sign-in-screen.png" alt="Sign-in screen with local users"><br><sub>Sign-in screen: local, Active Directory or Entra ID</sub></td>
</tr>
<tr>
<td><img src="docs/design/02-first-start-choices.png" alt="First start: choose browser, search engine and security"><br><sub>First start: the user chooses browser, search engine and antivirus</sub></td>
<td><img src="docs/design/16-remote-desktop-app.png" alt="Remote Desktop app"><br><sub>Built-in Remote Desktop app for Windows servers</sub></td>
</tr>
</table>

## Technical direction

LuxyOS is built on the **Linux kernel**, with its own on-demand **broker** (Rust), a desktop built with **Qt 6** on **Wayland**, and **Wine / DXVK / VKD3D-Proton** for Windows software. See [docs/architecture.md](docs/architecture.md) and the [decision records](docs/decisions/).

<p align="center"><img src="docs/design/diagram-architecture.png" width="640" alt="LuxyOS architecture: apps, Wine, broker, services, Linux kernel and hardware"></p>

## Documentation

| Document | Contents |
| --- | --- |
| [docs/vision.md](docs/vision.md) | Vision, target groups and launch rules |
| [docs/architecture.md](docs/architecture.md) | Layers, components and how on-demand works |
| [docs/requirements.md](docs/requirements.md) | What must work, per area and per target group |
| [docs/roadmap.md](docs/roadmap.md) | Phases and the first build steps |
| [docs/terms.md](docs/terms.md) | Terms: free and non-commercial, and the store terms for developers |
| [docs/europe.md](docs/europe.md) | Made for Europe: EU law as the baseline and what it means for LuxyOS |
| [docs/languages.md](docs/languages.md) | Languages, regions and translation |
| [docs/brand.md](docs/brand.md) | Logo, colours and animation |
| [website/](website/) | The website [luxyos.com](https://luxyos.com) in 11 languages, and how it is built |
| [docs/design/](docs/design/) | Screen designs (desktop, store, privacy, device manager, Remote Desktop and more) |
| [docs/decisions/](docs/decisions/) | Architecture decision records (ADRs) |
| [docs/good-first-tasks.md](docs/good-first-tasks.md) | Research and prototype tasks you can pick up now |
| [docs/nl/bouwnota.md](docs/nl/bouwnota.md) | The original, complete build note (Dutch) |

## How to help

Right now we need research, prototypes and review, not production code. Read [CONTRIBUTING.md](CONTRIBUTING.md) and pick a task from [issue #1: Start here](https://github.com/nijazo/luxyos/issues/1) or [docs/good-first-tasks.md](docs/good-first-tasks.md).

## Languages

The project language is **English**. LuxyOS itself starts with English (default), Dutch, Croatian, Bosnian, Serbian, Albanian, Macedonian, Turkish, German, French and Spanish, followed by all official EU languages. See [docs/languages.md](docs/languages.md).

## Support LuxyOS

LuxyOS is free and non-commercial. It is paid for by donations, grants and sponsors, never by users, ads or data.

<p><a href="https://paypal.me/nijazo"><strong>Donate to LuxyOS</strong></a> · via PayPal (paypal.me/nijazo)</p>

- Donations pay for servers, test hardware, development and legal advice (trademark, CRA, privacy).
- Donating is voluntary and gives no rights or influence over the product ([LEGAL.md](LEGAL.md)).
- We plan to publish a yearly overview of what comes in and what it is spent on.
- Sponsoring as a company or organisation? E-mail **sponsors@luxyos.com**.
- Donors are anonymous unless they ask to be on the supporters list on luxyos.com ([terms](docs/terms.md#supporters-list-optional)).

## Ownership

LuxyOS is a project founded and owned by **Nijaz Omanovic**. It is an own design: nothing is copied from other operating systems; it is built from what users say they want, so some familiar functions can resemble well-known systems. No rights can be derived from the plans and designs. See [LEGAL.md](LEGAL.md).

## Licence

| What | Licence |
| --- | --- |
| The operating system | [GPL-3.0-or-later](LICENSE) |
| The SDK for app developers | [Apache-2.0](LICENSE-APACHE) |
| Documentation and designs | [CC BY 4.0](LICENSE-CC-BY) |

The LuxyOS name and logo are trademarks ([TRADEMARKS.md](TRADEMARKS.md)). Details: [LICENSING.md](LICENSING.md).

---

<p align="center">Website: <a href="https://luxyos.com">luxyos.com</a> (11 languages)</p>
