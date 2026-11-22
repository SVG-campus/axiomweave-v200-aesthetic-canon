import os
import json
import html

WORKSPACE = r"C:\Users\svillalobosgonzalez1\.gemini\antigravity\scratch\v200_universal_canon_web"
DATA_DIR = os.path.join(WORKSPACE, "data")

print("[1/5] Loading datasets...")
with open(os.path.join(DATA_DIR, "cars_manifest.json"), "r", encoding="utf-8") as f:
    cars_data = json.load(f)
with open(os.path.join(DATA_DIR, "aviation_manifest.json"), "r", encoding="utf-8") as f:
    aviation_data = json.load(f)
with open(os.path.join(DATA_DIR, "music_manifest.json"), "r", encoding="utf-8") as f:
    music_data = json.load(f)
with open(os.path.join(DATA_DIR, "poetry_manifest.json"), "r", encoding="utf-8") as f:
    poetry_data = json.load(f)
with open(os.path.join(DATA_DIR, "synthesis_manifest.json"), "r", encoding="utf-8") as f:
    synthesis_data = json.load(f)

print(f"Loaded {len(cars_data['cars'])} cars, {len(aviation_data['aircraft'])} aircraft, {len(music_data['works'])} music, {len(poetry_data['poems'])} poems, {len(synthesis_data['lines'])} synthesized lines.")
