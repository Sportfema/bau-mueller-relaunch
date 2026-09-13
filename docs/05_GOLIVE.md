# 05_GOLIVE.md – Umschalt-Checkliste & 301-Redirects

> **Projekt**: Relaunch bau-mueller.eu  
> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K., Colditz  
> **Status**: In Vorbereitung (Phase 2)  
> **Geplantes Go-Live-Zeitfenster**: Nächste Woche (abgestimmter Wartungszeitraum)

---

## 1. Tabelle der 301-Permanent-Weiterleitungen (Alt $ightarrow$ Neu)

Alle bestehenden Google-indizierten URLs und externen Verlinkungen werden lückenlos per 301 auf die neuen sprechenden deutschen Ziel-URLs umgeleitet:

| Alte URL | Neuer Slug / Ziel-URL | Status-Code | Begründung & Zielseite |
| :--- | :--- | :--- | :--- |
| `https://bau-mueller.eu/about/` | `https://bau-mueller.eu/ueber-uns/` | 301 | Sprechender deutscher Slug für Tradition & Team |
| `https://bau-mueller.eu/projects/` | `https://bau-mueller.eu/referenzen/` | 301 | Neuer Loop-Grid Hub für alle Bauprojekte |
| `https://bau-mueller.eu/contact/` | `https://bau-mueller.eu/kontakt/` | 301 | Deutsche Kontaktseite mit optimiertem Formular |
| `https://bau-mueller.eu/zimmerei-2/` | `https://bau-mueller.eu/` | 301 | Bereinigung des alten Startseiten-Permalinks |
| `https://bau-mueller.eu/waerme-mit-stil-unsere-pellets-fuer-ihren-kamine/` | `https://bau-mueller.eu/leistungen/pellets-holzbriketts/` | 301 | Überführung des Pellet-Artikels in Hauptleistung |
| `https://bau-mueller.eu/binderdachstuhl/` | `https://bau-mueller.eu/leistungen/zimmerei-holzbau/` | 301 | Dünnen Alt-Beitrag (196 Wörter) auf Leistungsseite leiten |
| `https://bau-mueller.eu/lohnschnitt-im-neuen-saegewerk/` | `https://bau-mueller.eu/leistungen/zimmerei-holzbau/` | 301 | Kurzmeldung (73 Wörter) auf Sägewerk-Abschnitt leiten |
| `https://bau-mueller.eu/waermedaemmung-fuer-meine-fassade/` | `https://bau-mueller.eu/leistungen/altbausanierung-denkmalpflege/` | 301 | Dünnen Alt-Beitrag auf Sanierungsseite leiten |

*(Wichtige Blogartikel mit Substanz wie „Werkstatt der Zukunft“ und „Denkmalgerechte Altbausanierung“ bleiben erhalten und werden im neuen Single-Template gerendert).*

---

## 2. Go-Live Checkliste (Sequenzieller Ablauf)

- [ ] **Schritt 1: Backup-Prüfung**
  - All-Inkl / KAS Server-Backup verifizieren.
  - Datenbank-Dump via phpMyAdmin / Script exportieren.
  - Elementor-Export aller neuen Templates als JSON in `exports/` sichern.
- [ ] **Schritt 2: Wartungsmodus aktivieren** (optional, ca. 15–30 Min.)
- [ ] **Schritt 3: Elementor Site Settings umstellen**
  - Globale Farben, Fonts und Layout-Vorgaben aus dem freigegebenen Designsystem aktivieren.
- [ ] **Schritt 4: Astra-Customizer Anpassung**
  - Header & Footer auf Theme Builder übergeben.
- [ ] **Schritt 5: Theme-Builder-Bedingungen scharf schalten**
  - `NEU - Header` $ightarrow$ Gesamte Website.
  - `NEU - Footer` $ightarrow$ Gesamte Website.
  - `NEU - Single Beitrag` $ightarrow$ Alle Beiträge.
  - `NEU - Single Referenz` $ightarrow$ Alle Referenzen.
  - `NEU - 404` $ightarrow$ 404-Seite.
- [ ] **Schritt 6: Seiten-Status umschalten**
  - Alte Seiten (IDs 540, 541, 542, 7, 543) auf `draft` setzen (30 Tage Archiv).
  - Neue Seiten: Präfix `NEU - ` entfernen, Slugs final setzen, Status auf `publish`.
  - Startseite in WordPress *Einstellungen $ightarrow$ Lesen* auf die neue Startseite umstellen.
- [ ] **Schritt 7: Hauptmenü umstellen**
  - Menü ID 9 auf die neuen Seitenpfade aktualisieren.
- [ ] **Schritt 8: 301-Redirects einpflegen**
  - In `.htaccess` oder Yoast SEO Redirects eintragen und prüfen.
- [ ] **Schritt 9: Cache & CSS regenerieren**
  - Elementor CSS regenerieren (*Elementor $ightarrow$ Werkzeuge $ightarrow$ Dateien neu generieren*).
- [ ] **Schritt 10: Formular-Live-Test**
  - Testanfrage absenden, E-Mail-Eingang bei `info@bau-mueller.eu` und `thomas@q26.it` prüfen.
- [ ] **Schritt 11: Plugin-Bereinigung**
  - ElementsKit Lite/Pro, Essential Addons und Ultimate Addons deaktivieren und nach 7 Tagen löschen.
- [ ] **Schritt 12: Search Console & Sitemap**
  - XML-Sitemap `/sitemap_index.xml` in Google Search Console neu einreichen.
