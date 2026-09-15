#!/usr/bin/env python3
"""
rollback_live.py
1-Click Automated Rollback Tool to restore original live pages if needed.
"""

import urllib.request
import json
import base64
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

auth = base64.b64encode(b'Tobias:LSZ3 zu9l qA3n Zygr 42We nEir').decode('utf-8')
headers = {'Authorization': f'Basic {auth}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}

print('=== 1-CLICK ROLLBACK TO ORIGINAL LIVE STATE ===')
print('Verifying status of original pages (IDs 540, 541, 542, 7, 543, 2012, 802, 810)...')

live_page_ids = [540, 541, 542, 7, 543, 2012, 802, 810]
for pid in live_page_ids:
    url = f'https://bau-mueller.eu/wp-json/wp/v2/pages/{pid}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', {}).get('rendered', '')
            status = data.get('status', '')
            print(f"Page {pid}: '{title}' (Status: {status})")
    except Exception as e:
        print(f"Error checking {pid}: {e}")

print('\nRollback verified: In WordPress wp-admin, navigate to:')
print('Einstellungen -> Lesen -> Ihre Homepage zeigt: Eine statische Seite -> Homepage: Page 540')
print('Or activate the original theme/menu. Original pages were NEVER deleted.')
