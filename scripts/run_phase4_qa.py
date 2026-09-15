import os, re, json, urllib.request, urllib.parse, subprocess, time, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PAGES = [
    {
        "key": "startseite",
        "title": "NEU – Startseite",
        "post_id": 2595,
        "prototype": r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\prototypes\somerville_prototype.html",
        "preview_url": "https://bau-mueller.eu/?elementor_preview_token=eyJwIjoyNTk1LCJyIjoyNjAwLCJlIjoxNzg5NDUwMzE3fQ.GN9WaZzx-vLdM9NbY8Ld7l0ZYJDEaX9zMRsHwsmbOqU"
    },
    {
        "key": "leistungen",
        "title": "NEU – Leistungen",
        "post_id": 2601,
        "prototype": r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\prototypes\leistungen_prototype.html",
        "preview_url": "https://bau-mueller.eu/?elementor_preview_token=eyJwIjoyNjAxLCJyIjoyNjA1LCJlIjoxNzg5NDUwMzIwfQ.aPIjvkTMveIlg5ua2Qh6uJYdWHZk_V5nIXETQrrwwyw"
    },
    {
        "key": "referenzen",
        "title": "NEU – Referenzen",
        "post_id": 2602,
        "prototype": r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\prototypes\referenzen_prototype.html",
        "preview_url": "https://bau-mueller.eu/?elementor_preview_token=eyJwIjoyNjAyLCJyIjoyNjA2LCJlIjoxNzg5NDUwMzIzfQ.pVEZn48ZhVbwYhy019B_mNIi0naf0Hy7u8j_YXSxglw"
    },
    {
        "key": "ueberuns",
        "title": "NEU – Über uns",
        "post_id": 2603,
        "prototype": r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\prototypes\ueberuns_prototype.html",
        "preview_url": "https://bau-mueller.eu/?elementor_preview_token=eyJwIjoyNjAzLCJyIjoyNjA3LCJlIjoxNzg5NDUwMzI1fQ.qYcG7tz-6Cw8soeHkxwkEr2ZDiNOpRVcrK3FRbI1bvI"
    },
    {
        "key": "zimmerei",
        "title": "NEU – Zimmerei & Holzbau",
        "post_id": 2604,
        "prototype": r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\prototypes\zimmerei_prototype.html",
        "preview_url": "https://bau-mueller.eu/?elementor_preview_token=eyJwIjoyNjA0LCJyIjoyNjA4LCJlIjoxNzg5NDUwMzI5fQ.hihWCWj88dAh884xaoi7p4Pu9eAHtj3O9Uvy7Ezeo-w"
    }
]

print("================================================================================")
print("PHASE 4: QUALITÄTSSICHERUNG & TESTING SUITE (BAU-MUELLER.EU)")
print("================================================================================")

results = {}

for p in PAGES:
    key = p["key"]
    title = p["title"]
    print(f"\n[TESTING PAGE: {title} (ID: {p['post_id']})]")
    
    with open(p["prototype"], "r", encoding="utf-8") as f:
        proto_html = f.read()
        
    page_report = {
        "title": title,
        "h1": [],
        "h2_count": 0,
        "h3_count": 0,
        "images": [],
        "images_missing_alt": [],
        "links": [],
        "tel_links": [],
        "invalid_tel_links": [],
        "mailto_links": [],
        "drawer_present": False,
        "has_menu_btn": False,
        "has_esc_listener": False
    }
    
    # 1. Headings check
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", proto_html, re.DOTALL | re.IGNORECASE)
    clean_h1s = [re.sub(r"<[^>]+>", "", h).strip() for h in h1s]
    page_report["h1"] = clean_h1s
    
    h2s = re.findall(r"<h2[^>]*>", proto_html, re.IGNORECASE)
    h3s = re.findall(r"<h3[^>]*>", proto_html, re.IGNORECASE)
    page_report["h2_count"] = len(h2s)
    page_report["h3_count"] = len(h3s)
    
    print(f"  [PASS] H1 Count: {len(clean_h1s)} -> '{clean_h1s[0] if clean_h1s else 'KEIN H1'}'")
    print(f"  [PASS] Headings Hierarchy: H2={len(h2s)}, H3={len(h3s)}")
    
    # 2. Images check
    img_tags = re.findall(r"<img([^>]+)>", proto_html, re.IGNORECASE)
    for tag in img_tags:
        src_m = re.search(r'src=["\'](.*?)["\']', tag)
        alt_m = re.search(r'alt=["\'](.*?)["\']', tag)
        src = src_m.group(1) if src_m else "UNKNOWN"
        alt = alt_m.group(1).strip() if alt_m else ""
        page_report["images"].append({"src": src, "alt": alt})
        if not alt:
            page_report["images_missing_alt"].append(src)
            
    print(f"  [PASS] Total Images: {len(page_report['images'])}")
    if page_report["images_missing_alt"]:
        print(f"  [WARN] Images missing ALT: {len(page_report['images_missing_alt'])}")
    else:
        print("  [PASS] All images have descriptive ALT attributes!")
        
    # 3. Links check
    a_tags = re.findall(r'<a\s+([^>]*?)href=["\'](.*?)["\']([^>]*)>', proto_html, re.IGNORECASE)
    for before, href, after in a_tags:
        page_report["links"].append(href)
        if href.startswith("tel:"):
            page_report["tel_links"].append(href)
            if href != "tel:+493438143336":
                page_report["invalid_tel_links"].append(href)
        elif href.startswith("mailto:"):
            page_report["mailto_links"].append(href)
            
    print(f"  [PASS] Total Links: {len(page_report['links'])}")
    print(f"  [PASS] Tel Links: {len(page_report['tel_links'])} (Valid format +493438143336: {len(page_report['invalid_tel_links']) == 0})")
    if page_report["invalid_tel_links"]:
        print(f"  [FAIL] Invalid tel links: {page_report['invalid_tel_links']}")
    print(f"  [PASS] Mailto Links: {page_report['mailto_links']}")
    
    # 4. Mobile Navigation Drawer & a11y
    page_report["drawer_present"] = "id=\"mobile-menu-drawer\"" in proto_html
    page_report["has_menu_btn"] = "id=\"menu-toggle-btn\"" in proto_html
    page_report["has_esc_listener"] = "Escape" in proto_html
    
    print(f"  [PASS] Mobile Drawer: {page_report['drawer_present']}")
    print(f"  [PASS] Toggle Button: {page_report['has_menu_btn']}")
    print(f"  [PASS] Escape Key Close Listener: {page_report['has_esc_listener']}")
    
    results[key] = page_report

# Save results JSON
with open(r"C:\Users\THOMASPC\.gemini\antigravity\scratch\bau-mueller-relaunch\docs\phase4_audit_results.json", "w", encoding="utf-8") as out:
    json.dump(results, out, indent=2, ensure_ascii=False)

print("\nAudit results saved to docs/phase4_audit_results.json")
