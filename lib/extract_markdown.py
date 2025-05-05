import os
from pathlib import Path
import shutil

# Basisverzeichnisse definieren
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "_data"

# Ordner neu anlegen
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

EXCLUDED_NAMES = {"readme.md", "index.md"}
exported_files = []

for md_file in REPO_ROOT.rglob("*.md"):
    # Ordner ausschließen
    if any(part in md_file.parts for part in [".git", ".github", "_data", "_includes", "_layouts", "_saas", "assets"]):
        continue

    # Exkludiere bestimmte Dateinamen (case-insensitive)
    if md_file.name.lower() in EXCLUDED_NAMES:
        continue

    base_name = md_file.name

    # Prüfen, ob es zu Namenskonflikten kommen kann
    dest_file = OUTPUT_DIR / base_name
    if dest_file.exists():
        # Übergeordneten Ordnernamen holen und mit Unterstrich prefixen
        parent_name = md_file.parent.name
        new_name = f"{parent_name}_{base_name}"
        dest_file = OUTPUT_DIR / new_name

    shutil.copy2(md_file, dest_file)
    exported_files.append(dest_file.name)

# Ausgabe
print(f"✅ {len(exported_files)} Markdown-Dateien exportiert:")
for f in sorted(exported_files):
    print(" -", f)
