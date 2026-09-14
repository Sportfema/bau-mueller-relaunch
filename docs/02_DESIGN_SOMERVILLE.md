# Design-Transformation: Architectural Modern Craft (Somerville-Stil)

> **Projekt**: Relaunch bau-mueller.eu  
> **Referenz**: [Somerville (somervilles.co.uk)](https://somervilles.co.uk/)  
> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K. (Colditz)  
> **Status**: Konzept & Spezifikation für Elementor-Übertragung

---

## 1. Warum das bisherige Design nach „KI“ aussah – und was sich ändert

| Merkmal | Typisches „KI-Design“ (alt) | Somerville Architectural Craft (neu) |
| :--- | :--- | :--- |
| **Farbwelt** | Kaltes Weiß `#FFFFFF`, Tech-Marineblau, generative Verläufe | Warmer Creme-Fond (`#F8F5EE`), tiefes Warm-Charcoal (`#1C1B1A`), feiner Karminrot-Akzent (`#E31936`) |
| **Karten & Formen** | Schwebender Glas-Blur (Glassmorphism), weiße Standardboxen mit 8px-Radius | Großzügig gerundete "Architectural Slabs" (`32px`–`36px` Radius) als fließende Baukörper |
| **Bildsprache** | Stockfoto-Ästhetik oder generische Icons in farbigen Kreisen | Großflächige, authentische Werkstatt-, Holz- und Bauaufnahmen im 4:5- oder 16:10-Format |
| **Interaktion** | Generische Rechteck-Buttons mit Schatten | Vollständig abgerundete Pill-Buttons (`9999px`) mit Chevron & schwebende Circular-Action-Badges |
| **Typografie** | Gleichförmig, wenig Kontrast zwischen Headline und Fließtext | Geometrisch-prägnante Grotesk (Plus Jakarta Sans) mit engem Kerning (`-0.03em`) und großem Größenkontrast |
| **Seitenrhythmus** | Gleichförmiges 3-Spalten-Raster Sektion für Sektion | Wechsel aus Split-Layouts, asymmetrischen Galerien, Vollbild-Bannern und dunklen Einlege-Böden |

---

## 2. Das neue Designsystem im Detail

### A. Farb-Tokens
- `--bg-cream`: `#F8F5EE` (Haupt-Seitenhintergrund, wohnlich, warm, kein Kaltweiß)
- `--bg-charcoal`: `#1C1B1A` (Dunkle Sektionen, architektonisch, edel)
- `--bg-charcoal-card`: `#262523` (Kartenflächen innerhalb dunkler Sektionen)
- `--text-dark`: `#1A1918` (Primärtext auf hellem Grund, 100 % lesbar)
- `--text-light`: `#FFFCF5` (Primärtext auf dunklem Grund)
- `--text-muted`: `#6E6963` (Editorial-Sekundärtext)
- `--accent-red`: `#E31936` (Präziser Karminrot-Akzent für Pfeile, Badges, Status-Dots)

### B. Radien & Baukörper
- `--radius-slab`: `32px` bis `40px` (Großsektionen & Hero-Container)
- `--radius-card`: `20px` bis `24px` (Bildkarten & Feature-Blöcke)
- `--radius-pill`: `9999px` (Buttons, Status-Badges)

### C. Komponenten nach Somerville-Vorbild
1. **Hero-Bühne**: Großflächiges Handwerksbild mit abgerundetem Container, unten verankerter Typografie, feiner Trennlinie (`border-t`) und komplementärem Pill-Button.
2. **Gewerke-Karten**: Vertikale Bildkarten mit weißer Aktions-Plakette (rotes Plus-Icon) unten rechts, dezentem Hover-Zoom und typografischer Unterstreichung.
3. **Dunkler Baukörper ("Architectural Slab")**: Großer, abgerundeter Einlegeboden mit Split-Intro (Headline links, Pill-Button rechts) und 3 klaren Säulen mit echten Werkstattaufnahmen.
4. **Closed-Loop / Nachhaltigkeit**: Asymmetrische 2-Spalten-Sektion für den geschlossenen Holzkreislauf (Pellets & Holzbriketts aus eigenem Restholz).
5. **Portfolio-Galerie**: Asymmetrisches Projekt-Raster mit Gewerke-Tags und schwebenden Aktions-Badges.
6. **Werkstatt-Großbanner**: Breites Querformat der Fertigungshalle/des Abbundzentrums mit integrierter Typografie.
7. **Architektonischer Footer**: Dunkler Baukörper mit abgerundeter Oberkante, großem Headline-CTA und aufgeräumter 4-Spalten-Architektur.

---

## 3. Bildmaterial: 100 % Echte Fotos (Zero AI)

Nach Kundenprüfung wurden alle KI-generierten Platzhalter (die stilisierte Scheune und das Schraubzwingen-Werkzeugwand-Bild `Start1.jpg`) vollständig entfernt.

Es kommen ausschließlich echte Aufnahmen aus Werkstatt, Sägewerk und Referenzen zum Einsatz:
1. **Hero**: `Tor-Zimmerei-Mueller.jpeg` mit cinematografischem Ken-Burns-Video-Zoom (`animation: kenBurnsZoom`).
2. **Gewerke-Karten**:
   - Zimmerei: `Dachstuhl-Sanierung-Kirche-Wildenhain.jpeg`
   - Treppenbau: `Wangentreppe-viertelgewendelt-Koltzschen.jpeg`
   - Massivbau: `Sichtmauerwerk-Röhrsdorf.jpeg`
3. **Werkstatt- & Sägewerk-Säulen**:
   - Sägewerk / Baumstamm-Zuschnitt: `start4.jpg`
   - Präzisions-Zuschnitt / Tischkreissäge: `start3.jpg`
   - Meisterliche Holzwerkstatt: `start2.jpg`
4. **Kreislauf & Pellets**: `start4.jpg` (Sägespäne als Rohstoff für ENplus A1 Pellets)
5. **Referenzen-Galerie**: `Dachstuhl-Sanierung-Kirche-Wildenhain.jpeg`, `Wangentreppe-viertelgewendelt-Koltzschen.jpeg`, `Putzsanierung-Kirchturm-Zschirla.jpeg`
6. **Historie & Über uns**: `uberunssw.jpg` (Historische Aufnahme der Zimmerer-Mannschaft)
