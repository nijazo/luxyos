# Website (luxyos.com)

The "Coming soon" page for luxyos.com in the 11 launch languages. English is the default.

Edit texts in `src/build.py`, then run `python3 website/src/build.py`. Translations other than English and Dutch need a review by a native speaker.

| File | URL |
| --- | --- |
| [index.html](index.html) | https://luxyos.com/ (English, default) |
| `<code>/index.html` | https://luxyos.com/&lt;code&gt;/ for nl, de, fr, es, hr, bs, sr, sq, mk, tr |
| [img/](img/) | Design previews (WebP, 720 and 1440 px). Dutch pages use the `-nl` images, all other languages the `-en` images |
| [src/build.py](src/build.py) | Generates all pages from one template and the texts per language |
| [src/supporters.json](src/supporters.json) | Format of the optional supporters list. Stays empty here; the real list is `src/supporters.private.json`, which is git-ignored |

- Self-contained: no external fonts, scripts, trackers or cookies. Keep it that way; the footer promises it.
- The donate button is a plain link to PayPal (paypal.me/nijazo), with no PayPal script.
- Images are served from luxyos.com itself, so the page still loads nothing from other websites. `SHA256SUMS` lists every file for checking after upload.
- Supporters list: hidden until `CONTACT` (the e-mail address for removal requests) is set in `src/build.py`. Donors opt in themselves; see [docs/terms.md](../docs/terms.md).
- GitHub is linked in the top bar, the developers block and the footer.
- Redirects: luxyos.nl → https://luxyos.com/nl/ and luxyos.eu → https://luxyos.com/.

Licence: CC BY 4.0, except the LuxyOS name and logo ([TRADEMARKS.md](../TRADEMARKS.md)).
