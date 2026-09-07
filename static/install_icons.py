#!/usr/bin/env python3
"""
Architecture Icon Pack V1 installer.
This installs the bundled generic SVG fallback set and validates mappings.
Official vendor artwork is NOT redistributed in this package. Use the README
and OFFICIAL_SOURCES.md to obtain approved AWS/Azure/GCP assets, then replace
the matching files while keeping filenames unchanged.
"""
import json, shutil, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
TARGET=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
STATIC=TARGET/"static"
ICONS=STATIC/"icons"

if not STATIC.exists():
    print(f"ERROR: {STATIC} does not exist.")
    print("Usage: python install_icons.py /path/to/project")
    raise SystemExit(1)

src=HERE/"icons"
ICONS.mkdir(parents=True,exist_ok=True)
count=0
for f in src.rglob("*.svg"):
    rel=f.relative_to(src)
    dest=ICONS/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists():
        shutil.copy2(f,dest); count+=1

registry_source = HERE / "icon_registry.json"
registry_target = STATIC / "icon_registry.json"

try:
    shutil.copy2(registry_source, registry_target)
    print(f"Registry installed: {registry_target}")
except PermissionError:
    print()
    print("WARNING: Could not replace icon_registry.json")
    print(f"The file is currently being used: {registry_target}")
    print()
    print("The icon files were installed successfully.")
    print("Stop the application and manually copy icon_registry.json later.")
print(f"Installed {count} icon files.")
print(f"Registry: {STATIC/'icon_registry.json'}")
print("Next: replace selected generic SVGs with official vendor assets using the SAME filenames.")
