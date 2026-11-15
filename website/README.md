# Website (luxyos.com)

The "Coming soon" page for luxyos.com in the 11 launch languages. English is the default.

Edit texts in `src/build.py`, then run `python3 website/src/build.py`. Translations other than English and Dutch need a review by a native speaker.

| File | URL |
| --- | --- |
| [index.html](index.html) | https://luxyos.com/ (English, default) |
| `<code>/index.html` | https://luxyos.com/&lt;code&gt;/ for nl, de, fr, es, hr, bs, sr, sq, mk, tr |
| [img/](img/) | Design previews (WebP, 720 and 1440 px). Dutch pages use the `-nl` images, all other languages the `-en` images |
| [src/build.py](src/build.py) | Generates all pages from one template and the texts per language |
| [src/supporters.json](src/supporters.json) | Format and rules of the optional supporters list (anonymous count, sponsors with logo, supporters). Stays empty here; the real list lives on the server |
| [src/logo.py](src/logo.py) | Turns a sponsor logo into a small WebP (max 320 × 128, shown at 160 × 64). Logos go in `img/sponsors/` in the webroot, never in Git |

- Self-contained: no external fonts, scripts, trackers or cookies. Keep it that way; the footer promises it.
- The donate button is a plain link to PayPal (paypal.me/nijazo), with no PayPal script.
- Images are served from luxyos.com itself, so the page still loads nothing from other websites. `SHA256SUMS` lists every file for checking after upload.
- Supporters list: shown on every page; removal requests go to `CONTACT` (sponsors@luxyos.com) in `src/build.py`. Donors opt in themselves; see [docs/terms.md](../docs/terms.md).
- GitHub is linked in the top bar, the developers block and the footer.
- Redirects: luxyos.nl → https://luxyos.com/nl/ and luxyos.eu → https://luxyos.com/.

Licence: CC BY 4.0, except the LuxyOS name and logo ([TRADEMARKS.md](../TRADEMARKS.md)).

## Live site with the supporters list (server)

The real supporters list never goes into Git. On the server it is kept outside the webroot, and the pages are built there:

```sh
# one time: a private folder outside the webroot
/var/www/vhosts/quracom13/private/supporters.private.json   # {"supporters": []}
/var/www/vhosts/quracom13/private/luxyos-build/build.py     # copy of website/src/build.py

# every update
python3 /var/www/vhosts/quracom13/private/luxyos-build/build.py \
  --out <webroot of luxyos.com> \
  --supporters /var/www/vhosts/quracom13/private/supporters.private.json
```

- Add a donor only after the payment succeeded and only as they asked in the PayPal note (see `src/supporters.json`); remove them when they ask (sponsors@luxyos.com). Then run the build again.
- Logos: `python3 logo.py <file> <name>.webp`, put the result in `<webroot>/img/sponsors/`, and set `until` to 12 months after the payment. The build stops if a logo file is missing or a name is not a plain `.webp` file name; expired logos disappear automatically, the name stays.
- Website updates from this repository: copy `img/` and the new `src/build.py` to the server and run the build there. **Do not copy the `index.html` files from Git over the live site**: they have an empty supporters list and would remove the names.
