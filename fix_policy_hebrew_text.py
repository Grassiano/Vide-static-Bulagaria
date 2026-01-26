#!/usr/bin/env python3
import re
from pathlib import Path

# Policy files to fix
policy_files = [
    Path("public/videprints.com/policies/terms-of-service/index.html"),
    Path("public/videprints.com/policies/privacy-policy/index.html"),
]

# Bulgarian translations
translations = {
    "cookie_title": "Ние обичаме и използваме бисквитки",
    "cookie_text": "Най-много обичаме орао<br>и всъщност събираме информация от сърфирането в сайта, за да подобрим вашето изживяване.",
    "accept_cookies": "Приемане на бисквитки",
    "decline": "Отказ",
    "home": "Начало",
    "menu": "Меню",
    "shop": "Галерия",
    "navigation": "Навигация",
    "close": "Затвори"
}

def fix_hebrew_text(file_path):
    """Fix all remaining Hebrew text in policy pages"""
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix cookie banner
    content = content.replace('אנחנו אוהבים ומשתמשים בעוגיות', translations["cookie_title"])
    content = content.replace('הכי אוהבים אוראו<br>ותכלס אנחנו אוספים מידע מהגלישה באתר כדי לשפר את החוויה שלכם.', translations["cookie_text"])
    content = content.replace('אישור עוגיות', translations["accept_cookies"])
    content = content.replace('ביטול', translations["decline"])
    
    # Fix mobile dock
    content = content.replace('>בית</span>', f'>{translations["home"]}</span>')
    content = content.replace('>תפריט</span>', f'>{translations["menu"]}</span>')
    content = content.replace('>חנות</span>', f'>{translations["shop"]}</span>')
    
    # Fix navigation aria-label
    content = content.replace('aria-label="סגור"', f'aria-label="{translations["close"]}"')
    content = content.replace('>ניווט באתר</span>', f'>{translations["navigation"]}</span>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed Hebrew text in {file_path}")

# Fix both policy pages
for policy_file in policy_files:
    fix_hebrew_text(policy_file)

print("Done fixing Hebrew text in policy pages!")
