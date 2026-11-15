# Good first tasks

There is no code yet. These tasks are research, prototypes and reviews that help the first version. Each task should end in a short write-up (a Markdown file in `docs/research/` or a comment on the issue) or a small prototype in a separate branch.

Each task already has an issue, linked below and grouped under [#1 Start here](https://github.com/nijazo/luxyos/issues/1). Comment on the issue before you start, so others know you are working on it. For a new idea, open an issue with the **Research task** template.

## Base system

| Issue | Task | Result |
| --- | --- | --- |
| [#2](https://github.com/nijazo/luxyos/issues/2) | Compare Buildroot and Yocto for a minimal LuxyOS image with glibc | Recommendation with build times and image sizes |
| [#3](https://github.com/nijazo/luxyos/issues/3) | Build a minimal bootable image in Docker and boot it in QEMU | Dockerfile and a script that boots it |
| [#4](https://github.com/nijazo/luxyos/issues/4) | Prototype the on-demand broker in Rust: socket activation for one service, stop after idle time | Small prototype and measurements |
| [#5](https://github.com/nijazo/luxyos/issues/5) | Run each app in its own cgroup and stop the whole group when the last window closes | Prototype on an existing Wayland compositor |
| [#6](https://github.com/nijazo/luxyos/issues/6) | Measure boot time to a login screen with only the broker, display and login running | Numbers and a profile |
| [#7](https://github.com/nijazo/luxyos/issues/7) | Investigate a systemd-compatible interface so RMM agents can install their units | Notes on what agents expect |

## Windows compatibility

| Issue | Task | Result |
| --- | --- | --- |
| [#8](https://github.com/nijazo/luxyos/issues/8) | List the 50 most used business programs and test them in current Wine | Table with labels: works, minor issues, does not work |
| [#9](https://github.com/nijazo/luxyos/issues/9) | Test NTSYNC with a set of Windows games and programs | Before/after measurements |
| [#10](https://github.com/nijazo/luxyos/issues/10) | Investigate Microsoft 365 desktop and Edge WebView2 under Wine | Status and blockers |
| [#11](https://github.com/nijazo/luxyos/issues/11) | Investigate the Adobe Creative Cloud installer under Wine | Status and needed Wine changes |

## Desktop and design

| Issue | Task | Result |
| --- | --- | --- |
| [#12](https://github.com/nijazo/luxyos/issues/12) | Review the screen designs in [design/](design/) for usability and accessibility | Comments per screen |
| [#13](https://github.com/nijazo/luxyos/issues/13) | Prototype the taskbar and start menu in Qt 6 / QML | Running prototype |
| [#14](https://github.com/nijazo/luxyos/issues/14) | Turn the brand colours and spacing into design tokens | Token file |

## Security, privacy and business

| Issue | Task | Result |
| --- | --- | --- |
| [#15](https://github.com/nijazo/luxyos/issues/15) | Prototype a per-app firewall with a connection overview | Prototype and notes |
| [#16](https://github.com/nijazo/luxyos/issues/16) | Test joining an Active Directory domain with realmd and SSSD on a minimal system | Step-by-step notes |
| [#17](https://github.com/nijazo/luxyos/issues/17) | Test certificate auto-enrolment from AD CS with Samba | Notes and limitations |
| [#18](https://github.com/nijazo/luxyos/issues/18) | Test the RDP server (KRdp or GNOME Remote Desktop) with the Windows Remote Desktop client | Feature table: clipboard, drives, printers, multi-monitor |

## Languages

| Issue | Task | Result |
| --- | --- | --- |
| [#19](https://github.com/nijazo/luxyos/issues/19) | Set up a Weblate project structure for LuxyOS | Proposal |
| [#20](https://github.com/nijazo/luxyos/issues/20) | Review terminology for one launch language | Glossary |
