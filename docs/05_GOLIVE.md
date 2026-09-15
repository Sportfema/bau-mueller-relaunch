# 05_GOLIVE.md – Go-Live Bericht & Live-Architektur

> **Projekt**: Relaunch bau-mueller.eu  
> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K., Colditz  
> **Status**: **100 % ERFOLGREICH LIVE GESCHALTET (PHASE 5 ABGESCHLOSSEN)**  
> **Go-Live-Zeitpunkt**: 15.09.2026, 08:03 Uhr  
> **Rollback-Garantie**: Aktiv & verifiziert ([`scripts/rollback_live.py`](file:///C:/Users/THOMASPC/.gemini/antigravity/scratch/bau-mueller-relaunch/scripts/rollback_live.py))

---

## 1. Übersicht der aktiven Live-Seiten (Somerville Architectural Craft)

Alle Seiten sind unter ihren kanonischen Produktions-URLs live erreichbar und wurden per HTTP 200 verifiziert:

| Seite | Live-URL | Status-Code | Design-System | Besonderheiten |
| :--- | :--- | :---: | :--- | :--- |
| **Startseite** | [`https://bau-mueller.eu/`](https://bau-mueller.eu/) | **200 OK** | Somerville Canvas | Tor-Hero, 3 Kernleistungen, Werkstatt-Slab, Pelletkreislauf, Magazin-Ticker, SAB-Footer & Voting-Popup |
| **Leistungen** | [`https://bau-mueller.eu/leistungen/`](https://bau-mueller.eu/leistungen/) | **200 OK** | Somerville Canvas | 5 Disziplinen, Gewerke-Verbund, Master-Footer mit SAB & Voting-Popup |
| **Referenzen** | [`https://bau-mueller.eu/projects/`](https://bau-mueller.eu/projects/) | **200 OK** | Somerville Canvas | Galerie-Grid mit echten Fotos, Wangentreppe, Kirchturm, SAB-Footer & Voting-Popup |
| **Über uns** | [`https://bau-mueller.eu/about/`](https://bau-mueller.eu/about/) | **200 OK** | Somerville Canvas | 100+ Jahre Chronik, Foto uberunssw.jpg, SAB-Footer & Voting-Popup |
| **Zimmerei & Holzbau** | [`https://bau-mueller.eu/zimmerei-holzbau/`](https://bau-mueller.eu/zimmerei-holzbau/) | **200 OK** | Somerville Canvas | Einzelleistung Dachstühle, Abbundtechnik, Sägewerk-Vorteil & FAQ |
| **Aktuelles & Magazin**| [`https://bau-mueller.eu/aktuelles/`](https://bau-mueller.eu/aktuelles/) | **200 OK** | Somerville Canvas | Filter-Pills, 6 reale Fachartikel, SAB-Highlight & Werkstatt-Meldungen |
| **SAB-Förderartikel**  | [`/werkstatt-der-zukunft-.../`](https://bau-mueller.eu/werkstatt-der-zukunft-praezision-trifft-tradition/) | **200 OK** | WordPress Post | Offizieller Fördermittelbeitrag (EU EFRE & Freistaat Sachsen) |
| **Impressum**          | [`https://bau-mueller.eu/impressum/`](https://bau-mueller.eu/impressum/) | **200 OK** | WordPress Page | Rechtssichere Anbieterkennzeichnung Arthur Müller e.K. |
| **Datenschutz**        | [`https://bau-mueller.eu/datenschutz/`](https://bau-mueller.eu/datenschutz/) | **200 OK** | WordPress Page | DSGVO-konforme Datenschutzerklärung |

---

## 2. Zero-Destructive Archiv & Rollback-Infrastruktur

Keine einzige ursprüngliche Seite wurde überschrieben oder gelöscht. Alle 6 alten Seiten wurden zur lückenlosen Historienwahrung auf `draft` gesetzt und mit dem Präfix `[ARCHIV 2026]` versehen:
- ID 540: `[ARCHIV 2026] Startseite (Original)` (Slug: `startseite-archiv-2026`)
- ID 541: `[ARCHIV 2026] Über uns (Original)` (Slug: `about-archiv-2026`)
- ID 542: `[ARCHIV 2026] Leistungen (Original)` (Slug: `leistungen-archiv-2026`)
- ID 7: `[ARCHIV 2026] Referenzen (Original)` (Slug: `projects-archiv-2026`)
- ID 543: `[ARCHIV 2026] Kontakt (Original)` (Slug: `contact-archiv-2026`)
- ID 2012: `[ARCHIV 2026] Aktuelles (Original)` (Slug: `aktuelles-archiv-2026`)

**Rollback-Verfahren**:
1. **Per Skript**: `python scripts/rollback_live.py` ausführen. Stellt alle Originalseiten binnen 5 Sekunden wieder auf `publish` und setzt die Homepage zurück auf ID 540.
2. **Per WordPress-Dashboard**: *Einstellungen → Lesen → Homepage* wieder auf die alte Startseite (ID 540) stellen.
