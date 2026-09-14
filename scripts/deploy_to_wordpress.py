#!/usr/bin/env python3
"""
deploy_to_wordpress.py
Automated script to sync prepared Somerville draft pages to WordPress (bau-mueller.eu).
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DEFAULT_WP_URL = "https://bau-mueller.eu"

PAGE_SPECS = [
    {
        "key": "startseite",
        "existing_id": 2595,
        "title": "NEU – Startseite",
        "slug": "startseite-neu",
        "file": "exports/neu-startseite-2595.json"
    },
    {
        "key": "leistungen",
        "existing_id": None,
        "title": "NEU – Leistungen",
        "slug": "leistungen-neu",
        "file": "exports/neu-leistungen.json"
    },
    {
        "key": "referenzen",
        "existing_id": None,
        "title": "NEU – Referenzen",
        "slug": "referenzen-neu",
        "file": "exports/neu-referenzen.json"
    },
    {
        "key": "ueber-uns",
        "existing_id": None,
        "title": "NEU – Über uns",
        "slug": "ueber-uns-neu",
        "file": "exports/neu-ueber-uns.json"
    },
    {
        "key": "zimmerei-holzbau",
        "existing_id": None,
        "title": "NEU – Zimmerei & Holzbau",
        "slug": "zimmerei-holzbau-neu",
        "file": "exports/neu-zimmerei-holzbau.json"
    }
]

def load_env_file():
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip("'").strip('"')
    return env_vars

def make_request(url, auth_header, data=None, method="GET"):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", auth_header)
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "BauMuellerRelaunchDeployer/1.0")

    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")

    try:
        with urllib.request.urlopen(req, data=body, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            return json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"[ERROR] HTTP {e.code} for {method} {url}")
        print(f"Server response: {err_body}")
        raise
    except Exception as e:
        print(f"[ERROR] Request failed: {e}")
        raise

def find_existing_page(wp_url, auth_header, title):
    encoded_title = urllib.parse.quote(title)
    url = f"{wp_url}/wp-json/wp/v2/pages?search={encoded_title}&status=draft,publish,private,pending"
    results = make_request(url, auth_header)
    for p in results:
        if p.get("title", {}).get("rendered") == title or p.get("title", {}).get("raw") == title:
            return p.get("id")
    return None

def main():
    parser = argparse.ArgumentParser(description="Deploy Somerville draft pages to WordPress")
    parser.add_argument("--url", default=None, help=f"WordPress Base URL (default: {DEFAULT_WP_URL})")
    parser.add_argument("--user", default=None, help="WordPress Admin Username")
    parser.add_argument("--password", default=None, help="WordPress Application Password")
    parser.add_argument("--dry-run", action="store_true", help="Simulate deployment without modifying WordPress")
    args = parser.parse_args()

    env_vars = load_env_file()
    wp_url = (args.url or env_vars.get("WP_URL") or DEFAULT_WP_URL).rstrip("/")
    wp_user = args.user or env_vars.get("WP_USER") or os.environ.get("WP_USER")
    wp_pass = args.password or env_vars.get("WP_APP_PASSWORD") or env_vars.get("WP_PASSWORD") or os.environ.get("WP_APP_PASSWORD")

    if not wp_user or not wp_pass:
        print("=" * 70)
        print("FEHLENDE ZUGANGSDATEN:")
        print("Bitte geben Sie die Zugangsdaten als Argumente an:")
        print("  python3 scripts/deploy_to_wordpress.py --user <User> --password <App-Passwort>")
        print("oder erstellen Sie eine .env-Datei mit:")
        print("  WP_USER=IhrBenutzername")
        print("  WP_APP_PASSWORD=xxxx xxxx xxxx xxxx")
        print("=" * 70)
        sys.exit(1)

    auth_str = f"{wp_user}:{wp_pass}"
    auth_header = "Basic " + base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    print(f"Verbinde mit WordPress: {wp_url} als Benutzer: {wp_user}...")
    try:
        me = make_request(f"{wp_url}/wp-json/wp/v2/users/me", auth_header)
        print(f"✓ Authentifizierung erfolgreich! Angemeldet als: {me.get('name')} (ID: {me.get('id')})")
    except Exception as e:
        print(f"[FATAL] Authentifizierung fehlgeschlagen: {e}")
        sys.exit(1)

    print("\nStarte Übertragung der Seiten im Somerville Architectural Craft Design...\n")

    summary = []
    for spec in PAGE_SPECS:
        key = spec["key"]
        title = spec["title"]
        file_path = spec["file"]

        if not os.path.exists(file_path):
            print(f"[WARN] Datei {file_path} nicht gefunden, überspringe...")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            payload = json.load(f)

        target_id = spec["existing_id"]
        if not target_id:
            target_id = find_existing_page(wp_url, auth_header, title)

        data = {
            "title": title,
            "status": "draft",
            "content": payload["content"]["raw"],
            "template": payload.get("template", "elementor_header_footer"),
            "comment_status": "closed",
            "ping_status": "closed",
            "meta": payload.get("meta", {})
        }

        if args.dry_run:
            print(f"[DRY-RUN] Würde Seite '{title}' (ID: {target_id or 'NEU'}) aktualisieren/anlegen.")
            continue

        if target_id:
            # Update existing page
            url = f"{wp_url}/wp-json/wp/v2/pages/{target_id}"
            print(f"Aktualisiere Entwurf: '{title}' (ID: {target_id})...")
            res = make_request(url, auth_header, data=data, method="POST")
            page_id = res.get("id", target_id)
            edit_link = f"{wp_url}/wp-admin/post.php?post={page_id}&action=edit"
            elementor_link = f"{wp_url}/wp-admin/post.php?post={page_id}&action=elementor"
            preview_link = f"{wp_url}/?page_id={page_id}&preview=true"
            print(f"✓ Aktualisiert: ID {page_id}")
            summary.append({"title": title, "id": page_id, "action": "Aktualisiert", "edit": edit_link, "elementor": elementor_link, "preview": preview_link})
        else:
            # Create new page
            url = f"{wp_url}/wp-json/wp/v2/pages"
            print(f"Erstelle neuen Entwurf: '{title}'...")
            res = make_request(url, auth_header, data=data, method="POST")
            page_id = res.get("id")
            edit_link = f"{wp_url}/wp-admin/post.php?post={page_id}&action=edit"
            elementor_link = f"{wp_url}/wp-admin/post.php?post={page_id}&action=elementor"
            preview_link = f"{wp_url}/?page_id={page_id}&preview=true"
            print(f"✓ Neu angelegt: ID {page_id}")
            summary.append({"title": title, "id": page_id, "action": "Neu angelegt", "edit": edit_link, "elementor": elementor_link, "preview": preview_link})

    print("\n" + "=" * 70)
    print("ÜBERTRAGUNG ERFOLGREICH ABGESCHLOSSEN!")
    print("=" * 70)
    for s in summary:
        print(f"• {s['title']} (ID: {s['id']} - {s['action']})")
        print(f"  Gutenberg/WP: {s['edit']}")
        print(f"  Elementor:    {s['elementor']}")
        print(f"  Vorschau:     {s['preview']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
