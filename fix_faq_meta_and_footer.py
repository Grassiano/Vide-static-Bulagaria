#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Base directory
base_dir = Path("public/videprints.com")

# Fix FAQ page meta tags
faq_file = base_dir / "pages" / "שאלות-תשובות" / "index.html"

if faq_file.exists():
    with open(faq_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix title and meta tags
    content = content.replace('<title>Галерия &ndash; VIDE Bulgaria</title>', '<title>ЧЗВ &ndash; VIDE Bulgaria</title>')
    content = content.replace('<meta property="og:title" content="Галерия">', '<meta property="og:title" content="ЧЗВ">')
    content = content.replace('<meta name="twitter:title" content="Галерия">', '<meta name="twitter:title" content="ЧЗВ">')
    content = re.sub(
        r'<meta name="description" content="[^"]*Галерия[^"]*">',
        '<meta name="description" content="Често задавани въпроси и отговори за услугите на VIDE Bulgaria.">',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content="[^"]*Галерия[^"]*">',
        '<meta property="og:description" content="Често задавани въпроси и отговори за услугите на VIDE Bulgaria.">',
        content
    )
    content = re.sub(
        r'<meta name="twitter:description" content="[^"]*Галерия[^"]*">',
        '<meta name="twitter:description" content="Често задавани въпроси и отговори за услугите на VIDE Bulgaria.">',
        content
    )
    
    with open(faq_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed FAQ page meta tags: {faq_file}")

# Fix footer links that say "Галерия" but link to FAQ
files_to_fix = [
    base_dir / "cart" / "index.html",
    base_dir / "search" / "index.html",
    base_dir / "pages" / "תקנון-הגרלה" / "index.html",
]

for file_path in files_to_fix:
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix footer links: Replace "Галерия" text with "ЧЗВ" when linking to FAQ
        content = re.sub(
            r'<a href="[^"]*שאלות-תשובות[^"]*"[^>]*class="[^"]*reversed-link[^"]*"[^>]*>Галерия</a>',
            lambda m: m.group(0).replace('>Галерия</a>', '>ЧЗВ</a>'),
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed footer links: {file_path}")

print("Done fixing FAQ meta tags and footer links!")
