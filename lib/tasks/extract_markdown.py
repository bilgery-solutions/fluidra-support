import os
from pathlib import Path
import shutil

# Verzeichnisse definieren
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "_data"

# Vorherige Ausgabe löschen
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Alle Markdown-Dateien im Repo durchgehen
for md_file in REPO_ROOT.rglob("*.md"):
    # Nur Dateien innerhalb des Repos (nicht in .git, .github, output etc.)
    if any(part in md_file.parts for part in [".git", ".github", "output"]):
        continue

    # Zieldatei speichern
    rel_path = md_file.relative_to(REPO_ROOT)
    dest_file = OUTPUT_DIR / rel_path
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(md_file, dest_file)

print(f"✅ Exportiert: {len(list(OUTPUT_DIR.rglob('*.md')))} Markdown-Dateien.")
