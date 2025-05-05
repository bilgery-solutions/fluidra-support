from pathlib import Path

# Projektstruktur definieren
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "_data"
COMBINED_FILE = OUTPUT_DIR / "combined.md"

# Ausschlüsse definieren
EXCLUDED_DIRS = {".git", ".github", "_data", "_includes", "_layouts", "_saas", "assets"}
EXCLUDED_NAMES = {"readme.md", "index.md"}

# Zielordner erstellen, wenn nötig
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Alte Datei löschen, falls vorhanden
if COMBINED_FILE.exists():
    COMBINED_FILE.unlink()

# Markdown-Dateien sammeln und kombinieren
added_files = []
written_names = set()

with open(COMBINED_FILE, "w", encoding="utf-8") as outfile:
    for md_file in REPO_ROOT.rglob("*.md"):
        # Verzeichnisse ausschließen
        if any(part in EXCLUDED_DIRS for part in md_file.parts):
            continue

        # Bestimmte Dateinamen ignorieren
        if md_file.name.lower() in EXCLUDED_NAMES:
            continue

        base_name = md_file.name
        dest_name = base_name

        # Namenskonflikt: Ordnername voranstellen
        if dest_name in written_names:
            parent_name = md_file.parent.name
            dest_name = f"{parent_name}_{base_name}"

        # Abschnitt schreiben
        outfile.write(f"# File: {dest_name}\n\n")
        content = md_file.read_text(encoding="utf-8")
        outfile.write(content.strip() + "\n\n---\n\n")

        added_files.append(dest_name)
        written_names.add(dest_name)

# Zusammenfassung ausgeben
print(f"✅ Kombinierte Datei erstellt mit {len(added_files)} Markdown-Dateien:")
for name in added_files:
    print(" -", name)
