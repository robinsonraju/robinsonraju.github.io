#!/usr/bin/env python3
import os
import csv
import re
import zipfile
import shutil
from datetime import datetime
from pathlib import Path

"""
Substack to Quartz Migration Script (Final Teaser Version)

Logic:
1. Extracts the initial Quote (div.pullquote) if exists.
2. Extracts the first two meaningful paragraphs of content.
3. Removes header images and attributions.
4. Removes all automated wiki-linking.
5. Adds a prominent link back to the full Substack post.
"""

try:
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
    from dateutil import parser as date_parser
except ImportError:
    print("Missing dependencies. Please run: pip3 install beautifulsoup4 markdownify python-dateutil")
    exit(1)

def clean_filename(title):
    filename = re.sub(r'[\\/*?:"<>|]', "", title)
    return filename.strip()

def process_substack_export(zip_path, target_root):
    extract_dir = Path("substack_temp_extract")
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    posts_csv = extract_dir / "posts.csv"
    if not posts_csv.exists():
        print(f"Error: Could not find posts.csv in the export.")
        return

    target_root_path = Path(target_root)
    target_root_path.mkdir(parents=True, exist_ok=True)

    existing_dirs = [d for d in os.listdir(target_root) if os.path.isdir(os.path.join(target_root, d))]
    year_to_dir = {}
    for d in existing_dirs:
        match = re.search(r'(\d{4})$', d)
        if match:
            year_to_dir[match.group(1)] = d

    with open(posts_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('title')
            post_date_str = row.get('post_date')
            post_id = row.get('post_id')
            is_published = row.get('is_published', 'true').lower() == 'true'

            if not is_published:
                continue

            try:
                post_date = date_parser.parse(post_date_str)
            except Exception:
                continue

            year = str(post_date.year)
            date_prefix = post_date.strftime("%Y-%m-%d")
            
            if year in year_to_dir:
                year_subdir = target_root_path / year_to_dir[year]
            else:
                year_subdir = target_root_path / year
            
            year_subdir.mkdir(parents=True, exist_ok=True)

            potential_files = list((extract_dir / "posts").glob(f"{post_id}.*.html"))
            if not potential_files:
                potential_files = list((extract_dir / "posts").glob(f"{post_id}.html"))
            
            if potential_files:
                html_file = potential_files[0]
                parts = html_file.name.split('.')
                if len(parts) >= 3:
                   slug = ".".join(parts[1:-1])
                else:
                   slug = parts[0]
            else:
                print(f"Warning: Could not find HTML content for {title} (ID: {post_id})")
                continue

            # Process Teaser Migration
            with open(html_file, 'r', encoding='utf-8') as hf:
                html_content = hf.read()
                
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 1. Remove Header Image
            first_img = soup.find('img')
            if first_img:
                first_img.decompose()
            
            # 2. Extract Teaser Content
            teaser_elements = []
            
            # Try to find the pullquote (initial quote)
            pullquote = soup.find("div", class_="pullquote")
            if pullquote:
                teaser_elements.append(md(str(pullquote), heading_style="ATX"))
                # Remove it so we don't pick up its paragraphs again
                pullquote.decompose()
            
            # Pick first 2 paragraphs with actual text
            paragraphs = soup.find_all("p")
            count = 0
            for p in paragraphs:
                if count >= 2:
                    break
                # Ensure it's not empty or just whitespace
                if p.get_text(strip=True):
                    teaser_elements.append(md(str(p), heading_style="ATX"))
                    count += 1

            teaser_body = "\n\n".join(teaser_elements)

            # 3. Clean up Image Attributions
            attribution_pattern = re.compile(r'Photo by \[.*?\]\(.*?\) on \[.*?\]\(.*?\)', re.IGNORECASE)
            teaser_body = attribution_pattern.sub('', teaser_body)
            attribution_pattern_2 = re.compile(r'Photo by .* on Unsplash', re.IGNORECASE)
            teaser_body = attribution_pattern_2.sub('', teaser_body)

            # 4. Add Substack URL
            substack_url = f"https://www.readgreatbooks.info/p/{slug}"
            teaser_body += f"\n\n---\n\n[Read the full post on Substack]({substack_url})"

            # Create frontmatter
            frontmatter = f"---\ntitle: \"{title}\"\ndate: {date_prefix}\ntags:\n  - newsletter\n---\n\n"
            
            safe_title = clean_filename(title)
            output_filename = f"{date_prefix} - {safe_title}.md"
            output_path = year_subdir / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write(frontmatter)
                out_f.write(teaser_body)
            
            print(f"Updated (Teaser): {output_path}")

    shutil.rmtree(extract_dir)
    print("\nTeaser migration complete!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 import_substack.py /path/to/substack_export.zip")
        sys.exit(1)
    
    zap_path = sys.argv[1]
    target_root = "content/10_Writing"
    process_substack_export(zap_path, target_root)
