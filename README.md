# Relaunch bau-mueller.eu – Zimmerei & Baugeschäft Arthur Müller e.K.

> **Digitalagentur**: [q26.it](https://q26.it) – Thomas Wasner, Colditz  
> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K., Geithainer Str. 32, 04680 Colditz  
> **Inhaber**: Dipl.-Ing. Tobias Müller (Meisterbetrieb seit 1920, 4. Generation)  
> **Live-Website**: [https://bau-mueller.eu](https://bau-mueller.eu)

---

## 📌 Projektübersicht & Auftrag

Relaunch des Webauftritts der traditionsreichen Zimmerei und des Baugeschäfts Arthur Müller e.K. aus Colditz. Das Projekt umfasst eine ganzheitliche Neugestaltung auf technischer, inhaltlicher und optischer Ebene unter Berücksichtigung moderner Web-Standards, lokaler SEO (Colditz, Grimma, Leipziger Land, Sachsen) sowie höchster Gestaltungsqualität nach Apple-Design-Prinzipien (Fluid Typography, Liquid-Glass, 8px-Spacing, taktile Micro-Interactions).

### Technischer Stack
* **CMS**: WordPress 6.x (Astra Theme)
* **Page Builder**: Elementor & Elementor Pro (V4 Container Architecture)
* **Styling**: Native CSS-Tokens & Global Classes (Zero Third-Party Dependency)
* **Recht & DSGVO**: Real Cookie Banner, lokale Schriften (Plus Jakarta Sans & Inter), rechtskonformes Impressum & Datenschutz
* **Förderung**: Pflicht-Sektion EU-/Freistaat Sachsen (EFRE / SAB / GRW-Infra)

---

## 🚀 5-Phasen-Relaunch-Modell

1. **Phase 1: Audit & Bestandsaufnahme** (Abgeschlossen)
   * Vollständiger technischer, inhaltlicher und UX-Audit (Nielsen Heuristiken).
   * Bildinventar aller 141 Medien der Mediathek inkl. Dimensionen und Re-Use-Empfehlungen.
2. **Phase 2: Konzept & Designsystem** (Abgeschlossen & Freigegeben)
   * Neue Informationsarchitektur & schlanke Sitemap.
   * 3 ausgearbeitete Design-Stilrichtungen (Auswahl: Stil 1 „Meisterhandwerk & Zeitgeist“).
   * 1:1 Elementor Design-Tokens & 12 Kernkomponenten.
   * 14 vollständige SEO-Textentwürfe in `docs/03_INHALTE/`.
3. **Phase 3: Umsetzung via Elementor MCP** (Aktuell in Arbeit)
   * Globale CSS-Variablen & Utility-Klassen im aktiven Elementor-Kit registriert.
   * Theme Builder Templates: `NEU – Header` (ID: 2589) & `NEU – Footer` (ID: 2590) ohne Bedingungen.
   * Seitenentwurf: `NEU – Startseite` (ID: 2595) in reiner Container-Architektur mit 8 Sektionen.
   * JSON-Exports in `exports/`.
4. **Phase 4: Qualitätssicherung** (Bevorstehend)
   * Lighthouse Mobile >= 90 / >= 95 A11y, Best Practices, SEO.
   * Responsive Prüfung (360px bis 1440px).
   * Redaktionsanleitung `docs/REDAKTION.md`.
5. **Phase 5: Go-Live** (Bevorstehend)
   * 301-Redirects, Theme-Builder-Zuweisungen, Page-Swapping, Plugin-Konsolidierung.

---

## 📂 Verzeichnisstruktur

```text
├── assets/
│   └── bilder_inventar.csv          # Inventar aller 141 Medien der WordPress-Mediathek
├── docs/
│   ├── 01_AUDIT.md                  # Vollständiger Bestandsaudit (Technik, UX, SEO)
│   ├── 02_KONZEPT.md                # Relaunch-Konzept, Sitemap, Stilrichtungen, Tokens
│   ├── 03_INHALTE/                  # 14 vollständige redaktionelle Textvorlagen
│   │   ├── 01_startseite.md
│   │   ├── 02_leistungen_uebersicht.md
│   │   ├── 03_leistung_zimmerei_holzbau.md
│   │   ├── 04_leistung_treppen_moebelbau.md
│   │   ├── 05_leistung_maurer_betonarbeiten.md
│   │   ├── 06_leistung_altbausanierung_denkmalpflege.md
│   │   ├── 07_leistung_pellets_holzbriketts.md
│   │   ├── 08_referenzen.md
│   │   ├── 09_ueber_uns.md
│   │   ├── 10_aktuelles.md
│   │   ├── 11_kontakt.md
│   │   ├── 12_404.md
│   │   ├── 13_impressum.md
│   │   └── 14_datenschutz.md
│   ├── 05_GOLIVE.md                 # Go-Live-Checkliste & 301-Redirect-Mapping-Tabelle
│   ├── CHANGELOG.md                 # Lückenloses Protokoll aller Schreiboperationen
│   ├── OFFENE_FRAGEN.md             # Klärungspunkte für Kunde & Agentur
│   └── screenshots/
│       └── nachher/                 # Desktop- und Mobil-Screenshots der neuen Entwürfe
├── exports/                         # Gesicherte Elementor-JSON-Dateien
│   ├── neu-header-2589.json
│   ├── neu-footer-2590.json
│   └── neu-startseite-2595.json
├── content_audit.json               # Rohdaten-Audit der alten Seiten
├── inventory_raw.json               # Mediathek-Rohdaten
├── widget_and_media_analysis.json   # Widget- und Addon-Nutzungsanalyse
├── PROMPT.md                        # Projektauftrag und Arbeitsregeln
└── README.md                        # Diese Dokumentation
```

---

## 🛡️ Sicherheit & Arbeitsweise

* **Zero-Destructive-Policy**: Es werden keine Änderungen an bestehenden, veröffentlichten Seiten vorgenommen. Alle Arbeiten erfolgen parallel als Entwurf (`NEU – ...`).
* **Freigabe-Stopps**: Jede Phase und jeder Hauptmeilenstein erfordert eine explizite Kunden-/Agenturfreigabe.
* **Protokollierung**: Sämtliche Änderungen auf Server und Installation sind minutengenau in `docs/CHANGELOG.md` dokumentiert.
