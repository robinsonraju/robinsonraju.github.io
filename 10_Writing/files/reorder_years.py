#!/usr/bin/env python3
import os
import re
import argparse

# Navigate to 10_Writing folder
# Command to run: python3 files/reorder_years.py .
# Command for dry-run: python3 files/reorder_years.py . --dry-run

def reorder_year_folders(target_dir, dry_run=False):
    """
    Re-orders folders within target_dir that represent years (e.g. YYYY or XX_YYYY)
    in reverse chronological order by applying/updating numeric prefixes.
    """
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    # Get all entries in the directory
    entries = os.listdir(target_dir)
    # Filter for subdirectories
    dirs = [d for d in entries if os.path.isdir(os.path.join(target_dir, d))]
    
    # Identify folders that represent years.
    # We look for a 4-digit year at the end of the folder name.
    # Examples: '2024', '03_2024', 'old_2022'
    year_map = {} # year -> original_name
    for d in dirs:
        # Match YYYY at the end of the string
        match = re.search(r'(\d{4})$', d)
        if match:
            year = match.group(1)
            year_map[year] = d
            
    # Sort years in descending order (newest first)
    sorted_years = sorted(year_map.keys(), reverse=True)
    
    if not sorted_years:
        print("No year-based folders found.")
        return

    print(f"Found {len(sorted_years)} year folders. Re-ordering...")

    # Generate new names and perform renaming
    for i, year in enumerate(sorted_years):
        # Prefix is 1-indexed, padded to 2 digits (01, 02, etc.)
        prefix = f"{i+1:02d}_"
        new_name = f"{prefix}{year}"
        old_name = year_map[year]
        
        if old_name != new_name:
            source = os.path.join(target_dir, old_name)
            destination = os.path.join(target_dir, new_name)
            
            if dry_run:
                print(f"[DRY RUN] Would rename: '{old_name}' -> '{new_name}'")
            else:
                try:
                    os.rename(source, destination)
                    print(f"Renamed: '{old_name}' -> '{new_name}'")
                except Exception as e:
                    print(f"Error renaming '{old_name}': {e}")
        else:
            print(f"Skipping: '{old_name}' (already correct)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reorder year-based folders in reverse chronological order.")
    parser.add_argument("directory", nargs="?", default=".", help="The directory containing year folders (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without actually renaming folders")
    
    args = parser.parse_args()
    
    reorder_year_folders(args.directory, dry_run=args.dry_run)
