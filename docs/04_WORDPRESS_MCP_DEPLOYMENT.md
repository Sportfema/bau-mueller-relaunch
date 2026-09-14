# 04_WORDPRESS_MCP_DEPLOYMENT.md – Deployment-Leitfaden für heute Abend

> **Projekt**: Relaunch `bau-mueller.eu` (Zimmerei & Baugeschäft Arthur Müller e.K., Colditz)  
> **Agentur**: Digitalagentur q26.it (Thomas Wasner)  
> **Design**: Somerville Architectural Craft (Warme Farbwelt `#F8F5EE`, Charcoal `#1C1B1A`, Akzent `#E31936`, 32px Radien, Pill-Buttons, 100% echte Fotos)  
> **Stand**: Alle 5 Seiten, Header/Footer, interaktive HTML-Prototypen und Elementor-Vorlagen sind fertig vorbereitet.

---

## 1. Vorbereitete Seiten & Status

Alle Seiten sind als reine **Entwürfe (`status: draft`)** mit dem Präfix `NEU – ` konfiguriert. Die bestehende Live-Website bleibt zu jedem Zeitpunkt unberührt!

| Seite | Slug / URL | ID (falls existent) | Status | Kern-Inhalte & Medien |
| :--- | :--- | :--- | :--- | :--- |
| **NEU – Startseite** | `/startseite-neu/` | **2595** (aktualisieren) | Entwurf (`draft`) | • Hero mit Ken-Burns-Videozoom auf **Tor** (`Tor-Zimmerei-Mueller.jpeg`, ID 2473)<br>• 3 Leistungs-Cards (Wildenhain ID 1304, Treppe ID 1418, Röhrsdorf ID 1390)<br>• Dunkler Werkstatt-Slab mit echten Fotos: Sägewerk (`start4.jpg` ID 602), Werkbank (`start3.jpg` ID 601), Montagehalle (`start2.jpg` ID 600)<br>• Regionaler Pelletkreislauf (ENplus A1)<br>• Zitat Tobias Müller & historisches Teamfoto (`uberunssw.jpg` ID 703)<br>• EU-Fördersignet Sachsen (`EFRE...` ID 2485)<br>• 4-Schritte-Ablauf & Kontakt-Banner |
| **NEU – Leistungen** | `/leistungen/` | Neu anlegen | Entwurf (`draft`) | • Hub für alle 5 Gewerke<br>• Große Feature-Karten mit echten Fotos<br>• Der Bauherren-Vorteil (Zimmerei + Massivbau aus einer Hand)<br>• FAQ-Bereich |
| **NEU – Referenzen** | `/referenzen/` | Neu anlegen | Entwurf (`draft`) | • Filterbare Galerie (Somerville Pill-Buttons: Alle, Zimmerei, Treppenbau, Massivbau, Denkmalpflege)<br>• 100% echte Projektfotografien im Editorial-Grid |
| **NEU – Über uns** | `/ueber-uns/` | Neu anlegen | Entwurf (`draft`) | • 100+ Jahre Familientradition (seit 1920, 4. Generation)<br>• Historisches Foto ID 703<br>• Virtueller Werkstattrundgang mit echten Maschinen<br>• Diplom-Ingenieur-Standard & GRW-Förderung |
| **NEU – Zimmerei & Holzbau** | `/leistungen/zimmerei-holzbau/` | Neu anlegen | Entwurf (`draft`) | • Einzelleistungs-Blueprint<br>• Dachstühle, Abbund, Gauben, Balkone, Hallen<br>• Werkstattabbund-Vorteil & Lohnschnitt im Sägewerk<br>• Holzbau-FAQ |
| **NEU – Header** | Theme Builder | **2589** (aktualisieren) | Vorlage | Minimalistischer Architektur-Header, Pill-CTA |
| **NEU – Footer** | Theme Builder | **2590** (aktualisieren) | Vorlage | Dunkler Architektur-Slab, 4 Spalten, Pellets-Hinweis, Impressum/Datenschutz |

---

## 2. Durchführung heute Abend am anderen Rechner

Am gestrigen Rechner stehen dir **drei extrem einfache Wege** zur Verfügung:

### Weg A: Automatisiertes Skript (Empfohlen – 1 Befehl)

1. Repository auf den neuesten Stand bringen:
   ```bash
   git pull origin main
   ```
2. Übertragung mit deinen Anmeldedaten ausführen:
   ```bash
   python3 scripts/deploy_to_wordpress.py --user AdminThomas --password "xxxx xxxx xxxx xxxx"
   ```
   *(Alternativ kannst du die Zugangsdaten einmalig in eine `.env`-Datei schreiben und einfach `./scripts/deploy_to_wordpress.py` ausführen.)*

3. **Was das Skript automatisch tut**:
   * Verbindet sich mit `https://bau-mueller.eu` über die REST-API.
   * Aktualisiert Entwurf-ID 2595 (`NEU – Startseite`).
   * Legt `NEU – Leistungen`, `NEU – Referenzen`, `NEU – Über uns` und `NEU – Zimmerei & Holzbau` als Entwürfe an (oder aktualisiert sie, falls bereits angelegt).
   * Setzt das Template automatisch auf `elementor_header_footer`.
   * Gibt dir sofort alle direkten WordPress-Editier- und Vorschau-Links im Terminal aus.

---

### Weg B: Über den Elementor-MCP in Claude

Wenn du auf dem anderen Rechner mit Claude Code oder Claude Desktop arbeitest (wo der MCP mit `bau-mueller.eu` gekoppelt ist):

1. `git pull origin main`
2. Gib Claude einfach folgenden Prompt:
   > *"Lies `docs/04_WORDPRESS_MCP_DEPLOYMENT.md` und übertrage alle Entwürfe aus dem Ordner `exports/` auf WordPress. Aktualisiere Seite 2595 und lege die weiteren Unterseiten als Entwürfe mit Template elementor_header_footer an."*

Claude liest die JSON-Dateien aus `exports/` und führt die MCP-Befehle (`create-page`, `build-composition`) direkt aus.

---

### Weg C: Import über das WordPress-Backend (Ohne API/MCP)

Falls du die Seiten direkt als Elementor-Vorlagen importieren möchtest:
1. Im WordPress-Admin zu **Elementor $ightarrow$ Vorlagen $ightarrow$ Gespeicherte Vorlagen** navigieren.
2. Oben auf **„Vorlage importieren“** klicken.
3. Die fertigen JSON-Dateien aus dem Ordner `exports/elementor_templates/` auswählen:
   * `startseite.json`
   * `leistungen.json`
   * `referenzen.json`
   * `ueber-uns.json`
   * `zimmerei-holzbau.json`
4. Nach dem Import kannst du jede Vorlage mit einem Klick in eine neue Seite einfügen.

---

## 3. Datei-Übersicht im Repository

* **`prototypes/`**: Vollständig lauffähige, interaktive HTML-Prototypen aller 5 Seiten. Können per Doppelklick in jedem Browser geöffnet werden!
  * `somerville_prototype.html`
  * `leistungen_prototype.html`
  * `referenzen_prototype.html`
  * `ueberuns_prototype.html`
  * `zimmerei_prototype.html`
* **`exports/`**:
  * `neu-startseite-2595.json`
  * `neu-leistungen.json`
  * `neu-referenzen.json`
  * `neu-ueber-uns.json`
  * `neu-zimmerei-holzbau.json`
  * `neu-header-2589.json`
  * `neu-footer-2590.json`
  * `elementor_templates/*.json`: Sofort importierbare Elementor-Vorlagen
  * `html_snippets/*.html`: Reine HTML/Tailwind/CSS-Bausteine
* **`scripts/`**:
  * `deploy_to_wordpress.py`: Automatisches Deployment-Skript
  * `build_exports.py`: Export-Generator aus den Prototypen

---

## 4. Qualitätssicherung & Verifikation nach dem Import

Nach dem Übertrag bitte folgende Punkte im WordPress-Backend kurz gegenprüfen:
1. [ ] **Status aller neuen Seiten**: Steht auf `Entwurf` (`draft`).
2. [ ] **Template**: Steht auf `Elementor Header/Footer`.
3. [ ] **Hero-Zoom Startseite**: Tor (`Tor-Zimmerei-Mueller.jpeg`, ID 2473) zoomt sanft ein (Ken Burns Effekt).
4. [ ] **Null KI-Bilder**: Es sind nur authentische Werkstatt-, Sägewerk- und Projektfotos verbaut.
5. [ ] **CTA-Links & Telefonnummern**: `tel:+493438143336` und `/kontakt/` sind überall klickbar.
