# Build script to generate exports
import json
import re
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("exports/elementor_templates", exist_ok=True)
os.makedirs("exports/html_snippets", exist_ok=True)

pages = [
    {
        "key": "startseite",
        "id": 2595,
        "title": "NEU – Startseite",
        "slug": "startseite-neu",
        "prototype": "prototypes/somerville_prototype.html",
        "desc": "Startseite im Somerville Architectural Craft Design mit echtem Tor-Hero (Ken Burns Zoom), 3 Kernleistungen, dunkler Werkstatt-Slab, regionaler Pelletkreislauf, Tobias Müller Zitat und 4-Schritte Ablauf."
    },
    {
        "key": "leistungen",
        "id": None,
        "title": "NEU – Leistungen",
        "slug": "leistungen-neu",
        "prototype": "prototypes/leistungen_prototype.html",
        "desc": "Leistungsübersicht Hub (/leistungen/) mit 5 Disziplinen (Zimmerei, Treppenbau, Massivbau, Altbausanierung, Pellets) und Gewerke-Verbund-Vorteil."
    },
    {
        "key": "referenzen",
        "id": None,
        "title": "NEU – Referenzen",
        "slug": "referenzen-neu",
        "prototype": "prototypes/referenzen_prototype.html",
        "desc": "Projektgalerie mit Somerville Pill-Filter (Alle, Zimmerei, Treppenbau, Massivbau, Denkmalpflege) und 100% echten Fotografien."
    },
    {
        "key": "ueber-uns",
        "id": None,
        "title": "NEU – Über uns",
        "slug": "ueber-uns-neu",
        "prototype": "prototypes/ueberuns_prototype.html",
        "desc": "Über uns Seite mit 100+ Jahre Chronik (seit 1920), historischem Foto uberunssw.jpg, Werkstattrundgang und GRW-Infra Fördersignet."
    },
    {
        "key": "aktuelles",
        "id": None,
        "title": "NEU – Aktuelles",
        "slug": "aktuelles-neu",
        "prototype": "prototypes/aktuelles_prototype.html",
        "desc": "Magazin & Beitragsübersicht mit Filter-Pills, 6 echten Beiträgen, SAB/EU-Förderprojekt und Werkstatt-Meldungen."
    },
    {
        "key": "zimmerei-holzbau",
        "id": None,
        "title": "NEU – Zimmerei & Holzbau",
        "slug": "zimmerei-holzbau-neu",
        "prototype": "prototypes/zimmerei_prototype.html",
        "desc": "Einzelleistung Zimmerei & Holzbau mit Dachstuhlkonstruktionen, Werkstattabbund & Sägewerk Vorteil und Holzbau-FAQ."
    },
    {
        "key": "post-2496",
        "id": 2496,
        "title": "Werkstatt der Zukunft – Präzision trifft Tradition",
        "slug": "werkstatt-der-zukunft-praezision-trifft-tradition",
        "prototype": "prototypes/post_2496_prototype.html",
        "desc": "SAB/EFRE-Förderprojekt Einzelbeitrag im Somerville Design mit Fördersignet, 4 Maschinenkarten und Meisterzitat."
    }
]

for p in pages:
    with open(p["prototype"], "r", encoding="utf-8") as f:
        html = f.read()

    style_match = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
    style_content = style_match.group(1).strip() if style_match else ""

    # Replace fax number typo with real phone number
    html = html.replace("tel:03438143370", "tel:+493438143336")
    html = html.replace("034381 43370", "034381 43336")

    # Extract full body content preserving Somerville header, mobile drawer, sections and footer
    body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
    if body_match:
        body_content = body_match.group(1).strip()
    else:
        body_content = re.sub(r"</body>\s*</html>\s*$", "", html.strip())

    full_snippet = f"""<!-- SOMERVILLE ARCHITECTURAL CRAFT DESIGN: {p['title']} -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<style>
{style_content}
</style>

<div class="somerville-container w-full bg-[#F8F5EE] text-[#1A1918] antialiased" style="font-family: 'Inter', sans-serif;">
{body_content}
</div>
"""
    snippet_path = f"exports/html_snippets/{p['key']}.html"
    with open(snippet_path, "w", encoding="utf-8") as f:
        f.write(full_snippet)

    wp_payload = {
        "id": p["id"],
        "title": {
            "rendered": p["title"],
            "raw": p["title"]
        },
        "slug": p["slug"],
        "status": "draft",
        "type": "page",
        "template": "elementor_canvas",
        "comment_status": "closed",
        "ping_status": "closed",
        "content": {
            "rendered": full_snippet,
            "raw": full_snippet
        },
        "meta": {
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "ast-site-content-layout": "default",
            "site-sidebar-layout": "no-sidebar",
            "site-content-style": "unboxed",
            "site-sidebar-style": "unboxed",
            "ast-global-header-display": "",
            "theme-transparent-header-meta": "default"
        },
        "description": p["desc"]
    }

    json_path = f"exports/neu-{p['key']}.json"
    if p["id"] == 2595:
        json_path = "exports/neu-startseite-2595.json"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(wp_payload, f, indent=2, ensure_ascii=False)

    elem_template = {
        "version": "0.4",
        "title": p["title"],
        "type": "page",
        "page_settings": {
            "template": "elementor_canvas",
            "hide_title": "yes"
        },
        "content": [
            {
                "id": f"con_{p['key']}_root",
                "elType": "container",
                "isInner": False,
                "settings": {
                    "content_width": "full",
                    "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0"}
                },
                "elements": [
                    {
                        "id": f"html_{p['key']}",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": full_snippet
                        }
                    }
                ]
            }
        ]
    }
    template_path = f"exports/elementor_templates/{p['key']}.json"
    with open(template_path, "w", encoding="utf-8") as f:
        json.dump(elem_template, f, indent=2, ensure_ascii=False)

    print(f"✓ Generated: {json_path} & {template_path}")

print("All exports successfully written.")
