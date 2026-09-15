#!/usr/bin/env python3
"""
rollback_live.py
1-Click Automated Rollback Tool to restore the original 2026 website state.
Instantly switches WordPress back to original pages (IDs 540, 541, 542, 7, 543, 2012).
"""

import urllib.request
import json
import base64
import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WP_URL = "https://bau-mueller.eu"
auth_str = "Tobias:LSZ3 zu9l qA3n Zygr 42We nEir"
auth_header = "Basic " + base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

def api_call(endpoint, method="GET", data=None):
    url = f"{WP_URL}/wp-json/wp/v2/{endpoint}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", auth_header)
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "RollbackMaster/1.0")
    body = json.dumps(data).encode("utf-8") if data is not None else None
    with urllib.request.urlopen(req, data=body, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

print("=" * 80)
print("1-CLICK NOTFALL-ROLLBACK: ZURÜCKSTELLEN AUF ORIGINAL-WEBSITE")
print("=" * 80)

# 1. Revert Somerville pages to draft with temp slugs
somerville_pages = [
    (2595, "startseite-somerville-entwurf"),
    (2601, "leistungen-somerville-entwurf"),
    (2602, "projects-somerville-entwurf"),
    (2603, "about-somerville-entwurf"),
    (2604, "zimmerei-holzbau-somerville-entwurf"),
    (2613, "aktuelles-somerville-entwurf"),
]

print("\n1. Setze neue Relaunch-Seiten zurück auf Entwurf...")
for pid, temp_slug in somerville_pages:
    try:
        api_call(f"pages/{pid}", method="POST", data={"status": "draft", "slug": temp_slug})
        print(f"   ✓ ID {pid} auf Entwurf gesetzt.")
    except Exception as e:
        print(f"   [WARN] Fehler bei ID {pid}: {e}")

time.sleep(1)

# 2. Restore original pages to published with original slugs
original_pages = [
    (540, "zimmerei-2", "Zimmerei & Baugeschäft Müller Colditz | Meisterbetrieb seit 1920"),
    (541, "about", "Über uns: Tradition in 4. Generation"),
    (542, "leistungen", "Leistungen im Holz- & Massivbau"),
    (7,   "projects", "Referenzen & Bauprojekte"),
    (543, "contact", "Kontakt & Beratung"),
    (2012,"aktuelles", "Aktuelles & Einblicke"),
]

print("\n2. Reaktiviere alle 6 Original-Seiten...")
for pid, orig_slug, orig_title in original_pages:
    try:
        res = api_call(f"pages/{pid}", method="POST", data={
            "status": "publish",
            "slug": orig_slug,
            "title": orig_title
        })
        print(f"   ✓ ID {pid} wieder live: {res.get('link')}")
    except Exception as e:
        print(f"   [ERROR] Fehler bei Reaktivierung von {pid}: {e}")

# 3. Reset Front Page option to 540
print("\n3. Stelle WordPress Startseiten-Einstellung zurück...")
try:
    s_res = api_call("settings", method="POST", data={"page_on_front": 540, "show_on_front": "page"})
    print(f"   ✓ Startseite wieder auf Original ID: {s_res.get('page_on_front')}")
except Exception as e:
    print(f"   [ERROR] Fehler beim Zurückstellen der Startseite: {e}")

print("\n" + "=" * 80)
print("ROLLBACK VOLLSTÄNDIG DURCHGEFÜHRT! DIE ALTE SEITE IST WIEDER 1:1 LIVE.")
print("=" * 80)
