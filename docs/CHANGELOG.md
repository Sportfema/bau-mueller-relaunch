# CHANGELOG.md – Protokoll aller Schreiboperationen

> **Projekt**: Relaunch bau-mueller.eu  
> **Agentur**: Digitalagentur q26.it (Thomas Wasner)  
> **Regel**: Jede Schreiboperation auf der WordPress-Installation oder im Dateisystem wird hier lückenlos mit Zeitstempel, Objekt-ID, Titel und Aktion dokumentiert.

---

| Zeitstempel (UTC) | Phase | Objekt-ID | Typ / Titel | Ausgeführte Aktion |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-13 10:40 | Setup | Lokal | Verzeichnisstruktur | Projektordner `bau-mueller-relaunch/` mit Unterordnern `docs/`, `exports/`, `assets/` angelegt. |
| 2026-09-13 10:41 | Setup | Lokal | `PROMPT.md` | Projektauftrag und Briefing-Regeln lokal abgelegt. |
| 2026-09-13 10:43 | Phase 1 (3.0) | Lokal | `01_AUDIT.md` | Bestandsaufnahme & Inventar 3.0 dokumentiert (Read-only Lauf). |
| 2026-09-13 10:45 | Phase 1 (3.0) | Lokal | `CHANGELOG.md`, `OFFENE_FRAGEN.md` | Initiale Tracking-Dokumente angelegt. |
| 2026-09-13 10:57 | Phase 1 (3.2) | Lokal | `assets/bilder_inventar.csv` | Vollständiges Bild-Inventar für alle 141 Medien generiert. |
| 2026-09-13 10:58 | Phase 1 (3.1-3.4) | Lokal | `01_AUDIT.md` | Vollständigen Auditbericht (Technik, Inhalt, UX, Heuristik, Top-10) fertiggestellt. |

| 2026-09-13 11:00 | Phase 2 | Lokal | `05_GOLIVE.md` | Go-Live-Checkliste und 301-Redirect-Mapping-Tabelle initialisiert. |
| 2026-09-13 11:01 | Phase 2 | Lokal | `02_KONZEPT.md` | Vollständiges Relaunch-Konzept (Sitemap, 3 Stilrichtungen, Design-Tokens, Komponenten) fertiggestellt. |
| 2026-09-13 11:02 | Phase 2 | Lokal | `docs/03_INHALTE/` | Alle 14 Textentwürfe (Seiten, Hubs, Einzelseiten, Rechtliches) komplett ausgearbeitet. |
| 2026-09-13 11:03 | Phase 3 | Server/KAS | Hoster-Backup | Backup-Check durchgeführt: All-Inkl KAS Hoster-Backup aktiv (Dateien + DB). |
| 2026-09-13 11:05 | Phase 3 | Kit/Globals | 16 CSS Tokens | Global CSS Variables (Farben, Schriften, Radien) im aktiven Kit angelegt. |
| 2026-09-13 11:06 | Phase 3 | Kit/Classes | 5 Global Classes | Globale CSS-Klassen (`glass-card`, `solid-card`, `btn-primary`, `btn-secondary`, `badge-pill`) angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2589 | Theme Builder Header | Entwurf `NEU – Header` ohne Bedingungen angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2590 | Theme Builder Footer | Entwurf `NEU – Footer` ohne Bedingungen angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2591 | Theme Builder Single Post | Entwurf `NEU – Beitrag` ohne Bedingungen angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2592 | Theme Builder Single Ref | Entwurf `NEU – Referenz` ohne Bedingungen angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2593 | Theme Builder 404 | Entwurf `NEU – 404` ohne Bedingungen angelegt. |
| 2026-09-13 11:07 | Phase 3 | 2594 | Theme Builder Loop Item | Entwurf `NEU – Loop Item Referenz` angelegt. |
| 2026-09-13 11:08 | Phase 3 | 2589 | Theme Builder Header | Header-Komposition (`NEU – Header`) erstellt und gespeichert. |
| 2026-09-13 11:08 | Phase 3 | 2590 | Theme Builder Footer | 4-spaltiger Footer (`NEU – Footer`) erstellt und gespeichert. |
| 2026-09-13 11:09 | Phase 3 | exports/ | Templates JSON | `exports/neu-header-2589.json` und `exports/neu-footer-2590.json` gesichert. |
| 2026-09-13 11:10 | Phase 3 | 2595 | Seite: NEU – Startseite | Neuer Seiten-Entwurf angelegt (Elementor Header/Footer Template, hide_title: yes). |
| 2026-09-13 11:11 | Phase 3 | 2595 | Seite: NEU – Startseite | Vollständige V4-Container-Komposition (8 Sektionen, Apple Design, Glass-Cards) aufgebaut & gespeichert. |
| 2026-09-13 11:12 | Phase 3 | 2595 | Seite: NEU – Startseite | Vorschau-Token erzeugt, Desktop- und Mobil-Screenshots in `docs/screenshots/nachher/` abgelegt. |
| 2026-09-13 11:13 | Phase 3 | exports/ | Startseite JSON | `exports/neu-startseite-2595.json` gesichert. |
| 2026-09-13 16:45 | Phase 3 | GitHub | Repo `bau-mueller-relaunch` | Lokales Repository initialisiert und erfolgreich nach `Sportfema/bau-mueller-relaunch` gepusht. |

*(Hinweis: Bisher keine zerstörenden Operationen auf Live; alle neuen Inhalte werden als Entwürfe mit Präfix `NEU – ` angelegt.)*
| 2026-09-14 13:19 | Phase 2/3 | Designsystem | `docs/02_DESIGN_SOMERVILLE.md` | Somerville Architectural Craft Designsystem spezifiziert, KI-Bilder entfernt, 100% echte Fotos (Tor mit Ken-Burns-Zoom, Sägewerk, Werkstatt) freigegeben. |
