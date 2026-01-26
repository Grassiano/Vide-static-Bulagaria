#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Base directory
base_dir = Path("public/videprints.com")

# Files to process
html_files = list(base_dir.rglob("*.html"))

def fix_faq_links(content, file_path):
    """Fix all FAQ-related links"""
    original = content
    
    # Fix footer links: Replace "Галерия" links to collections/all with "ЧЗВ" links to FAQ
    # Pattern: <a href="../../collections/all/" ...>Галерия</a>
    content = re.sub(
        r'<a href="([^"]*collections/all/)"[^>]*class="[^"]*reversed-link[^"]*"[^>]*>Галерия</a>',
        lambda m: f'<a href="{m.group(1).replace("collections/all/", "pages/שאלות-תשובות/")}" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
        content
    )
    
    # Fix relative paths for FAQ links in footers
    # For files in pages/*, use ../שאלות-תשובות/
    # For files in root, use pages/שאלות-תשובות/
    # For files in collections/*, use ../../pages/שאלות-תשובות/
    
    # Fix empty href with "Галерия" text
    content = re.sub(
        r'<a href\s+class="[^"]*reversed-link[^"]*"[^>]*>Галерия</a>',
        lambda m: f'<a href="../שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
        content
    )
    
    # Fix index.html footer link
    if "index.html" in str(file_path) and file_path.name == "index.html":
        content = re.sub(
            r'<a href="collections/all/"\s+class="block reversed-link text-sm-lg leading-tight">Галерия</a>',
            '<a href="pages/שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
            content
        )
    
    # Fix collections/all/index.html footer link
    if "collections/all" in str(file_path):
        content = re.sub(
            r'<a href="../../collections/all/"\s+class="block reversed-link text-sm-lg leading-tight">Галерия</a>',
            '<a href="../../pages/שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
            content
        )
    
    # Fix pages/* footer links
    if "/pages/" in str(file_path):
        content = re.sub(
            r'<a href="../../collections/all/"\s+class="block reversed-link text-sm-lg leading-tight">Галерия</a>',
            '<a href="../שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
            content
        )
    
    # Fix cart and search footer links (they're in root level)
    if "cart" in str(file_path) or "search" in str(file_path):
        content = re.sub(
            r'<a href="[^"]*שאלות-תשובות/[^"]*"\s+class="block reversed-link text-sm-lg leading-tight">Галерия</a>',
            '<a href="../pages/שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
            content
        )
    
    # Fix policies footer links
    if "/policies/" in str(file_path):
        content = re.sub(
            r'<a href="../../collections/all/"\s+class="block reversed-link text-sm-lg leading-tight">Галерия</a>',
            '<a href="../../pages/שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>',
            content
        )
    
    return content

# Process all HTML files
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_faq_links(content, html_file)
        
        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {html_file}")
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

print("Done fixing FAQ links!")
