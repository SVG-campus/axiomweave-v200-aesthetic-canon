import os
import json

WORKSPACE = r"C:\Users\svillalobosgonzalez1\.gemini\antigravity\scratch\v200_universal_canon_web"
with open(os.path.join(WORKSPACE, "syllabus_data.json"), "r", encoding="utf-8") as f:
    SYLLABUS = json.load(f)

syllabus_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AxiomWeave v200.0 Apex | Master Academic & Literary Syllabus</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

  <style>
    :root {
      --bg-void: #06080e;
      --bg-surface: #0c101a;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(230, 175, 46, 0.35);
      --gold-primary: #e6af2e;
      --gold-light: #f5d47a;
      --cyan-accent: #38bdf8;
      --emerald-accent: #34d399;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --font-display: 'Cinzel', serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-void);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.6;
      padding: 2rem 1.5rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    header {
      border-bottom: 1px solid var(--border-gold);
      padding-bottom: 2rem;
      margin-bottom: 2.5rem;
      text-align: center;
    }
    .back-nav {
      text-align: left;
      margin-bottom: 1.5rem;
    }
    .back-nav a {
      color: var(--gold-primary);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }
    .title {
      font-family: var(--font-display);
      font-size: 2.4rem;
      font-weight: 900;
      color: var(--gold-primary);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }
    .subtitle {
      font-size: 1.1rem;
      color: var(--text-muted);
      max-width: 800px;
      margin: 0 auto;
    }

    .section-title {
      font-family: var(--font-display);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--gold-primary);
      margin: 2.5rem 0 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .item-card {
      background: rgba(16, 22, 36, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }
    .item-card:hover {
      border-color: rgba(230, 175, 46, 0.35);
    }
    .item-title {
      font-family: var(--font-display);
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.25rem;
    }
    .item-meta {
      font-size: 0.85rem;
      color: var(--gold-light);
      margin-bottom: 0.6rem;
      font-family: var(--font-mono);
    }
    .item-desc {
      font-size: 0.88rem;
      color: #cbd5e1;
      margin-bottom: 0.85rem;
      line-height: 1.5;
    }
    .item-edition {
      font-size: 0.8rem;
      color: var(--text-dim);
      background: rgba(0, 0, 0, 0.3);
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.85rem;
    }

    .links-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .btn-link {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 0.3rem 0.65rem;
      border-radius: 4px;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }
    .btn-jstor {
      background: rgba(230, 175, 46, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
    }
    .btn-primary {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--cyan-accent);
    }
    .btn-buy {
      background: rgba(52, 211, 153, 0.12);
      border: 1px solid rgba(52, 211, 153, 0.3);
      color: var(--emerald-accent);
    }
  </style>
</head>
<body>
  <div class="back-nav">
    <a href="index.html">&larr; Return to Universal Canon Portal</a>
  </div>

  <header>
    <h1 class="title">The Master Academic Syllabus</h1>
    <p class="subtitle">An exhaustive curriculum of all literary titans, prosodic theories, psychoacoustic physics, transonic aerodynamics, multi-body kinematics, and mathematical engines required for complete mastery.</p>
  </header>

  <!-- PART 1: LITERARY TITANS -->
  <h2 class="section-title">📖 I. The 22 Primary Literary Titans</h2>
  <div id="titans-list"></div>

  <!-- PART 2: LINGUISTICS & PROSODY -->
  <h2 class="section-title">🔤 II. Linguistics, Metrics & Cognitive Semiotics</h2>
  <div id="linguistics-list"></div>

  <!-- PART 3: MUSICOLOGY & ACOUSTIC PHYSICS -->
  <h2 class="section-title">🎼 III. Musicology, Psychoacoustics & Acoustic Physics</h2>
  <div id="musicology-list"></div>

  <!-- PART 4: AERODYNAMICS & PROPULSION -->
  <h2 class="section-title">✈️ IV. Aerodynamics, Fluid Dynamics & Propulsion Physics</h2>
  <div id="aero-list"></div>

  <!-- PART 5: VEHICLE DYNAMICS -->
  <h2 class="section-title">🏎️ V. Vehicle Dynamics, Kinematics & High-Performance Powertrains</h2>
  <div id="vehicle-list"></div>

  <!-- PART 6: MATHEMATICAL ENGINES -->
  <h2 class="section-title">🔬 VI. The 6 AxiomWeave Mathematical Engines & Commingling</h2>
  <div id="math-list"></div>

  <script>
    const S = __DATA_SYLLABUS__;

    document.getElementById('titans-list').innerHTML = S.literary_titans.map(t => `
      <div class="item-card">
        <div class="item-title">${t.work}</div>
        <div class="item-meta">${t.author} (${t.year}) &bull; ${t.lang} &bull; Form: ${t.form}</div>
        <div class="item-desc">${t.significance}</div>
        <div class="item-edition"><b>Definitive Edition:</b> ${t.scholarly_edition}</div>
        <div class="links-row">
          <a href="${t.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ JSTOR Research</a>
          <a href="${t.gutenberg_url}" target="_blank" class="btn-link btn-primary">📜 Primary Gutenberg Text</a>
          <a href="${t.loeb_url}" target="_blank" class="btn-link btn-primary">🏛️ Classical Library / Archive</a>
          <a href="${t.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Purchase Edition</a>
        </div>
      </div>
    `).join('');

    document.getElementById('linguistics-list').innerHTML = S.linguistics_prosody.map(item => `
      <div class="item-card">
        <div class="item-title">${item.title}</div>
        <div class="item-meta">${item.author} (${item.year}) &bull; ${item.publisher}</div>
        <div class="item-desc">${item.focus}</div>
        <div class="links-row">
          <a href="${item.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ JSTOR / Scholarly Archive</a>
          <a href="${item.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Purchase Monograph</a>
        </div>
      </div>
    `).join('');

    document.getElementById('musicology-list').innerHTML = S.musicology_psychoacoustics.map(item => `
      <div class="item-card">
        <div class="item-title">${item.title}</div>
        <div class="item-meta">${item.author} (${item.year}) &bull; ${item.publisher}</div>
        <div class="item-desc">${item.focus}</div>
        <div class="links-row">
          <a href="${item.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ Scholarly Resource</a>
          <a href="${item.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Purchase Monograph</a>
        </div>
      </div>
    `).join('');

    document.getElementById('aero-list').innerHTML = S.aerodynamics_flight.map(item => `
      <div class="item-card">
        <div class="item-title">${item.title}</div>
        <div class="item-meta">${item.author} (${item.year}) &bull; ${item.publisher}</div>
        <div class="item-desc">${item.focus}</div>
        <div class="links-row">
          <a href="${item.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ AIAA / NASA Portal</a>
          <a href="${item.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Purchase Textbook</a>
        </div>
      </div>
    `).join('');

    document.getElementById('vehicle-list').innerHTML = S.vehicle_dynamics_engineering.map(item => `
      <div class="item-card">
        <div class="item-title">${item.title}</div>
        <div class="item-meta">${item.author} (${item.year}) &bull; ${item.publisher}</div>
        <div class="item-desc">${item.focus}</div>
        <div class="links-row">
          <a href="${item.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ SAE International / ScienceDirect</a>
          <a href="${item.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Purchase Textbook</a>
        </div>
      </div>
    `).join('');

    document.getElementById('math-list').innerHTML = S.mathematical_engines.map(eng => `
      <div class="item-card" style="border-left: 4px solid var(--gold-primary);">
        <div class="item-title">${eng.engine}</div>
        <div class="item-meta">${eng.foundational_paper}</div>
        <div style="background:rgba(0,0,0,0.4); padding:1rem; border-radius:6px; margin:0.75rem 0; text-align:center;">
          $${eng.equation_katex}$
        </div>
        <div class="item-desc">${eng.role}</div>
        <div class="links-row">
          <a href="${eng.jstor_url}" target="_blank" class="btn-link btn-jstor">🏛️ Original Math Paper</a>
          <a href="${eng.purchase_url}" target="_blank" class="btn-link btn-buy">🛒 Mathematical Monograph</a>
        </div>
      </div>
    `).join('');
  </script>
</body>
</html>
"""

syllabus_final = syllabus_html.replace("__DATA_SYLLABUS__", json.dumps(SYLLABUS))
with open(os.path.join(WORKSPACE, "syllabus.html"), "w", encoding="utf-8") as f:
    f.write(syllabus_final)

print("Generated syllabus.html successfully! Size:", len(syllabus_final), "bytes")
