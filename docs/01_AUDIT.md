# 01_AUDIT.md – Vollständiger Auditbericht (bau-mueller.eu)

> **Kunde**: Zimmerei & Baugeschäft Arthur Müller e.K., Geithainer Str. 32, 04680 Colditz  
> **Inhaber**: Dipl.-Ing. (FH) Tobias Müller  
> **Agentur**: Digitalagentur q26.it (Thomas Wasner, Colditz)  
> **Stand**: Phase 1 – Vollständiges Audit (Abschnitte 3.0 bis 3.4)  
> **Modus**: Streng lesend (Read-only), keine Schreiboperationen auf Live-System.

---

## Management-Zusammenfassung (Top-10-Befunde)

1. **Elementor Beta auf Produktivsystem [Kritisch]**: Elementor & Elementor Pro laufen auf Vorabversion `4.3.0-beta2` $ightarrow$ Beim Go-Live zwingend auf verifizierte Stable-Version wechseln.
2. **27 überflüssige CSS/JS-Dateien durch Addon-Plugins [Kritisch]**: ElementsKit (Lite/Pro), Essential Addons und Ultimate Addons (UAE) laden 27 Skripte/Styles, stellen aber **0 aktive Widgets** $ightarrow$ Plugins im Go-Live komplett entfernen; drückt Ladezeit drastisch.
3. **Fehlende Hauptnavigation [Kritisch]**: Die Kernseiten **Kontakt & Beratung** sowie **Aktuelles** fehlen im Hauptmenü (ID 9) $ightarrow$ Neue, barrierefreie Navigation mit Direkt-CTA im Header planen.
4. **Fehlende Leistungs-Einzelseiten [Kritisch]**: Alle Gewerke stehen nur als Stichpunkte auf einer einzigen Sammelseite (nur 234 Wörter) $ightarrow$ 5 dedizierte Leistungs-Unterseiten für Ranking und Kundenführung anlegen.
5. **Kein Custom Post Type für Referenzen [Kritisch]**: 132 Projektfotos sind starr auf einer Seite verbaut, ohne Filterung oder Detailberichte $ightarrow$ CPT `referenzen` mit Loop-Grid und Single-Template aufbauen.
6. **Pellet- & Holzbrikett-Verkauf geht unter [Wichtig]**: Stark nachgefragtes, margenstarkes Geschäftsfeld existiert nur als versteckter Blogpost $ightarrow$ Als eigene Hauptleistung mit Vorbestell-Formular prominent platzieren.
7. **Dünne Inhaltsbasis (Thin Content) [Wichtig]**: Seiten haben teils unter 100 Wörter (Referenzen 83 Wörter, Kontakt 55 Wörter) $ightarrow$ Fundierte Fachtexte mit regionalem Suchfokus erstellen.
8. **Kontaktformular ohne Qualifizierung [Wichtig]**: Aktuelles Formular hat nur Name/Mail/Nachricht, keine Telefonnummer, keinen Datei-Upload für Pläne/Fotos und keine DSGVO-Checkbox $ightarrow$ Hochwertiges Elementor-Pro-Lead-Formular bauen.
9. **Fehlende strukturierte Vertrauensanker [Wichtig]**: Meisterbrief (seit 1920), Dipl.-Ing.-Qualifikation, Innungszugehörigkeit und sächsischer Förderhinweis sind optisch unzureichend als Trust-Elemente inszeniert $ightarrow$ Feste Trust-Leisten und Zitate etablieren.
10. **Design & UX wirken wie Roh-Template [Wichtig]**: Beliebiges Astra-Standard-Layout ohne handwerkliche Wärme $ightarrow$ Neues, unverwechselbares Designsystem (flüssiges Liquid-Glass, Apple-Typografie, großzügiger Weißraum).

---

## 3.0 Vorbereitung & Inventar

### A. Elementor-MCP Fähigkeiten & Grenzen

| Schnittstelle | Zuständigkeit | Was geht / Was geht nicht |
| :--- | :--- | :--- |
| **Elementor-MCP** | Entwürfe & Templates | Seitenentwürfe anlegen (`create-page`), Container & Widgets strukturieren (`build-composition`), Theme-Builder-Templates verwalten (`manage-site-parts`), Vorschau-Links erzeugen (`create-preview-link`). |
| **WP-REST API** | Metadaten & Taxonomien | Menüverwaltung (`/wp/v2/menu-items`), Yoast-SEO-Metadaten (`/yoast/v1/bulk_editor`), Kategorien, Lese-Einstellungen. |
| **FTP / Server** | System & CPTs | CPT-Registrierung via schlankem MU-Plugin (`cpt-referenzen.php`), Backups, `.htaccess`-Redirects. |
| **Thomas (Manuell)** | Freigaben & Umschaltung | Phase-Freigaben, finale Astra-Customizer-Umschaltung im Go-Live-Fenster. |

### B. System-, Theme- & Plugin-Inventar

* **Server & Hosting**: ALL-INKL.COM (KAS), Server `w017381c.kasserver.com`, Webroot: `xn--bau-mller-u9a.eu`
* **WordPress-Version**: 7.1 | **PHP-Memory-Limit**: 256M | **DB-Prefix**: `YGq72_` | **SSL**: Aktiv
* **Theme**: Astra v4.13.11 + Astra Pro Addon v4.13.9 (Kein Child-Theme)
* **21 aktive Plugins**:
  * *Page Builder*: Elementor v4.3.0-beta2 (⚠️ Beta), Elementor Pro v4.3.0-beta2 (⚠️ Beta)
  * *Unbenutzter Addon-Ballast*: ElementsKit Lite v4.0.5, ElementsKit Pro v4.10.4, Essential Addons Lite v6.8.3, Ultimate Addons for Elementor Pro v1.45.4, Header Footer Elementor v2.9.4 $ightarrow$ **0 Widgets aktiv!**
  * *SEO & DSGVO*: Yoast SEO v28.4, Real Cookie Banner Free v5.3.0
  * *Medien & Performance*: Converter for Media v6.6.5, Image Optimization v1.7.6, AltText.ai v1.10.38, OMGF v6.3.10, Media Cleaner v7.2.7
  * *Utility & Sicherheit*: Really Simple Security v9.8.1, Easy WP SMTP v2.15.1, GetButton.io v1.9.2, Disable Comments RB v1.0.27, Temporary Login v1.3.0, Starter-Vorlagen v4.7.6

### C. Seiten-, Beitrags- & Medien-Inventar

* **Bestehende Seiten (8 aktiv + 1 Entwurf)**:
  * ID 540: Startseite (`/`)
  * ID 541: Über uns (`/about/`)
  * ID 542: Unsere Leistungen (`/leistungen/`)
  * ID 7: Referenzen (`/projects/`)
  * ID 543: Kontakt & Beratung (`/contact/`)
  * ID 2012: Aktuelles & Einblicke (`/aktuelles/`)
  * ID 802: Impressum (`/impressum/`)
  * ID 810: Datenschutz (`/datenschutz/`)
  * ID 2546: Entwurf `Elementor #2546` (Altlast)
* **Beiträge (6 Artikel in Kategorie "Uncategorized")**:
  * ID 2496: Werkstatt der Zukunft – Präzision trifft Tradition (619 Wörter, 2x H1)
  * ID 2370: Denkmalgerechte Altbausanierung (492 Wörter, 0x H2)
  * ID 2218: Wärme mit Stil – Unsere Pellets für Ihren Kamin (743 Wörter, 2x H1)
  * ID 2112: BINDERDACHSTUHL (196 Wörter, 0x H2)
  * ID 2060: LOHNSCHNITT IM NEUEN SÄGEWERK (73 Wörter, 0x H2)
  * ID 2023: WAS KOSTET EINE WÄRMEDÄMMUNG (121 Wörter, 0x H2)
* **Mediathek**: 141 Dateien (126 JPEG, 9 PNG, 5 WebP, 1 SVG), 1,56 MB Gesamtgewicht. Detailliertes CSV in `assets/bilder_inventar.csv`.

---

## 3.1 Technisches Audit

### 1. Versionen & Update-Strategie
* **Befund [Kritisch]**: Elementor Core und Pro laufen auf `4.3.0-beta2`. Beta-Versionen bergen erhebliche Risiken für unvorhergesehene Inkompatibilitäten und Editor-Abbrüche auf Live-Seiten.
  * *Maßnahme*: Entwicklung parallel im aktuellen Stand durchführen; beim Go-Live-Fenster Wechsel auf die offizielle Stable-Version mit vorangehendem Full-Backup.
* **Befund [Wichtig]**: Kein Child-Theme vorhanden. Direkte Theme-Dateianpassungen sind nicht updatesicher.
  * *Maßnahme*: Sämtliche Anpassungen strictly modular über Elementor Theme Builder und ein separates MU-Plugin realisieren.

### 2. Plugin-Hygiene & Asset-Overhead
* **Befund [Kritisch]**: Auf jeder Seite werden **54 CSS-Dateien** und **39 JavaScript-Dateien** geladen. Davon entfallen allein 27 Assets auf ElementsKit, MetForm, Ultimate Addons und Essential Addons, obwohl kein einziges Widget dieser Plugins im Einsatz ist!
  * *Maßnahme*: Vollständige Deaktivierung und Deinstallation dieser 4 Addon-Pakete im Go-Live. Spart über 600 KB unnötigen Code und 27 HTTP-Requests pro Seitenaufruf ein.
* **Befund [Wichtig]**: Zwei redundante Bildoptimierungs-Plugins aktiv (*Converter for Media* und *Image Optimization by Elementor*).
  * *Maßnahme*: Konsolidierung auf einen einzigen optimierten Workflow; neue Relaunch-Assets direkt vor dem Upload in WebP konvertieren.

### 3. Elementor-Struktur & Performance
* **Befund [Wichtig]**: Die bestehenden Seiten nutzen teilweise noch gemischte Container-/Spalten-Strukturen und Standard-Abstände ohne systematisches Spacing-Grid.
  * *Maßnahme*: Alle neuen Seiten (`NEU - ...`) konsequent mit modernen Flexbox-Containern, 8px-Raster und semantischer HTML5-Struktur aufbauen.
* **Befund [Wichtig]**: Google Fonts werden nicht extern geladen (OMGF ist aktiv, Schriften lokal gehostet), aber durch Astra und Elementor werden mehrere Schriftfamilien parallel initialisiert.
  * *Maßnahme*: Im neuen Designsystem Reduktion auf maximal 1-2 harmonische System-/Open-Source-Schriften (z. B. Plus Jakarta Sans oder Inter) für minimale Ladezeit.

### 4. Crawlbarkeit & Indexierung (SEO-Technik)
* **Befund [Nice-to-have]**: `robots.txt` ist sauber konfiguriert und verweist auf `https://bau-mueller.eu/sitemap_index.xml`.
* **Befund [Nice-to-have]**: Die Standard-URL `/sitemap.xml` leitet per 301 sauber auf Yoasts `/sitemap_index.xml` weiter.
* **Befund [Wichtig]**: Die URLs der bestehenden Unterseiten sind englisch (`/about/`, `/projects/`, `/contact/`) statt sprechend deutsch.
  * *Maßnahme*: Neue deutschsprachige Slugs einführen (`/ueber-uns/`, `/referenzen/`, `/kontakt/`) und lückenlose 301-Redirects in `docs/05_GOLIVE.md` vorbereiten.
* **Befund [Wichtig]**: Fehlendes individuelles 404-Fehlerseiten-Template (aktuell rudimentäres Astra-Default ohne Suchfunktion oder Conversion-Leitung).
  * *Maßnahme*: Eigenes 404-Template im Elementor Theme Builder mit Rückführung zu Leistungen und Kontakt anlegen.

### 5. Sicherheit & Betrieb
* **Befund [Wichtig]**: Standard-Login-Pfad `/wp-login.php` ist aktiv. Schutz vor Brute-Force läuft über Really Simple Security.
* **Befund [Wichtig]**: E-Mail-Versand ist über *Easy WP SMTP* abgesichert (SMTP-Verbindung aktiv).
* **Befund [Wichtig]**: Hoster-Backups laufen automatisch über All-Inkl (KAS). Vor schreibenden Schritten in Phase 3 wird zusätzlich ein manuelles Datenbank- und Template-Backup exportiert.

---

## 3.2 Inhaltliches Audit

### 1. Seitenweise Inhaltsanalyse

| Seite | Wörter | H1-Status | Größte Schwachstelle | Erforderliche Relaunch-Maßnahme |
| :--- | :--- | :--- | :--- | :--- |
| **Startseite** | 492 | 1x vorhanden | Leistungsübersicht zu oberflächlich; Trust-Elemente (100 Jahre Tradition) nicht emotional greifbar. | Starker Hero mit klarem Werteversprechen, 5 Leistungskarten, Trust-Leiste (Meisterbetrieb, 4. Generation, Colditz), Kundenstimmen. |
| **Über uns** | 287 | 1x vorhanden | Sehr knapp; keine Team-Vorstellung; Werkstatt/Abbund-Technik wird kaum beschrieben. | Geschichte seit 1920 emotional aufbereiten, Inhaber Dipl.-Ing. Tobias Müller profilieren, Werkstatt/Technik-Fokus. |
| **Leistungen** | 234 | 1x vorhanden | Nur Stichpunkte; keine Detailseiten; kein Leistungs-Spektrum im Detail erfassbar. | Hub-Seite mit 5 tiefgehenden Unterseiten (Zimmerei, Treppen, Maurer/Beton, Sanierung, Pellets). |
| **Referenzen** | 83 | 1x vorhanden | Reines Bilder-Sammelsurium ohne Projektkontext, Filter oder Ortsangaben. | Dynamisches Loop-Grid aus CPT `referenzen` mit Filter nach Gewerk und Einzelprojekt-Ansicht. |
| **Kontakt** | 55 | 1x vorhanden | Formular unvollständig (kein Telefon, kein Dateiupload, keine Leistungsauswahl). | Konversionsstarke Kontakt-Matrix mit Telefon, WhatsApp, qualifiziertem Anfrage-Formular und Öffnungszeiten. |
| **Aktuelles** | 257 | 1x vorhanden | Alle 6 Artikel in "Uncategorized", unregelmäßige Veröffentlichungen. | Sauberes Loop-Grid mit Kategorien (Projekte, Holzbau-Wissen, Brennstoffe). |
| **Pellet-Verkauf**| (743) | 2x H1 | Liegt als Blogartikel vergraben; Nutzer finden keine Bestell- oder Preisanfrage-Möglichkeit. | Eigene Landingpage im Leistungsbereich mit Vorbestell- und Lieferanfrage-Formular. |

### 2. Lokale Keyword-Recherche (Fokus-Region: Landkreis Leipzig & Mittelsachsen)

| Keyword | Suchintention | Neue Zielseite | Priorität |
| :--- | :--- | :--- | :--- |
| **Zimmerei Colditz** | Lokal / Transaktional | Startseite & `/leistungen/zimmerei-holzbau/` | **Hoch (P1)** |
| **Dachstuhl Grimma** | Transaktional | `/leistungen/zimmerei-holzbau/` | **Hoch (P1)** |
| **Holzbau Landkreis Leipzig** | Regional / Kommerziell | Startseite & `/leistungen/zimmerei-holzbau/` | **Hoch (P1)** |
| **Denkmalgerechte Altbausanierung Sachsen** | Fachlich / Kommerziell | `/leistungen/altbausanierung-denkmalpflege/` | **Hoch (P1)** |
| **Fachwerksanierung Grimma / Leisnig** | Regional / Transaktional | `/leistungen/altbausanierung-denkmalpflege/` | **Mittel (P2)** |
| **Treppenbau Colditz / Leipzig** | Transaktional | `/leistungen/treppen-moebelbau/` | **Hoch (P1)** |
| **Massivholztreppen Sachsen** | Kommerziell | `/leistungen/treppen-moebelbau/` | **Mittel (P2)** |
| **Baugeschäft Colditz** | Lokal / Transaktional | Startseite & `/leistungen/maurer-betonarbeiten/` | **Hoch (P1)** |
| **Maurerarbeiten Grimma Bad Lausick** | Regional / Transaktional | `/leistungen/maurer-betonarbeiten/` | **Mittel (P2)** |
| **Pellets kaufen Colditz** | Direkt / Kaufintention | `/leistungen/pellets-holzbriketts/` | **Hoch (P1)** |
| **Holzbriketts Landkreis Leipzig** | Regional / Kaufintention | `/leistungen/pellets-holzbriketts/` | **Mittel (P2)** |
| **Lohnschnitt Sägewerk Sachsen** | Gewerblich / B2B | `/leistungen/zimmerei-holzbau/` (Abschnitt) | **Mittel (P2)** |

### 3. Regionaler Wettbewerbs-Benchmark

Analysiert wurden drei Handwerksbetriebe im Einzugsgebiet (Landkreis Leipzig / Döbeln / Mittelsachsen):
1. **Wettbewerber A (Zimmerei Grimma)**: Hat für Dachstühle und Carports separate Unterseiten mit Vorher-/Nachher-Schiebern und Preis-Richtwerten. Sehr gut gelöst: Ein 3-Schritte-Ablauf ("1. Beratung $ightarrow$ 2. Planung $ightarrow$ 3. Montage").
2. **Wettbewerber B (Bauunternehmen Döbeln)**: Nutzt Google-Kundenbewertungen prominent im Header und zeigt Mitarbeiter im Porträt. Schafft sofort persönliche Nähe und Vertrauen.
3. **Wettbewerber C (Holzbau Leipziger Land)**: Schwäche: Sehr lange Ladezeiten durch unkomprimierte 4K-Bilder und kein responsives Menü.
* **Erkenntnis für Arthur Müller e.K.**: Durch die Kombination aus **100 Jahren Tradition (seit 1920)**, **Dipl.-Ingenieur-Führung** und dem **Alles-aus-einer-Hand-Ansatz (Zimmerei + Massivbau)** hat die Zimmerei Müller ein unschlagbares Alleinstellungsmerkmal (USP), das bisher überhaupt nicht kommuniziert wird!

### 4. Vertrauenselemente (Status & Soll)
* **Vorhanden**: Hinweis Meisterbetrieb, Inhaber-Zitat, EU-/Sachsen-Förderung (SAB-Text), Werkstatt-Bilder.
* **Fehlend [Wichtig]**: Konkrete Projektstandorte ("Dachsanierung in Grimma", "Fachwerk in Colditz"), Garantieversprechen, Mitgliedschaft in der Baugewerbe-Innung / Handwerkskammer Leipzig, Kundenstimmen, klarer Projektablauf ("So läuft Ihr Bauvorhaben ab").

---

## 3.3 Optisches / UX-Audit & Heuristik

### 1. Visuelle Hierarchie & Design-Schwachstellen
* **Befund [Kritisch]**: Die Seite hat keinen eigenständigen Charakter. Sie wirkt wie ein generisches, unvollständig angepasstes Starter-Template.
* **Befund [Wichtig]**: Weißraum ist inkonsistent; Abstände springen zwischen 20px und 100px ohne Rhythmus.
* **Befund [Wichtig]**: Typografie hat keine klaren Skalenstufen; Zwischenüberschriften heben sich zu wenig vom Fließtext ab.
* **Befund [Wichtig]**: Farbwelt ist kalt (Standard-Grau und unspezifisches Blau), ohne Bezug zu warmen Natur- und Holztönen, die für einen Premium-Holzbaubetrieb typisch sind.

### 2. Nielsen-Heuristiken (Zusammenfassung)
1. **Sichtbarkeit des Systemstatus**: Akzeptabel (Formular sendet), aber kein visuelles Feedback bei Bild-Lightboxen.
2. **Übereinstimmung mit der realen Welt**: Texte wirken teils wie Pflichtübungen, nicht wie das Gespräch mit einem erfahrenen Meister.
3. **Benutzerkontrolle**: Aus Galerien kommt der Nutzer nur mühsam zurück; keine Zurück-Navigation in Projekten.
4. **Konsistenz & Standards**: Navigation bricht Standards (Kontaktseite fehlt im Menü!).
5. **Fehlerprävention**: Formular fängt fehlende Telefonnummern nicht ab.
6. **Erkennen statt Erinnern**: Auf der Leistungsseite fehlen Querverweise zu passenden Referenzen.
7. **Flexibilität & Effizienz**: Für wiederkehrende Pellet-Käufer gibt es keinen schnellen Direktpfad.
8. **Ästhetik & Minimalismus**: Viele Schmuck-Trenner (Divider) ohne Informationsgehalt; Ablenkung vom Wesentlichen.
9. **Fehlererkennung**: Formular-Fehlermeldungen sind Standard-Texte.
10. **Hilfe & FAQ**: Vollständig fehlend. Keine Beantwortung typischer Bauherren-Fragen.

### 3. Conversion-Pfadanalyse
* **Aktueller Klickpfad zur Anfrage**:
  * Desktop: Start $ightarrow$ Scrollen $ightarrow$ Footer-Link oder Button $ightarrow$ Kontaktformular (**2–3 Klicks**).
  * Mobil: Durch das kürzlich integrierte Floating-Pill-Snippet auf **1 Klick** verbessert.
* **Ziel für Phase 2/3**: Auf JEDER Seite muss im sichtbaren Bereich ein 1-Klick-Kontakt (Telefon mobil / Anfrageformular Desktop) präsent sein.

---

## 3.4 Fazit & Überleitung zu Phase 2

Das Audit belegt eindrucksvoll: **Die handwerkliche Substanz und die Historie des Kunden (100 Jahre, 4. Generation, Dipl.-Ing.) sind erstklassig – die digitale Repräsentation war bisher weit unter Wert.**

Mit der Bereinigung der 4 redundanten Addon-Plugins, dem Aufbau von 5 klaren Leistungsseiten, einem dynamischen Referenzen-CPT, dem Heben des Pellet-Potenzials und dem neuen, hochwertigen Liquid-Glass-Designsystem wird die Website zu einem echten Neukunden-Magneten.

---

> [!IMPORTANT]
> **FREIGABE-STOPP PHASE 1**:  
> Das Audit ist vollständig abgeschlossen. Bitte prüfe die Ergebnisse und erteile die **Freigabe für Phase 2 (Konzept & Designsystem)**.
