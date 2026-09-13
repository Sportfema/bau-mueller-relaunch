# 02_KONZEPT.md – Phase 2: Informationsarchitektur & Designsystem

> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K., Colditz  
> **Agentur**: Digitalagentur q26.it (Thomas Wasner, Colditz)  
> **Stand**: Phase 2 (Konzept & Designsystem)  
> **Status**: Zur Freigabe und Stilwahl vorgelegt

---

## 4.1 Informationsarchitektur & Neue Sitemap

Ausgehend von den Schwachstellen des Audits (fehlende Detailseiten, vergrabene Pellets, 0 CPTs für Referenzen) gliedert sich die neue Seitenarchitektur in einen kunden- und SEO-zentrierten Aufbau:

```
Startseite (/)
│
├── Leistungen (/leistungen/)  [Hub-Seite]
│   ├── Zimmerei & Holzbau (/leistungen/zimmerei-holzbau/)
│   ├── Treppen- & Möbelbau (/leistungen/treppen-moebelbau/)
│   ├── Maurer- & Betonarbeiten (/leistungen/maurer-betonarbeiten/)
│   ├── Altbausanierung & Denkmalpflege (/leistungen/altbausanierung-denkmalpflege/)
│   └── Pellets & Holzbriketts (/leistungen/pellets-holzbriketts/)
│
├── Referenzen (/referenzen/)  [Loop-Grid mit Filter nach Gewerk]
│   └── Einzelprojekt [Theme Builder Single-Template für CPT referenzen]
│
├── Über uns (/ueber-uns/)  [Tradition seit 1920, 4. Generation, Dipl.-Ing., Werkstatt]
│
├── Aktuelles (/aktuelles/)  [Loop-Grid aus Blogbeiträgen]
│   └── Einzelbeitrag [Theme Builder Single-Template für Beiträge]
│
├── Kontakt & Beratung (/kontakt/)  [Qualifiziertes Formular, Telefon, Karte mit Consent]
│
├── 404-Seite (/404/)  [Hilfe- und Leitsystem im Theme Builder]
│
└── Rechtliches: Impressum (/impressum/) · Datenschutz (/datenschutz/)
```

### Seiten-Steckbriefe (Zweck, Keywords, Sektionen, CTAs)

| Seite | Primäres Keyword | H1-Überschrift | Sektionen-Aufbau | Primärer CTA | Benötigte Medien |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Startseite** | Zimmerei Colditz | Meisterhafte Holzarbeit & Massivbau seit 1920 in Colditz | 1. Hero mit Werten & Schnellkontakt<br>2. Trust-Leiste (Meister, Dipl.-Ing., 4. Gen.)<br>3. 5 Leistungs-Cards mit Liquid Glass<br>4. Über-uns-Teaser & Inhaber-Zitat<br>5. Ausgewählte Referenzen (Loop)<br>6. Ablauf in 4 Schritten<br>7. Förderhinweis (SAB/EU)<br>8. Kontakt-CTA-Band | „Jetzt Projekt anfragen“ & 📞 Anruf | Werkstatt-Hero, Inhaber-Porträt, 4 Referenzfotos, Förder-Logo |
| **Leistungen (Hub)** | Holzbau & Massivbau Colditz | Unsere Leistungen: Von Zimmerei bis Massivbau aus einer Hand | 1. Hero mit Leistungsversprechen<br>2. 5 große Gewerkekarten mit Detail-Links<br>3. Warum alles aus einer Hand?<br>4. Passende Referenz-Highlights<br>5. FAQ allgemein<br>6. Abschluss-CTA | „Beratung vereinbaren“ | 5 Gewerk-Titelbilder |
| **1. Zimmerei & Holzbau** | Dachstuhl Grimma Colditz | Zimmerei & moderner Holzbau: Dachstühle, Abbund & Konstruktion | 1. Hero mit Gewerk-Fokus<br>2. Leistungen (Dachstühle, Carports, Gauben, Balkone)<br>3. Eigener Abbund & moderne Maschinen<br>4. Lohnschnitt im Sägewerk<br>5. Projektbeispiele (Filter-Loop)<br>6. FAQ Zimmerei<br>7. CTA-Anfrageformular | „Dachstuhl / Holzbau anfragen“ | Abbund-Maschine, fertige Dachstühle, Carports |
| **2. Treppen & Möbel** | Treppenbau Sachsen Colditz | Maßgefertigte Massivholztreppen & individueller Innenausbau | 1. Hero Treppenbau<br>2. Treppenarten (Gerade, Gewendelt, Faltwerk)<br>3. Holzarten & Geländervarianten<br>4. Möbelbau & Einzelanfertigungen<br>5. Referenz-Galerie Treppen<br>6. FAQ Treppenbau<br>7. CTA-Formular | „Treppen-Beratung anfordern“ | Fotos Massivholztreppen, Geländerdetails |
| **3. Maurer & Beton** | Baugeschäft Colditz Maurerarbeiten | Maurer-, Beton- & Fundamentarbeiten für Neu- und Umbau | 1. Hero Massivbau<br>2. Fundamente, Bodenplatten, Decken<br>3. Mauerwerk & Putzarbeiten<br>4. Synergie Holz- & Massivbau<br>5. Referenzen Massivbau<br>6. FAQ Maurerarbeiten<br>7. CTA-Formular | „Massivbau-Angebot anfragen“ | Baustellenfotos, Fundament, Rohbau |
| **4. Altbausanierung** | Denkmalgerechte Altbausanierung Sachsen | Denkmalgerechte Altbausanierung & historische Fachwerksanierung | 1. Hero Denkmalschutz<br>2. Fachwerk-Instandsetzung & Holzreparatur<br>3. Schwammsanierung & Schadstoffbeseitigung<br>4. Energetische Sanierung denkmalgerecht<br>5. Vorher-/Nachher-Referenzen<br>6. FAQ Altbausanierung<br>7. CTA-Formular | „Sanierungsprojekt besprechen“ | Fachwerk historisch, Vorher/Nachher |
| **5. Pellets & Holzbriketts** | Pellets kaufen Colditz | Hochwertige Kaminpellets & Holzbriketts direkt ab Werk Colditz | 1. Hero Brennstoffe<br>2. Produktspezifikationen (Pellets ENplus, Briketts)<br>3. Gebinde (Säcke, Paletten, Abholung/Lieferung)<br>4. Umwelt- & Kostenvorteile<br>5. Vorbestell- & Preisanfrage-Formular<br>6. FAQ Pellets & Abholung | „Pellets / Briketts anfragen“ | Produktfotos Pellets, Paletten, Kaminofen |
| **Referenzen (Hub)** | Referenzen Bauprojekte Colditz | Unsere Referenzen: Handwerksqualität in Bildern | 1. Hero mit Filterbar nach Gewerken<br>2. Dynamisches Loop-Grid (CPT referenzen)<br>3. Projektkarten mit Gewerk, Ort & Bild<br>4. CTA für eigenes Projekt | „Ähnliches Projekt anfragen“ | Alle 132 qualifizierten Referenzfotos |
| **Über uns** | Meisterbetrieb seit 1920 Colditz | Tradition seit 1920: Handwerkskunst in 4. Generation | 1. Hero Geschichte & Generationen<br>2. Chronik 1920 bis heute<br>3. Inhaber Dipl.-Ing. Tobias Müller & Philosophie<br>4. Eigene Werkstatt & moderne Technik<br>5. Regionale Verbundenheit (Colditz & Umland)<br>6. Kontakt-CTA | „Lernen Sie uns kennen“ | Historisches Foto 1920, Werkstatt, Inhaber |
| **Aktuelles** | Aktuelles Zimmerei Müller | Aktuelles aus Werkstatt, Sägewerk & Baustellen | 1. Hero News<br>2. Dynamisches Post-Loop-Grid (Kategorien: Projekte, Wissen, Betrieb)<br>3. Newsletter-/Kontakt-Hinweis | „Zum Kontakt“ | Beitragsbilder |
| **Kontakt & Beratung** | Kontakt Baugeschäft Müller Colditz | Kontakt & Beratung: Wir sind für Ihr Bauvorhaben da | 1. Hero Kontaktaufnahme<br>2. Kontakt-Matrix (Telefon, WhatsApp, E-Mail, Anschrift)<br>3. Qualifiziertes Anfrageformular mit Dateiupload<br>4. Öffnungszeiten & Anfahrts-Hinweis<br>5. Interaktive Karte (nur nach Consent) | „Anfrage absenden“ | Werkstattansicht Außen, Anfahrtskarte |

---

## 4.2 Die drei Design-Stilrichtungen zur Auswahl

Für den Relaunch stehen drei eigenständige, maßgeschneiderte Stilwelten zur Auswahl. Alle drei erfüllen die **Apple Design Principles** (Klarheit, flüssiges Feedback, typografische Hierarchie, großzügiger Weißraum) und setzen auf **Liquid-Glass-Container** via purem CSS.

### Stilrichtung 1: „Meisterhandwerk & Zeitgeist“ (Modern Craft) – [UNSERE EMPFEHLUNG]

> **Charakter**: Souverän, architektonisch, warm-handwerklich und kompromisslos modern. Bringt die Tradition von 1920 mit modernster Abbundtechnik perfekt in Einklang.

* **Referenz-Adjektive**: *Präzise · Architektonisch · Zeitlos*
* **Farbpalette**:
  * **Primär**: `#142238` (Tiefes Schiefer-Marineblau – serios, abgeleitet aus dem Logo-Fundament)
  * **Sekundär / Handwerks-Akzent**: `#C28B45` (Warmes Eichenbraun / Bernstein – Echtholz-Assoziation)
  * **Liquid-Glass Layer**: `rgba(255, 255, 255, 0.80)` mit `backdrop-filter: blur(24px) saturate(190%)` und Lichtkante `border: 1px solid rgba(255, 255, 255, 0.40)`
  * **Hintergrund**: `#FAFAF9` (Warmes Alabaster-Weiß – angenehm fürs Auge, kein grelles Kaltweiß)
  * **Fließtext**: `#334155` (Slate 700 – hervorragende Lesbarkeit)
* **Kontrastnachweis (WCAG 2.1 AA / AAA)**:
  * `#142238` auf `#FAFAF9`: **12.8:1** (Weit über AAA 7.0:1)
  * `#334155` auf `#FAFAF9`: **8.9:1** (AAA erfüllt)
  * `#C28B45` auf `#142238`: **5.2:1** (AA für UI-Komponenten erfüllt)
* **Schriftpaarung (100% lokal gehostet, Open Source)**:
  * Überschriften: **Plus Jakarta Sans** (SemiBold/Bold, geometrisch-architektonisch, mit Apple-Kerning `-0.02em`)
  * Fließtext: **Inter** (Regular/Medium, herausragende Bildschirmschärfe bis auf Smartphones)
* **Button- & Komponentenstil**:
  * Sanfte Radien (12px auf Karten, 9999px Pill auf Buttons).
  * Haptisches Touch-Feedback (`transform: scale(0.97)` bei Klick).
  * Subtile Tiefenschatten: `box-shadow: 0 10px 30px rgba(20, 34, 56, 0.07)`.
* **Bildsprache**: Großzügige, authentische Werkstatt- und Holzbauaufnahmen; warmes Naturlicht; Detailaufnahmen von Holzverbindungen.

---

### Stilrichtung 2: „Tradition & Naturholz“ (Warm Alpine Heritage)

> **Charakter**: Bodenständig, wald- und naturbezogen, gemütlich, traditionsbetont.

* **Referenz-Adjektive**: *Natürlich · Vertraut · Solide*
* **Farbpalette**:
  * **Primär**: `#1E3A2F` (Tiefes Tannengrün / Waldgrün)
  * **Sekundär / Akzent**: `#D4A373` (Helle Douglasie / Kiefernholz)
  * **Liquid-Glass Layer**: `rgba(253, 251, 247, 0.85)` mit Kante `rgba(212, 163, 115, 0.3)`
  * **Hintergrund**: `#FDFBF7` (Warmer Sand/Creme-Ton)
  * **Fließtext**: `#2B2118` (Tiefes Kaffeebraun)
* **Kontrastnachweis**: `#1E3A2F` auf `#FDFBF7`: **11.4:1** (AAA).
* **Schriftpaarung**:
  * Überschriften: **Lora** (stilvolle Handwerks-Serife mit Wärme)
  * Fließtext: **Source Sans 3** (weich, zugänglich)
* **Button- & Komponentenstil**:
  * Klassische Radien (6px–8px), erdige Farbtöne, traditionelle Trennlinien.
* **Bildsprache**: Fokus auf Holzmaserung, Späne, Waldhintergrund, historische Altbauten.

---

### Stilrichtung 3: „Konstruktion & Ingenieurbau“ (Technical Minimalist)

> **Charakter**: Nüchtern, ingenieurmäßig, technisch-konstruktiv, fokussiert auf Statik und Präzision.

* **Referenz-Adjektive**: *Konstruktiv · Analytisch · Linear*
* **Farbpalette**:
  * **Primär**: `#18181B` (Technisches Zink/Graphit)
  * **Sekundär / Akzent**: `#EA580C` (Ziegelorange / Signal-Bauhelm)
  * **Liquid-Glass Layer**: `rgba(244, 244, 245, 0.80)` mit Kante `rgba(24, 24, 27, 0.15)`
  * **Hintergrund**: `#FFFFFF` (Reinweiß)
  * **Fließtext**: `#27272A` (Anthrazit)
* **Kontrastnachweis**: `#18181B` auf `#FFFFFF`: **17.5:1** (AAA).
* **Schriftpaarung**:
  * Überschriften: **Space Grotesk** (technisch, konstruiert)
  * Fließtext: **Roboto** (neutral)
* **Button- & Komponentenstil**:
  * Scharfkantig (2px–4px), monochrome Kontraste, sichtbare Rasterlinien.
* **Bildsprache**: CAD-Konstruktionszeichnungen, Abbundpläne, Großbaustellen, Kräne.

---

## 4.3 Vollständige Designsystem-Spezifikation (Stil 1 – Meisterhandwerk & Zeitgeist)

Nachfolgende Tabelle dient als 1:1 Übertragungsvorlage für die Elementor Site Settings (Global Colors / Global Fonts / Layout):

### A. Globale Farbtokens (Elementor Site Settings)
| Token-Name | Hex-Wert / CSS | Verwendung |
| :--- | :--- | :--- |
| `NEU Primär (Navy)` | `#142238` | Hauptüberschriften, Header-Hintergrund, primäre Markenflächen |
| `NEU Sekundär (Slate)` | `#334155` | Standard-Fließtext, Icons, Meta-Texte |
| `NEU Akzent (Eiche/Amber)`| `#C28B45` | Primäre Action-Buttons, Highlights, Badges, Pfeile |
| `NEU Akzent-Hover` | `#A67433` | Hover- und Fokus-Zustand für Akzent-Buttons |
| `NEU Hintergrund (Warm)` | `#FAFAF9` | Seitenhintergrund (Alabaster) |
| `NEU Surface (Card White)` | `#FFFFFF` | Karten- und Container-Flächen |
| `NEU Surface Glass` | `rgba(255, 255, 255, 0.78)` | Liquid-Glass Karten & Sticky Header |
| `NEU Glass Border` | `rgba(255, 255, 255, 0.45)` | Hauchdünne Lichtkante auf Glasflächen |
| `NEU Border Subtle` | `#E2E8F0` | Dezente Trennlinien und Eingabefeld-Rahmen |
| `NEU Erfolg / Grün` | `#15803D` | Formular-Erfolgsmeldung, Gütesiegel |
| `NEU Fehler / Rot` | `#B91C1C` | Formular-Fehlerhinweise |

### B. Typografie-Skala (Plus Jakarta Sans & Inter)
| Ebene | Schriftfamilie | Schnitt / Gewicht | Größe Desktop | Größe Mobil | Line-Height | Letter-Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Display / Hero H1** | Plus Jakarta Sans | Bold (700) | `48px`–`54px` | `32px`–`36px` | `1.15` | `-0.025em` |
| **H1 (Seiten)** | Plus Jakarta Sans | SemiBold (600) | `38px`–`42px` | `28px`–`30px` | `1.20` | `-0.02em` |
| **H2 (Sektionen)** | Plus Jakarta Sans | SemiBold (600) | `30px`–`34px` | `24px`–`26px` | `1.25` | `-0.015em` |
| **H3 (Karten/FAQ)** | Plus Jakarta Sans | SemiBold (600) | `22px`–`24px` | `19px`–`20px` | `1.30` | `-0.01em` |
| **H4–H6** | Plus Jakarta Sans | Medium (500) | `18px`–`20px` | `17px` | `1.35` | `0` |
| **Body (Fließtext)** | Inter | Regular (400) | `16px` | `16px` (min!) | `1.65` | `0` |
| **Body Large / Lead** | Inter | Regular/Medium | `18px` | `17px` | `1.60` | `-0.005em` |
| **Small / Meta / Badges**| Inter | Medium (500) | `13px`–`14px` | `13px` | `1.50` | `+0.01em` |
| **Button Text** | Plus Jakarta Sans | SemiBold (600) | `15px`–`16px` | `15px` | `1.00` | `0` |

### C. Abstände, Radien & Schatten (8px-Raster)
* **Container-Breite**: `1200px` (Boxed Content Max-Width).
* **Section-Paddings**:
  * Desktop: `80px` bis `96px` oben/unten (großzügiger Weißraum).
  * Mobil: `48px` bis `56px` oben/unten, `20px` seitlich.
* **Element-Gaps**: `16px` (Karten-Inhalt), `24px` (Spalten), `32px` bis `48px` (Sektionen-Grid).
* **Eckenradien (Border-Radius)**:
  * Karten & Container: `16px` (moderne Apple-Rundung).
  * Buttons: `9999px` (Pill-Shape) für höchste Klick-Affordanz.
  * Formularfelder: `10px`.
* **Schatten (Soft Natural Shadows)**:
  * Standard Card: `0 10px 30px -5px rgba(20, 34, 56, 0.06), 0 2px 6px rgba(0, 0, 0, 0.03)`
  * Hover Card Lift: `0 20px 40px -10px rgba(20, 34, 56, 0.12), 0 4px 12px rgba(0, 0, 0, 0.05)`
  * Floating Mobile Bar: `0 12px 36px rgba(20, 34, 56, 0.28)`

---

## 4.4 Komponenten-Katalog (Die 12 Kern-Bausteine)

1. **Header-Komponente (`NEU - Header`)**:
   * Sticky bei Scroll mit Liquid-Glass-Hintergrund.
   * Logo links (Originalgröße mit scharfem SVG/WebP).
   * Horizontale Desktop-Navigation mit Hover-Highlight (`Kontakt` & `Aktuelles` integriert).
   * Rechts: Prominenter Telefon-CTA-Button mit Öffnungszeiten-Status („Mo–Fr erreichbar“).
   * Mobil: Kompakter Burger-Drawer + direkte Schnellanwahl.
2. **Hero-Komponente**:
   * Starke H1 mit Handwerks-Claim und regionaler Verankerung („Colditz & Sachsen“).
   * Zwei komplementäre CTAs: Primär (Anfrage) & Sekundär (Leistungen entdecken).
   * Integrierte Trust-Badges: *Meisterbetrieb seit 1920*, *4. Generation*, *Dipl.-Ingenieur*.
3. **Leistungskarte (Liquid-Glass)**:
   * Transluzenter Container mit Eichen-Akzent-Icon, Teasertext und 3 Kernvorteilen.
   * Button „Details ansehen $ightarrow$“ mit Klick-Zustand.
4. **Referenzkarte (Loop-Item für CPT `referenzen`)**:
   * Bild im 16:10 Format mit sanftem Zoom-Hover.
   * Gewerk-Badge (z. B. „Dachstuhl“, „Treppe“, „Denkmal“).
   * Titel & Ortsangabe (z. B. „Fachwerksanierung in Colditz“).
5. **Trust-Leiste (Vertrauens-Band)**:
   * 4 prägnante Kacheln: *100+ Jahre Erfahrung*, *Eigener Abbund & Sägewerk*, *Dipl.-Ing. Meisterqualität*, *Alles aus einer Hand*.
6. **Prozess-Schritte („In 4 Schritten zu Ihrem Projekt“)**:
   * 1. Unverbindliche Beratung $ightarrow$ 2. Planung & Aufmaß $ightarrow$ 3. Meisterhafter Abbund/Bau $ightarrow$ 4. Abnahme & Übergabe.
7. **FAQ-Accordion**:
   * Sauberes Ausklapp-Element mit Schema.org `FAQPage` Markup für Google Rich Snippets.
8. **Kontakt-Matrix & Lead-Formular**:
   * Schnellauswahl: Telefon, WhatsApp, E-Mail, Anschrift.
   * Elementor-Pro-Formular: Name, Tel (Pflicht!), E-Mail, Gewerk-Dropdown, Nachricht, Datei-Upload für Pläne/Skizzen, DSGVO-Checkbox.
   * Spam-Schutz per Honeypot (ohne Google-Tracker).
9. **Pellet-Verkaufsbox**:
   * Visuelle Präsentation von Kaminpellets (ENplus A1) und Holzbriketts mit Vorbestell-Formular.
10. **EU-/SAB-Förderbanner (Pflicht)**:
    * Rechtssichere Einbindung mit Fördermittel-Logo und exaktem Wortlaut im Startseiten-Unterbereich.
11. **Footer-Komponente (`NEU - Footer`)**:
    * 4-Spaltig: Über den Betrieb, Leistungs-Links, Kontakt & Öffnungszeiten, Rechtliches & SAB-Förderhinweis.
12. **404-Leitsystem**:
    * Freundliche Fehlerseite mit Suchfeld, Schnellverlinkung zu Zimmerei/Massivbau und Kontakt.
