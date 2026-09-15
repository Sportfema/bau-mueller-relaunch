#!/usr/bin/env python3
"""
backup_live_pages.py
Creates full JSON snapshots of all original WordPress live pages before relaunch.
"""

import urllib.request
import json
import base64
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

auth = base64.b64encode(b'Tobias:LSZ3 zu9l qA3n Zygr 42We nEir').decode('utf-8')
headers = {'Authorization': f'Basic {auth}', 'User-Agent': 'Mozilla/5.0'}

base_dir = os.path.join(os.path.dirname(__file__), '..', 'backups', 'live_pages_original')
os.makedirs(base_dir, exist_ok=True)

live_page_ids = [540, 541, 542, 7, 543, 2012, 802, 810]

print('=== BACKING UP LIVE PAGES BEFORE RELAUNCH ===')
for pid in live_page_ids:
    url = f'https://bau-mueller.eu/wp-json/wp/v2/pages/{pid}?context=edit'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', {}).get('raw', data.get('title', {}).get('rendered', ''))
            slug = data.get('slug', 'page')
            filename = os.path.join(base_dir, f'page_{pid}_{slug}.json')
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Backed up Page {pid} ('{title}') -> {filename}")
    except Exception as e:
        print(f"Failed to backup {pid}: {e}")

print('\nBackup completed successfully!')
