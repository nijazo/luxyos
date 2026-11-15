# Requirements

What LuxyOS must do, per area. Designs for many of these screens are in [design/](design/). The complete Dutch build note with all details is in [nl/bouwnota.md](nl/bouwnota.md).

## Desktop and usability

- Familiar layout: taskbar, Start button, two-column start menu, Explorer, system tray. Own look, not a copy of Windows.
- No command line needed for normal use. Installation in at most 5 steps.
- One settings app; advanced options behind "Advanced".
- Familiar shortcuts: Win+E, Win+L, Win+D, Win+V, Win+Shift+S, Ctrl+Shift+Esc.
- Snipping tool, clipboard history, emoji panel, window snapping, virtual desktops, notification centre.

## Windows compatibility

- `.exe` and `.msi` install with a double click. The user never sees Wine.
- Windows components (.NET, Visual C++ runtimes, DirectX) install only when a program needs them.
- Compatibility labels: *Works perfectly*, *Minor issues*, *Does not work*, *Not tested yet*.
- Gaming: Proton, controllers, shader pre-caching, NTSYNC. Games with kernel anti-cheat: one click to Windows (dual boot) or cloud gaming.

## Migration from Windows

A Windows `.exe` "migration assistant": check report → collect data → full Windows image backup → install → reinstall programs → restore settings and licences → user continues where they left off. Always a way back for 30 days.

## Privacy and security

- Nothing leaves the system without permission. Everything that sends data is off by default.
- Privacy overview: which program connected to what, with per-app internet switches.
- Sandbox per app; permissions from the app manifest.
- AI setting for administrators: **blocked**, **local only** or **allowed** (OS features, store, app execution, network blocklist, NPU).
- Disk encryption on by default (LUKS2 + TPM). Reset: keep files or remove everything (crypto-erase).
- Central certificate management, like Windows (personal, trusted roots, intermediates, publishers, untrusted, machine).

## Users and sign-in

- Account types: Administrator, Standard, Child, Guest. Groups, including custom groups and AD groups.
- Sign-in: local account (password, PIN, fingerprint, security key), Active Directory, Entra ID.
- Users manage their own profile: photo, name, password, linked mail, calendar, contacts and files (Gmail, Outlook/Microsoft 365, Yahoo, IMAP).

## System management

- Device Manager: status per device in plain language, install, update and roll back drivers, firmware updates.
- Network: IPv4/IPv6, DHCP or static, DNS (also encrypted DNS), VPN, profiles, per-app firewall, SMB sharing.
- Disk Management: create, extend, shrink partitions; format FAT32, exFAT, NTFS, ext4, Btrfs; drive letters for Windows programs; SMART warnings.
- Battery: automatic power profiles, only open apps get energy, per-app battery usage, 80 % charge limit.
- Phone link over Wi-Fi, Bluetooth and USB (KDE Connect based), Android and iPhone.

## Business

- Active Directory, Group Policy (partial), certificate auto-enrolment.
- Remote management agents (RMM) can be installed and run always-on with admin approval.
- PowerShell 7 and a winget-like package manager (`app install`, `app upgrade --all`, `app export/import`).
- Runs as a VM (ESXi, Hyper-V, Proxmox) and as a multi-user Remote Desktop server, without per-user licences.
- Built-in Remote Desktop client with the familiar layout (Computer, Username; tabs General, Display, Local Resources, Experience, Advanced), `.rdp` files, RD Gateway, RemoteApp.

## Store

- One store for Windows apps, Linux apps and open-source apps from GitHub (imported automatically when the licence allows it).
- Labels: *Verified* or *From GitHub*. Permissions from the manifest are shown before installation.
- Developer mode, SDK, emulator, manifest per app.

## Europe and law

- EU law is the minimum standard in every country; one version for everyone ([europe.md](europe.md), [decision 0009](decisions/0009-eu-law-as-baseline.md)).
- GDPR and ePrivacy: privacy by design and by default, data export and deletion, consent before anything is sent.
- Cyber Resilience Act: secure by default, SBOM per release, vulnerability handling and reporting, security updates for the stated support period, CE marking.
- European Accessibility Act: screen reader, keyboard-only use, high contrast, scalable text in every screen.
- AI Act: AI use is always labelled; administrators can block AI.
- Digital Services Act for the store: traceable sellers, reporting of illegal apps, reasons for removals.
- Online services (updates, store, registration, backup) run in the EU.

## Updates and business model

- Free; registration optional. Security updates for everyone.
- Atomic A/B updates with one-click rollback; Stable and Beta channels; LTS edition for business and government.
- Income: business subscriptions, store commission, search engine partners.
