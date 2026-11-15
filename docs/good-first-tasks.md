# Good first tasks

There is no code yet. These tasks are research, prototypes and reviews that help the first version. Each task should end in a short write-up (a Markdown file in `docs/research/` or a comment on the issue) or a small prototype in a separate branch.

Open an issue with the **Research task** template before you start, so others know you are working on it.

## Base system

| Task | Result |
| --- | --- |
| Compare Buildroot and Yocto for a minimal LuxyOS image with glibc | Recommendation with build times and image sizes |
| Build a minimal bootable image in Docker and boot it in QEMU | Dockerfile and a script that boots it |
| Prototype the on-demand broker in Rust: socket activation for one service, stop after idle time | Small prototype and measurements |
| Run each app in its own cgroup and stop the whole group when the last window closes | Prototype on an existing Wayland compositor |
| Measure boot time to a login screen with only the broker, display and login running | Numbers and a profile |
| Investigate a systemd-compatible interface so RMM agents can install their units | Notes on what agents expect |

## Windows compatibility

| Task | Result |
| --- | --- |
| List the 50 most used business programs and test them in current Wine | Table with labels: works, minor issues, does not work |
| Test NTSYNC with a set of Windows games and programs | Before/after measurements |
| Investigate Microsoft 365 desktop and Edge WebView2 under Wine | Status and blockers |
| Investigate the Adobe Creative Cloud installer under Wine | Status and needed Wine changes |

## Desktop and design

| Task | Result |
| --- | --- |
| Review the screen designs in [design/](design/) for usability and accessibility | Comments per screen |
| Prototype the taskbar and start menu in Qt 6 / QML | Running prototype |
| Turn the brand colours and spacing into design tokens | Token file |

## Security, privacy and business

| Task | Result |
| --- | --- |
| Prototype a per-app firewall with a connection overview | Prototype and notes |
| Test joining an Active Directory domain with realmd and SSSD on a minimal system | Step-by-step notes |
| Test certificate auto-enrolment from AD CS with Samba | Notes and limitations |
| Test the RDP server (KRdp or GNOME Remote Desktop) with the Windows Remote Desktop client | Feature table: clipboard, drives, printers, multi-monitor |

## Languages

| Task | Result |
| --- | --- |
| Set up a Weblate project structure for LuxyOS | Proposal |
| Review terminology for one launch language | Glossary |
