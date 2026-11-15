# Languages and regions

The project language is **English**. LuxyOS defaults to English and supports European languages. Each user can choose their own language; language and region are set separately (for example English menus with Dutch date format and euro).

## Launch languages

| Language | Script | Keyboard |
| --- | --- | --- |
| English (default) | Latin | QWERTY (US and UK) |
| Dutch | Latin | QWERTY (US international), Belgian AZERTY |
| Croatian | Latin (č, ć, đ, š, ž) | Croatian QWERTZ |
| Bosnian | Latin, also Cyrillic | Bosnian QWERTZ |
| Serbian | Cyrillic and Latin | Serbian Cyrillic and Serbian Latin (QWERTZ) |
| Albanian | Latin (ë, ç) | Albanian QWERTZ |
| Macedonian | Cyrillic (ѓ, ќ, ѕ, љ, њ, џ) | Macedonian Cyrillic |
| Turkish | Latin (ç, ğ, ı, İ, ö, ş, ü) | Turkish Q and Turkish F |
| German | Latin (ä, ö, ü, ß) | German QWERTZ |
| French | Latin | French AZERTY |
| Spanish | Latin (ñ) | Spanish QWERTY |

Then all 24 official EU languages, and later other European languages such as Montenegrin, Norwegian and Ukrainian.

## Technical requirements

- Language packs on demand: only chosen languages are downloaded.
- Switch language without reinstalling, per user.
- Fonts covering Latin with diacritics, Cyrillic and Greek.
- Spell checking per language (Hunspell) and correct keyboard layouts.
- Windows programs via Wine get the same language and region settings.
- Turkish dotted and dotless i (ı/I, i/İ): case conversion and search must be locale-aware.
- Qt translation files and ICU for dates, times, numbers and currency.

## Translation process

- **Weblate** (open source) as translation platform, with community volunteers.
- Professional translators for launch languages and for legal texts (privacy policy, terms).
- Every language is reviewed by a native speaker before it ships.
- Everything is translated: installer, settings, store, error messages, help and the website (luxyos.com, English default).
