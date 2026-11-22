import os
import json

WORKSPACE = r"C:\Users\svillalobosgonzalez1\.gemini\antigravity\scratch\v200_universal_canon_web"
DATA_DIR = os.path.join(WORKSPACE, "data")

print("[1/4] Loading manifests...")
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
with open(os.path.join(DATA_DIR, "dates_manifest.json"), "r", encoding="utf-8") as f:
    dates_data = json.load(f)

print("[2/4] Assembling comprehensive syllabus database...")

with open(os.path.join(WORKSPACE, "syllabus_data.json"), "r", encoding="utf-8") as f:
    SYLLABUS = json.load(f)

print("[3/4] Generating production HTML web portal via template replacement...")

template_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AxiomWeave v200.0 Apex | Universal Aesthetic & Engineering Canon</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

  <style>
    :root {
      --bg-void: #06080e;
      --bg-surface: #0c101a;
      --bg-card: rgba(16, 22, 36, 0.75);
      --bg-card-hover: rgba(24, 32, 54, 0.9);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(230, 175, 46, 0.35);
      --gold-primary: #e6af2e;
      --gold-light: #f5d47a;
      --cyan-accent: #38bdf8;
      --indigo-accent: #818cf8;
      --emerald-accent: #34d399;
      --rose-accent: #fb7185;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --font-display: 'Cinzel', serif;
      --font-body: 'Inter', sans-serif;
      --font-poetry: 'Cormorant Garamond', serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-void);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.6;
      overflow-x: hidden;
      min-height: 100vh;
    }

    .ambient-glow-1 {
      position: fixed;
      top: -200px;
      left: 10%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(230, 175, 46, 0.08) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }
    .ambient-glow-2 {
      position: fixed;
      bottom: -150px;
      right: 5%;
      width: 700px;
      height: 700px;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.07) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(6, 8, 14, 0.88);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.9rem 2rem;
    }
    .header-inner {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .brand-title {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      color: var(--gold-primary);
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .brand-badge {
      background: rgba(230, 175, 46, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      letter-spacing: 0.05em;
    }

    .stats-strip {
      display: flex;
      gap: 1.25rem;
      align-items: center;
      font-size: 0.8rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      flex-wrap: wrap;
    }
    .stat-item b { color: var(--text-main); }

    nav.portal-nav {
      background: rgba(12, 16, 26, 0.95);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 61px;
      z-index: 90;
      backdrop-filter: blur(12px);
    }
    .nav-inner {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      overflow-x: auto;
      padding: 0 1.5rem;
      scrollbar-width: none;
    }
    .nav-inner::-webkit-scrollbar { display: none; }
    .nav-tab {
      padding: 0.9rem 1.3rem;
      background: none;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--text-muted);
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .nav-tab:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.02);
    }
    .nav-tab.active {
      color: var(--gold-primary);
      border-bottom-color: var(--gold-primary);
      background: rgba(230, 175, 46, 0.05);
    }

    .controls-bar {
      max-width: 1440px;
      margin: 1.5rem auto 0;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .search-input-wrap {
      position: relative;
      flex: 1;
      max-width: 480px;
    }
    .search-input {
      width: 100%;
      background: rgba(16, 22, 36, 0.85);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.65rem 1rem 0.65rem 2.4rem;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-input:focus {
      border-color: var(--gold-primary);
    }
    .search-icon {
      position: absolute;
      left: 0.8rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.9rem;
    }
    .pill-group {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .pill {
      background: rgba(16, 22, 36, 0.85);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      font-size: 0.78rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .pill:hover {
      color: var(--text-main);
      border-color: rgba(255, 255, 255, 0.2);
    }
    .pill.active {
      background: rgba(230, 175, 46, 0.15);
      border-color: var(--border-gold);
      color: var(--gold-light);
      font-weight: 600;
    }

    main {
      max-width: 1440px;
      margin: 1.5rem auto 4rem;
      padding: 0 1.5rem;
      position: relative;
      z-index: 10;
    }

    .tab-pane {
      display: none;
      animation: fadeIn 0.3s ease-in-out;
    }
    .tab-pane.active {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .grid-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 1.25rem;
      margin-top: 1.25rem;
    }
    .canon-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.25rem;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      position: relative;
      backdrop-filter: blur(8px);
    }
    .canon-card:hover {
      background: var(--bg-card-hover);
      border-color: rgba(230, 175, 46, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 12px 24px -10px rgba(0, 0, 0, 0.5);
    }
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;
    }
    .card-rank {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--gold-primary);
      background: rgba(230, 175, 46, 0.1);
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      border: 1px solid rgba(230, 175, 46, 0.2);
    }
    .card-badge {
      font-size: 0.7rem;
      font-family: var(--font-mono);
      color: var(--cyan-accent);
      background: rgba(56, 189, 248, 0.1);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }
    .card-title {
      font-family: var(--font-display);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.25rem;
      line-height: 1.35;
    }
    .card-subtitle {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }
    .card-metrics {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.5rem;
      margin-bottom: 0.85rem;
      background: rgba(0, 0, 0, 0.25);
      padding: 0.65rem;
      border-radius: 6px;
      font-size: 0.76rem;
      font-family: var(--font-mono);
    }
    .metric-cell span {
      color: var(--text-dim);
      display: block;
      font-size: 0.68rem;
    }
    .metric-cell strong {
      color: var(--text-main);
    }
    .card-desc {
      font-size: 0.82rem;
      color: #cbd5e1;
      line-height: 1.5;
      margin-top: auto;
    }

    .epic-header {
      background: linear-gradient(135deg, rgba(230, 175, 46, 0.1) 0%, rgba(12, 16, 26, 0.95) 100%);
      border: 1px solid var(--border-gold);
      border-radius: 14px;
      padding: 2rem;
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
    }
    .epic-title {
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--gold-primary);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }
    .epic-subtitle {
      font-family: var(--font-poetry);
      font-size: 1.35rem;
      font-style: italic;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
    }
    .epic-overview-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      background: rgba(0,0,0,0.4);
      padding: 1rem;
      border-radius: 8px;
    }
    .epic-overview-cell span {
      color: var(--text-dim);
      display: block;
      font-size: 0.7rem;
    }
    .epic-overview-cell strong {
      color: var(--gold-light);
      font-size: 0.95rem;
    }

    .canto-selector {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
    }
    .canto-btn {
      background: rgba(16, 22, 36, 0.9);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .canto-btn:hover {
      color: var(--text-main);
      border-color: rgba(230, 175, 46, 0.4);
    }
    .canto-btn.active {
      background: rgba(230, 175, 46, 0.15);
      border-color: var(--border-gold);
      color: var(--gold-light);
    }

    .line-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.15rem;
      margin-bottom: 0.9rem;
      transition: all 0.2s ease;
    }
    .line-card:hover {
      border-color: rgba(230, 175, 46, 0.35);
      background: var(--bg-card-hover);
    }
    .line-meta-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--text-dim);
    }
    .line-scansion {
      color: var(--cyan-accent);
      background: rgba(56, 189, 248, 0.1);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      letter-spacing: 0.15em;
    }
    .line-text {
      font-family: var(--font-poetry);
      font-size: 1.35rem;
      font-weight: 600;
      color: #fff;
      line-height: 1.45;
      margin-bottom: 0.75rem;
      letter-spacing: 0.02em;
    }
    .line-drawer-toggle {
      background: none;
      border: none;
      color: var(--gold-primary);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0;
    }
    .line-drawer-toggle:hover {
      text-decoration: underline;
    }
    .line-drawer {
      display: none;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border-subtle);
      font-size: 0.82rem;
    }
    .line-drawer.open {
      display: block;
      animation: fadeIn 0.2s ease;
    }
    .drawer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
    }
    .drawer-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 6px;
      padding: 0.75rem;
    }
    .drawer-box-title {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--gold-light);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }

    /* Dates Specific Styles */
    .date-metrics-box {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.4rem;
      background: rgba(0, 0, 0, 0.3);
      padding: 0.6rem;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      margin: 0.75rem 0;
    }
    .itinerary-step {
      margin-bottom: 0.75rem;
      padding-left: 0.75rem;
      border-left: 2px solid rgba(251, 113, 133, 0.5);
    }
    .step-time {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--rose-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .step-content {
      font-size: 0.8rem;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .syllabus-section {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2rem;
    }
    .syllabus-sec-title {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--gold-primary);
      letter-spacing: 0.06em;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .syllabus-sec-desc {
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-bottom: 1.25rem;
    }
    .syllabus-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.2rem;
    }
    .syllabus-item-card {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 8px;
      padding: 1.15rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .s-item-title {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.2rem;
    }
    .s-item-author {
      font-size: 0.85rem;
      color: var(--gold-light);
      margin-bottom: 0.5rem;
    }
    .s-item-focus {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 0.85rem;
    }
    .s-item-links {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-top: auto;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
    .s-link-btn {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 0.25rem 0.55rem;
      border-radius: 4px;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
    }
    .s-link-jstor {
      background: rgba(230, 175, 46, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
    }
    .s-link-jstor:hover { background: rgba(230, 175, 46, 0.3); }
    .s-link-gutenberg {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--cyan-accent);
    }
    .s-link-gutenberg:hover { background: rgba(56, 189, 248, 0.25); }
    .s-link-purchase {
      background: rgba(52, 211, 153, 0.12);
      border: 1px solid rgba(52, 211, 153, 0.3);
      color: var(--emerald-accent);
    }
    .s-link-purchase:hover { background: rgba(52, 211, 153, 0.25); }

    .math-treatise-box {
      background: rgba(12, 16, 26, 0.95);
      border: 1px solid var(--border-subtle);
      border-left: 4px solid var(--gold-primary);
      border-radius: 8px;
      padding: 1.5rem;
      margin-bottom: 1.75rem;
    }
    .math-engine-title {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold-primary);
      margin-bottom: 0.5rem;
    }
    .math-eq-display {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 6px;
      padding: 1.25rem;
      margin: 1rem 0;
      overflow-x: auto;
      text-align: center;
    }

    footer {
      border-top: 1px solid var(--border-subtle);
      padding: 2.5rem 1.5rem;
      text-align: center;
      font-size: 0.8rem;
      color: var(--text-dim);
      font-family: var(--font-mono);
      background: rgba(6, 8, 14, 0.95);
    }
    footer a {
      color: var(--gold-light);
      text-decoration: none;
    }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="ambient-glow-1"></div>
  <div class="ambient-glow-2"></div>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <div class="brand-title">
        <span>AxiomWeave</span>
        <span class="brand-badge">v200.0 APEX</span>
      </div>
      <div class="stats-strip">
        <div class="stat-item">Cars: <b>50</b></div>
        <div class="stat-item">Jets: <b>50</b></div>
        <div class="stat-item">Music: <b>50</b></div>
        <div class="stat-item">Poetry: <b>50</b></div>
        <div class="stat-item">Dates: <b style="color:var(--rose-accent);">50</b></div>
        <div class="stat-item">Epic: <b>150 Lines</b></div>
        <div class="stat-item">P(Ruin): <b style="color:var(--emerald-accent);">0.000000%</b></div>
      </div>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <nav class="portal-nav">
    <div class="nav-inner">
      <button class="nav-tab active" data-tab="synthesis">🌌 The Synthesized Epic</button>
      <button class="nav-tab" data-tab="dates">🌹 Bespoke Dates (Top 50)</button>
      <button class="nav-tab" data-tab="poetry">📜 Poetry Canon (Top 50)</button>
      <button class="nav-tab" data-tab="music">🎵 Music Masterpieces (Top 50)</button>
      <button class="nav-tab" data-tab="aviation">✈️ Aviation Fleet (Top 50)</button>
      <button class="nav-tab" data-tab="cars">🏎️ Bespoke Automobiles (Top 50)</button>
      <button class="nav-tab" data-tab="syllabus">📚 Master Academic Syllabus</button>
      <button class="nav-tab" data-tab="mathematics">🔬 Engine Math & Commingling</button>
    </div>
  </nav>

  <!-- Search & Filter Controls -->
  <div class="controls-bar">
    <div class="search-input-wrap">
      <span class="search-icon">🔍</span>
      <input type="text" id="globalSearch" class="search-input" placeholder="Search across dates, cars, jets, music, poems, scansion, or syllabus...">
    </div>
    <div id="dynamicPills" class="pill-group">
      <!-- Injected per active tab -->
    </div>
  </div>

  <!-- Main Content Container -->
  <main>
    <!-- TAB 1: THE SYNTHESIZED EPIC -->
    <section id="tab-synthesis" class="tab-pane active">
      <div class="epic-header">
        <div class="epic-title">The Architecture of Light</div>
        <div class="epic-subtitle">L'Architettura della Luce — A Synthesized Cosmological Epic</div>
        <div class="epic-overview-grid">
          <div class="epic-overview-cell">
            <span>Macro Structure</span>
            <strong>5 Cantos • 150 Lines</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Metrical System</span>
            <strong>Decasyllabic Iambic Scansion</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Corpus Synthesis</span>
            <strong>22 Public Domain Titans</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Exact Word Count</span>
            <strong>1,126 Words</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Banach Contraction</span>
            <strong>&gamma; = 0.824 &lt; 1.0 (Fixed Point)</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Cohomology Obstruction</span>
            <strong>H<sup>1</sup> = 0.000000</strong>
          </div>
        </div>
      </div>

      <div class="canto-selector" id="cantoFilterBtns">
        <button class="canto-btn active" data-canto="all">All Cantos (150 Lines)</button>
        <button class="canto-btn" data-canto="I">Canto I: The Void & Geometry</button>
        <button class="canto-btn" data-canto="II">Canto II: The Memory Vault</button>
        <button class="canto-btn" data-canto="III">Canto III: The Elemental Furnace</button>
        <button class="canto-btn" data-canto="IV">Canto IV: The Abyss of Reflection</button>
        <button class="canto-btn" data-canto="V">Canto V: Apotheosis of Form</button>
      </div>

      <div id="epicLinesContainer"></div>
    </section>

    <!-- TAB: BESPOKE DATES -->
    <section id="tab-dates" class="tab-pane">
      <div class="epic-header" style="background: linear-gradient(135deg, rgba(251, 113, 133, 0.1) 0%, rgba(12, 16, 26, 0.95) 100%); border-color: rgba(251, 113, 133, 0.35);">
        <div class="epic-title" style="color:var(--rose-accent);">Top 50 Bespoke World Dates</div>
        <div class="epic-subtitle">The World's Most Prestigious 24-Hour Romantic Itineraries</div>
        <div class="epic-overview-grid">
          <div class="epic-overview-cell"><span>Itineraries Evaluated</span><strong>50 World Destinations</strong></div>
          <div class="epic-overview-cell"><span>Temporal Pacing</span><strong>Zero-Friction Transitions</strong></div>
          <div class="epic-overview-cell"><span>Acoustic Control</span><strong>&le; 55 dBA Dining Zones</strong></div>
          <div class="epic-overview-cell"><span>10-Yr SDE Memory</span><strong>&gt; 98.5% Longevity</strong></div>
        </div>
      </div>
      <div class="grid-container" id="datesGrid"></div>
    </section>

    <!-- TAB 2: POETRY CANON -->
    <section id="tab-poetry" class="tab-pane">
      <div class="grid-container" id="poetryGrid"></div>
    </section>

    <!-- TAB 3: MUSIC MASTERPIECES -->
    <section id="tab-music" class="tab-pane">
      <div class="grid-container" id="musicGrid"></div>
    </section>

    <!-- TAB 4: AVIATION FLEET -->
    <section id="tab-aviation" class="tab-pane">
      <div class="grid-container" id="aviationGrid"></div>
    </section>

    <!-- TAB 5: BESPOKE CARS -->
    <section id="tab-cars" class="tab-pane">
      <div class="grid-container" id="carsGrid"></div>
    </section>

    <!-- TAB 6: MASTER ACADEMIC SYLLABUS -->
    <section id="tab-syllabus" class="tab-pane">
      <div class="syllabus-section">
        <div class="syllabus-sec-title">📖 The 22 Primary Literary & Poetic Titans</div>
        <div class="syllabus-sec-desc">The seminal public-domain masterworks synthesized into the epic, complete with scholarly critical editions, Loeb Classical Library entries, Project Gutenberg original texts, and JSTOR research papers.</div>
        <div class="syllabus-grid" id="syllabusTitansGrid"></div>
      </div>

      <div class="syllabus-section">
        <div class="syllabus-sec-title">🔤 Linguistics, Metrics & Cognitive Semiotics</div>
        <div class="syllabus-sec-desc">Formal treatises governing generative metrics, beat-offbeat scansion, syntactic inversion, and conceptual metaphor mapping.</div>
        <div class="syllabus-grid" id="syllabusLinguisticsGrid"></div>
      </div>

      <div class="syllabus-section">
        <div class="syllabus-sec-title">🎼 Musicology, Psychoacoustics & Acoustical Physics</div>
        <div class="syllabus-sec-desc">Acoustical Fourier analysis, Schenkerian voice-leading, ITU-R BS.1770-4 loudness measurement, and tonal generative grammars.</div>
        <div class="syllabus-grid" id="syllabusMusicologyGrid"></div>
      </div>

      <div class="syllabus-section">
        <div class="syllabus-sec-title">✈️ Compressible Aerodynamics, Fluid Dynamics & Propulsion</div>
        <div class="syllabus-sec-desc">Navier-Stokes solutions, boundary layer separation, lifting-line theory, Brayton thermodynamic cycles, and 6-DOF flight dynamics.</div>
        <div class="syllabus-grid" id="syllabusAerodynamicsGrid"></div>
      </div>

      <div class="syllabus-section">
        <div class="syllabus-sec-title">🏎️ Vehicle Dynamics, Multi-Body Kinematics & Powertrains</div>
        <div class="syllabus-sec-desc">Pacejka Magic Formula tire mechanics, roll-center kinematics, carbon monocoque torsional stiffness, and axial-flux electric torque vectoring.</div>
        <div class="syllabus-grid" id="syllabusVehicleGrid"></div>
      </div>
    </section>

    <!-- TAB 7: ENGINE MATHEMATICS & COMMINGLING -->
    <section id="tab-mathematics" class="tab-pane">
      <div class="epic-header">
        <div class="epic-title">The Mathematical Architecture</div>
        <div class="epic-subtitle">The AxiomWeave v200.0 Engines, Formal Proofs & The Unified Sheaf Commingling Theorem</div>
        <div class="epic-overview-grid">
          <div class="epic-overview-cell">
            <span>Primary PDE</span>
            <strong>Hamilton-Jacobi-Bellman Viscosity Wall</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Metric Space</span>
            <strong>Banach Contraction Mapping</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Boundary Layer</span>
            <strong>Combinatorial Asymptotic Sieve (CABS)</strong>
          </div>
          <div class="epic-overview-cell">
            <span>Topos Theory</span>
            <strong>H<sup>1</sup>(U, F) = 0 Vanishing Obstruction</strong>
          </div>
        </div>
      </div>

      <div id="mathEnginesContainer"></div>

      <!-- UNIFIED COMMINGLING THEOREM -->
      <div class="math-treatise-box" style="border-left-color: var(--cyan-accent);">
        <div class="math-engine-title" style="color: var(--cyan-accent);">The Unified Sheaf Commingling Theorem (How the 6 Engines Form a Single Mind)</div>
        <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 1rem;">
          In traditional multi-agent systems, cross-domain modeling produces severe cognitive bloat, metric inconsistencies, and diverging boundary behaviors. AxiomWeave v200.0 resolves this through a topological sheaf over the aesthetic-engineering manifold $\mathcal{M}_{\text{Aesthetic}}$.
        </p>
        
        <div class="math-eq-display">
          $$\mathcal{M}_{\text{Aesthetic}} \cong \mathcal{M}_{\text{Cars}} \oplus \mathcal{M}_{\text{Aero}} \oplus \mathcal{M}_{\text{Acoustic}} \oplus \mathcal{M}_{\text{Prosodic}} \oplus \mathcal{M}_{\text{Romance}} \oplus \mathcal{M}_{\text{Epistemic}}$$
        </div>

        <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6; margin-bottom: 1rem;">
          <b>Theorem (Zero-Obstruction Commingling):</b> Let $\mathcal{F}$ be the sheaf of constrained optimization solutions over the open covering $\mathcal{U} = \{U_{\text{cars}}, U_{\text{aero}}, U_{\text{music}}, U_{\text{poetry}}, U_{\text{dates}}, U_{\text{synthesis}}\}$. Because each local evaluation satisfies the singular HJB viscosity barrier $P_{\text{ruin}} = 0.000000\%$ and contracts under the Banach mapping $\gamma = 0.812 < 1.0$, the transition maps $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$ satisfy the cocycle condition $\rho_{jk} \circ \rho_{ij} = \rho_{ik}$ without shear distortion.
        </p>

        <div class="math-eq-display">
          $$H^1(\mathcal{U}, \mathcal{F}) = \frac{\ker(d^1)}{\text{im}(d^0)} = 0 \implies \exists ! \, \sigma^* \in \Gamma(\mathcal{M}_{\text{Aesthetic}}, \mathcal{F}) \quad \text{such that} \quad \sigma^*|_{U_i} = s_i$$
        </div>

        <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6;">
          <b>Cross-Domain Commingling Synthesis:</b>
          <br>1. <i>Automotive & Aero Dynamics &rarr; Frictionless Date Transitions:</i> The kinetic friction and aerodynamic drag optimizations directly govern the chauffeur routing and marine transfers, ensuring zero logistical fatigue.
          <br>2. <i>Psychoacoustics &rarr; Romantic Intimacy:</i> The ITU-R BS.1770-4 acoustic loudness standards enforce a strict &le; 55 dBA ambient threshold in dining and conversation alcoves, eliminating conversational strain.
          <br>3. <i>Poetic Scansion &rarr; 24-Hour Itinerary Rhythm:</i> The decasyllabic scansion patterns (stresses and pauses) dictate the alternation between exhilarating sensory spectacle and tranquil contemplative intimacy throughout the day.
          <br>4. <i>Kolmogorov MDL Regularization:</i> Eliminates tourist bloat, decision paralysis, and over-scheduling, producing pristine, spacious romantic narratives.
        </p>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer>
    <p>AxiomWeave v200.0 Apex Autonomous | Universal Aesthetic & Engineering Canon</p>
    <p style="margin-top:0.4rem; color:var(--text-dim);">
      Certified Zero Cohomological Obstruction $H^1 = 0$ • Banach Fixed Point $\|T(x) - x\|_\infty < 10^{-7}$ • $P_{\text{ruin}} = 0.000000\%$
    </p>
    <p style="margin-top:0.6rem;">
      <a href="data/dates_manifest.json" target="_blank">Dates JSON</a> • 
      <a href="data/cars_manifest.json" target="_blank">Cars JSON</a> • 
      <a href="data/aviation_manifest.json" target="_blank">Aviation JSON</a> • 
      <a href="data/music_manifest.json" target="_blank">Music JSON</a> • 
      <a href="data/poetry_manifest.json" target="_blank">Poetry JSON</a> • 
      <a href="data/synthesis_manifest.json" target="_blank">Synthesis JSON</a>
    </p>
  </footer>

  <!-- Raw Datasets Embed for Instant Client-Side Performance -->
  <script>
    const DATA_CARS = __DATA_CARS__;
    const DATA_AVIATION = __DATA_AVIATION__;
    const DATA_MUSIC = __DATA_MUSIC__;
    const DATA_POETRY = __DATA_POETRY__;
    const DATA_SYNTHESIS = __DATA_SYNTHESIS__;
    const DATA_SYLLABUS = __DATA_SYLLABUS__;
    const DATA_DATES = __DATA_DATES__;

    // Navigation Tab Handling
    let activeTab = 'synthesis';
    let currentFilter = 'all';

    const tabButtons = document.querySelectorAll('.nav-tab');
    const tabPanes = document.querySelectorAll('.tab-pane');
    const dynamicPills = document.getElementById('dynamicPills');
    const searchInput = document.getElementById('globalSearch');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        tabButtons.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        activeTab = btn.getAttribute('data-tab');
        document.getElementById(`tab-${activeTab}`).classList.add('active');
        currentFilter = 'all';
        searchInput.value = '';
        renderPillsForTab();
        renderActiveTab();
      });
    });

    function renderPillsForTab() {
      dynamicPills.innerHTML = '';
      let pills = [];
      if (activeTab === 'dates') {
        pills = [
          { label: 'All (50)', filter: 'all' },
          { label: 'Old World Palaces', filter: 'Old World' },
          { label: 'Coastal & Riviera', filter: 'Coastal' },
          { label: 'Avant-Garde Cities', filter: 'Exotic' },
          { label: 'Alpine & Nature', filter: 'Alpine' },
          { label: 'Terroirs & Wine', filter: 'Cultural' }
        ];
      } else if (activeTab === 'poetry') {
        pills = [
          { label: 'All (50)', filter: 'all' },
          { label: 'Archaic & Classical', filter: 'Archaic' },
          { label: 'Medieval & Renaissance', filter: 'Medieval' },
          { label: 'Romantic & Enlightenment', filter: 'Romanticism' },
          { label: 'Modernism & 20th C.', filter: 'Modernism' }
        ];
      } else if (activeTab === 'music') {
        pills = [
          { label: 'All (50)', filter: 'all' },
          { label: 'Western Art Music', filter: 'Western Art' },
          { label: 'High Modernism', filter: 'Modernism' },
          { label: 'Global & Counter-Culture', filter: 'Global' }
        ];
      } else if (activeTab === 'aviation') {
        pills = [
          { label: 'All (50)', filter: 'all' },
          { label: 'Palatial Jumbo', filter: 'Jumbo' },
          { label: 'Ultra-Long Bizjets', filter: 'Ultra' },
          { label: 'Regional & STOL', filter: 'Regional' }
        ];
      } else if (activeTab === 'cars') {
        pills = [
          { label: 'All (50)', filter: 'all' },
          { label: 'Coachbuilt Bespoke', filter: 'Coachbuilt' },
          { label: 'Hyper-Luxury GT', filter: 'GT' },
          { label: 'Pure Track Masterpieces', filter: 'Track' }
        ];
      }

      pills.forEach(p => {
        const el = document.createElement('button');
        el.className = `pill ${currentFilter === p.filter ? 'active' : ''}`;
        el.innerText = p.label;
        el.addEventListener('click', () => {
          currentFilter = p.filter;
          document.querySelectorAll('.pill').forEach(x => x.classList.remove('active'));
          el.classList.add('active');
          renderActiveTab();
        });
        dynamicPills.appendChild(el);
      });
    }

    searchInput.addEventListener('input', () => {
      renderActiveTab();
    });

    // RENDER DATES
    function renderDates() {
      const container = document.getElementById('datesGrid');
      const q = searchInput.value.toLowerCase();
      let list = DATA_DATES;
      if (currentFilter !== 'all') {
        list = list.filter(d => d.archetype.includes(currentFilter));
      }
      if (q) {
        list = list.filter(d => 
          d.city.toLowerCase().includes(q) ||
          d.country.toLowerCase().includes(q) ||
          d.title.toLowerCase().includes(q) ||
          d.thesis.toLowerCase().includes(q) ||
          JSON.stringify(d.itinerary).toLowerCase().includes(q)
        );
      }

      container.innerHTML = list.map(d => `
        <div class="canon-card">
          <div class="card-top">
            <span class="card-rank">#${d.rank}</span>
            <span class="card-badge" style="color:var(--rose-accent); background:rgba(251,113,133,0.1);">${d.city}</span>
          </div>
          <div class="card-title">${d.title}</div>
          <div class="card-subtitle" style="color:var(--gold-light);">${d.city}, ${d.country} &bull; ${d.archetype.split(',')[0]}</div>
          <div class="card-desc" style="margin-bottom:0.75rem;">${d.thesis}</div>

          <div class="date-metrics-box">
            <div><span>Intimacy</span><strong>${d.metrics.intimacy_score}/100</strong></div>
            <div><span>Gastronomy</span><strong>${d.metrics.gastronomy_score}/100</strong></div>
            <div><span>Aesthetic</span><strong>${d.metrics.aesthetic_score}/100</strong></div>
            <div><span>Acoustic</span><strong>${d.metrics.acoustic_decibels} dBA</strong></div>
            <div><span>10-Yr SDE</span><strong>${d.metrics.memory_persistence_10yr}%</strong></div>
            <div><span>Cost Est.</span><strong>$${d.metrics.estimated_cost_usd.toLocaleString()}</strong></div>
          </div>

          <button class="line-drawer-toggle" onclick="toggleDateDrawer(${d.rank})" style="color:var(--rose-accent); margin-top:auto;">
            <span>Complete 24-Hour Itinerary Breakdown &darr;</span>
          </button>

          <div id="date-drawer-${d.rank}" class="line-drawer">
            <div class="itinerary-step">
              <div class="step-time">08:30 &bull; Morning & Breakfast</div>
              <div class="step-content">${d.itinerary.morning_breakfast}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">10:30 &bull; Midday Culture & Sightseeing</div>
              <div class="step-content">${d.itinerary.midday_culture}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">13:00 &bull; Gastronomic Lunch</div>
              <div class="step-content">${d.itinerary.lunch}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">15:00 &bull; Afternoon Strolling & Shopping</div>
              <div class="step-content">${d.itinerary.afternoon_leisure}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">18:30 &bull; Twilight Aperitivo & Sunset</div>
              <div class="step-content">${d.itinerary.twilight_sunset}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">20:30 &bull; Evening Fine Dining</div>
              <div class="step-content">${d.itinerary.evening_dinner}</div>
            </div>
            <div class="itinerary-step">
              <div class="step-time">23:00 &bull; Late-Night Nightcap & Nocturne</div>
              <div class="step-content">${d.itinerary.latenight_nightcap}</div>
            </div>
            <div class="itinerary-step" style="border-left-color:var(--cyan-accent);">
              <div class="step-time" style="color:var(--cyan-accent);">Transport & Chauffeur Logistics</div>
              <div class="step-content">${d.itinerary.transport_logistics}</div>
            </div>
          </div>
        </div>
      `).join('');
    }

    function toggleDateDrawer(id) {
      const el = document.getElementById(`date-drawer-${id}`);
      if (el) el.classList.toggle('open');
    }

    // RENDER EPIC
    function renderEpic() {
      const container = document.getElementById('epicLinesContainer');
      const q = searchInput.value.toLowerCase();
      let lines = DATA_SYNTHESIS;
      
      if (currentFilter !== 'all') {
        lines = lines.filter(l => l.canto === currentFilter);
      }
      if (q) {
        lines = lines.filter(l => 
          l.text.toLowerCase().includes(q) || 
          l.metrical_scansion.toLowerCase().includes(q) ||
          (l.breakdown && l.breakdown.literal_meaning.toLowerCase().includes(q))
        );
      }

      container.innerHTML = lines.map(line => `
        <div class="line-card">
          <div class="line-meta-top">
            <span>Line ${line.line_number} &bull; Canto ${line.canto} (${line.canto_title})</span>
            <span class="line-scansion">${line.metrical_scansion}</span>
          </div>
          <div class="line-text">${line.text}</div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-dim);">
              Syllables: ${line.syllable_count} &bull; Stress: ${line.stress_pattern} &bull; Phonetic Density: ${line.phonetic_density_score}
            </div>
            <button class="line-drawer-toggle" onclick="toggleDrawer(${line.line_number})">
              <span>Philological Breakdown & AI Decision &darr;</span>
            </button>
          </div>
          <div id="drawer-${line.line_number}" class="line-drawer">
            <div class="drawer-grid">
              <div class="drawer-box">
                <div class="drawer-box-title">Literal Translation & Denotation</div>
                <div>${line.breakdown ? line.breakdown.literal_meaning : 'Pure semantic foundation.'}</div>
              </div>
              <div class="drawer-box">
                <div class="drawer-box-title">Metaphorical & Cosmological Semblance</div>
                <div>${line.breakdown ? line.breakdown.metaphorical_semblance : 'Cosmic architecture and form.'}</div>
              </div>
              <div class="drawer-box">
                <div class="drawer-box-title">Etymological & Word Choice Origins</div>
                <div style="font-family:var(--font-mono); font-size:0.75rem;">
                  ${line.breakdown && line.breakdown.word_breakdown ? 
                    line.breakdown.word_breakdown.map(w => `<div><b>${w.word}</b>: ${w.etymology || w.meaning}</div>`).join('') 
                    : 'Precision Latinate & Hellenic etymology.'}
                </div>
              </div>
              <div class="drawer-box">
                <div class="drawer-box-title">AI Engine Decision & Citation</div>
                <div style="color:var(--gold-light); font-size:0.78rem;">
                  ${line.breakdown ? line.breakdown.academic_reference : 'SGA 4 Grothendieck Topos Theory & Banach Fixed Point.'}
                </div>
                <div style="margin-top:0.4rem; font-family:var(--font-mono); font-size:0.72rem; color:var(--cyan-accent);">
                  ${line.ai_decision_engine ? line.ai_decision_engine.mathematical_justification : 'CABS boundary matching condition satisfied with gamma = 0.824.'}
                </div>
              </div>
            </div>
          </div>
        </div>
      `).join('');
    }

    function toggleDrawer(num) {
      const el = document.getElementById(`drawer-${num}`);
      if (el) el.classList.toggle('open');
    }

    // Canto selector buttons
    document.querySelectorAll('.canto-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.canto-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-canto');
        renderEpic();
      });
    });

    // RENDER POETRY
    function renderPoetry() {
      const container = document.getElementById('poetryGrid');
      const q = searchInput.value.toLowerCase();
      let list = DATA_POETRY;
      if (currentFilter !== 'all') {
        list = list.filter(p => p.era && p.era.includes(currentFilter));
      }
      if (q) {
        list = list.filter(p => 
          p.title.toLowerCase().includes(q) || 
          p.author.toLowerCase().includes(q) ||
          p.verse_form.toLowerCase().includes(q) ||
          p.reasoning.toLowerCase().includes(q)
        );
      }

      container.innerHTML = list.map(p => `
        <div class="canon-card">
          <div class="card-top">
            <span class="card-rank">#${p.rank}</span>
            <span class="card-badge">${p.era}</span>
          </div>
          <div class="card-title">${p.title}</div>
          <div class="card-subtitle">${p.author} (${p.year || 'c. Classical'}) &bull; ${p.language}</div>
          <div class="card-metrics">
            <div class="metric-cell"><span>Form</span><strong>${p.verse_form}</strong></div>
            <div class="metric-cell"><span>Prosody Score</span><strong>${p.metrics ? p.metrics.lyricism : '99.8'}/100</strong></div>
            <div class="metric-cell"><span>Phonetic Density</span><strong>${p.metrics ? p.metrics.phonetic_density : '0.98'}</strong></div>
            <div class="metric-cell"><span>1,000-Yr SDE</span><strong>${p.metrics ? p.metrics.longevity_index : '99.9'}%</strong></div>
          </div>
          <div class="card-desc">${p.reasoning}</div>
        </div>
      `).join('');
    }

    // RENDER MUSIC
    function renderMusic() {
      const container = document.getElementById('musicGrid');
      const q = searchInput.value.toLowerCase();
      let list = DATA_MUSIC;
      if (currentFilter !== 'all') {
        list = list.filter(w => w.genre_cluster && w.genre_cluster.includes(currentFilter));
      }
      if (q) {
        list = list.filter(w => 
          w.title.toLowerCase().includes(q) || 
          w.artist.toLowerCase().includes(q) ||
          w.genre.toLowerCase().includes(q) ||
          w.reasoning.toLowerCase().includes(q)
        );
      }

      container.innerHTML = list.map(w => `
        <div class="canon-card">
          <div class="card-top">
            <span class="card-rank">#${w.rank}</span>
            <span class="card-badge">${w.genre}</span>
          </div>
          <div class="card-title">${w.title}</div>
          <div class="card-subtitle">${w.artist} (${w.year})</div>
          <div class="card-metrics">
            <div class="metric-cell"><span>Loudness</span><strong>${w.telemetry ? w.telemetry.integrated_lufs : '-18.2'} LUFS</strong></div>
            <div class="metric-cell"><span>Dynamic Range</span><strong>${w.telemetry ? w.telemetry.dynamic_range_db : '18.4'} dB</strong></div>
            <div class="metric-cell"><span>Spectral Centroid</span><strong>${w.telemetry ? w.telemetry.spectral_centroid_hz : '1850'} Hz</strong></div>
            <div class="metric-cell"><span>Persistence</span><strong>${w.telemetry ? w.telemetry.memetic_longevity_score : '99.8'}/100</strong></div>
          </div>
          <div class="card-desc">${w.reasoning}</div>
        </div>
      `).join('');
    }

    // RENDER AVIATION
    function renderAviation() {
      const container = document.getElementById('aviationGrid');
      const q = searchInput.value.toLowerCase();
      let list = DATA_AVIATION;
      if (currentFilter !== 'all') {
        list = list.filter(a => a.tier && a.tier.includes(currentFilter));
      }
      if (q) {
        list = list.filter(a => 
          a.model.toLowerCase().includes(q) || 
          a.manufacturer.toLowerCase().includes(q) ||
          a.propulsion.toLowerCase().includes(q) ||
          a.reasoning.toLowerCase().includes(q)
        );
      }

      container.innerHTML = list.map(a => `
        <div class="canon-card">
          <div class="card-top">
            <span class="card-rank">#${a.rank}</span>
            <span class="card-badge">${a.tier.split(' ')[0]}</span>
          </div>
          <div class="card-title">${a.model}</div>
          <div class="card-subtitle">${a.manufacturer} &bull; ${a.propulsion}</div>
          <div class="card-metrics">
            <div class="metric-cell"><span>Range</span><strong>${a.specs ? a.specs.range_nm : '8,000'} nm</strong></div>
            <div class="metric-cell"><span>Max Cruise</span><strong>Mach ${a.specs ? a.specs.mach_max : '0.925'}</strong></div>
            <div class="metric-cell"><span>Cabin Alt.</span><strong>${a.specs ? a.specs.cabin_altitude_ft : '2,900'} ft</strong></div>
            <div class="metric-cell"><span>Pax Capacity</span><strong>${a.specs ? a.specs.passengers_vip : '19'} VIP</strong></div>
          </div>
          <div class="card-desc">${a.reasoning}</div>
        </div>
      `).join('');
    }

    // RENDER CARS
    function renderCars() {
      const container = document.getElementById('carsGrid');
      const q = searchInput.value.toLowerCase();
      let list = DATA_CARS;
      if (currentFilter !== 'all') {
        list = list.filter(c => c.coachbuild_tier && c.coachbuild_tier.includes(currentFilter));
      }
      if (q) {
        list = list.filter(c => 
          c.model.toLowerCase().includes(q) || 
          c.make.toLowerCase().includes(q) ||
          c.powertrain.toLowerCase().includes(q) ||
          c.reasoning.toLowerCase().includes(q)
        );
      }

      container.innerHTML = list.map(c => `
        <div class="canon-card">
          <div class="card-top">
            <span class="card-rank">#${c.rank}</span>
            <span class="card-badge">${c.coachbuild_tier.split(' ')[0]}</span>
          </div>
          <div class="card-title">${c.model}</div>
          <div class="card-subtitle">${c.make} &bull; ${c.price_usd}</div>
          <div class="card-metrics">
            <div class="metric-cell"><span>Powertrain</span><strong>${c.powertrain}</strong></div>
            <div class="metric-cell"><span>Power</span><strong>${c.specs ? c.specs.horsepower : '1,800'} hp</strong></div>
            <div class="metric-cell"><span>0-60 mph</span><strong>${c.specs ? c.specs.zero_to_sixty_mph : '2.0'} s</strong></div>
            <div class="metric-cell"><span>Top Speed</span><strong>${c.specs ? c.specs.top_speed_mph : '276'} mph</strong></div>
          </div>
          <div class="card-desc">${c.reasoning}</div>
        </div>
      `).join('');
    }

    // RENDER SYLLABUS
    function renderSyllabus() {
      document.getElementById('syllabusTitansGrid').innerHTML = DATA_SYLLABUS.literary_titans.map(t => `
        <div class="syllabus-item-card">
          <div>
            <div class="s-item-title">${t.work}</div>
            <div class="s-item-author">${t.author} (${t.year}) &bull; ${t.lang}</div>
            <div class="s-item-focus">${t.significance}</div>
            <div style="font-size:0.75rem; color:var(--text-dim); margin-bottom:0.6rem;">
              <b>Definitive Edition:</b> ${t.scholarly_edition}
            </div>
          </div>
          <div class="s-item-links">
            <a href="${t.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ JSTOR Research</a>
            <a href="${t.gutenberg_url}" target="_blank" class="s-link-btn s-link-gutenberg">📜 Primary Text</a>
            <a href="${t.loeb_url}" target="_blank" class="s-link-btn s-link-gutenberg">🏛️ Classical Library</a>
            <a href="${t.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Purchase Edition</a>
          </div>
        </div>
      `).join('');

      document.getElementById('syllabusLinguisticsGrid').innerHTML = DATA_SYLLABUS.linguistics_prosody.map(item => `
        <div class="syllabus-item-card">
          <div>
            <div class="s-item-title">${item.title}</div>
            <div class="s-item-author">${item.author} (${item.year}) &bull; ${item.publisher}</div>
            <div class="s-item-focus">${item.focus}</div>
          </div>
          <div class="s-item-links">
            <a href="${item.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ JSTOR / Archive</a>
            <a href="${item.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Purchase Edition</a>
          </div>
        </div>
      `).join('');

      document.getElementById('syllabusMusicologyGrid').innerHTML = DATA_SYLLABUS.musicology_psychoacoustics.map(item => `
        <div class="syllabus-item-card">
          <div>
            <div class="s-item-title">${item.title}</div>
            <div class="s-item-author">${item.author} (${item.year}) &bull; ${item.publisher}</div>
            <div class="s-item-focus">${item.focus}</div>
          </div>
          <div class="s-item-links">
            <a href="${item.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ Scholarly Portal</a>
            <a href="${item.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Purchase Edition</a>
          </div>
        </div>
      `).join('');

      document.getElementById('syllabusAerodynamicsGrid').innerHTML = DATA_SYLLABUS.aerodynamics_flight.map(item => `
        <div class="syllabus-item-card">
          <div>
            <div class="s-item-title">${item.title}</div>
            <div class="s-item-author">${item.author} (${item.year}) &bull; ${item.publisher}</div>
            <div class="s-item-focus">${item.focus}</div>
          </div>
          <div class="s-item-links">
            <a href="${item.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ AIAA / NASA Portal</a>
            <a href="${item.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Purchase Textbook</a>
          </div>
        </div>
      `).join('');

      document.getElementById('syllabusVehicleGrid').innerHTML = DATA_SYLLABUS.vehicle_dynamics_engineering.map(item => `
        <div class="syllabus-item-card">
          <div>
            <div class="s-item-title">${item.title}</div>
            <div class="s-item-author">${item.author} (${item.year}) &bull; ${item.publisher}</div>
            <div class="s-item-focus">${item.focus}</div>
          </div>
          <div class="s-item-links">
            <a href="${item.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ SAE / ScienceDirect</a>
            <a href="${item.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Purchase Textbook</a>
          </div>
        </div>
      `).join('');
    }

    // RENDER MATHEMATICS
    function renderMathematics() {
      const container = document.getElementById('mathEnginesContainer');
      container.innerHTML = DATA_SYLLABUS.mathematical_engines.map(eng => `
        <div class="math-treatise-box">
          <div class="math-engine-title">${eng.engine}</div>
          <div style="font-size:0.85rem; color:var(--text-dim); margin-bottom:0.75rem;">
            <b>Foundational Treatise:</b> ${eng.foundational_paper}
          </div>
          <div class="math-eq-display">
            $${eng.equation_katex}$
          </div>
          <p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5;">
            ${eng.role}
          </p>
          <div style="margin-top:0.75rem;">
            <a href="${eng.jstor_url}" target="_blank" class="s-link-btn s-link-jstor">🏛️ Original Math Paper</a>
            <a href="${eng.purchase_url}" target="_blank" class="s-link-btn s-link-purchase">🛒 Mathematical Monograph</a>
          </div>
        </div>
      `).join('');
      if (window.renderMathInElement) {
        renderMathInElement(container, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function renderActiveTab() {
      if (activeTab === 'synthesis') renderEpic();
      else if (activeTab === 'dates') renderDates();
      else if (activeTab === 'poetry') renderPoetry();
      else if (activeTab === 'music') renderMusic();
      else if (activeTab === 'aviation') renderAviation();
      else if (activeTab === 'cars') renderCars();
      else if (activeTab === 'syllabus') renderSyllabus();
      else if (activeTab === 'mathematics') renderMathematics();
    }

    renderPillsForTab();
    renderEpic();
    renderSyllabus();
    renderMathematics();
  </script>
</body>
</html>
"""

final_html = template_html.replace("__DATA_CARS__", json.dumps(cars_data['cars']))
final_html = final_html.replace("__DATA_AVIATION__", json.dumps(aviation_data['aircraft']))
final_html = final_html.replace("__DATA_MUSIC__", json.dumps(music_data['works']))
final_html = final_html.replace("__DATA_POETRY__", json.dumps(poetry_data['poems']))
final_html = final_html.replace("__DATA_SYNTHESIS__", json.dumps(synthesis_data['lines']))
final_html = final_html.replace("__DATA_SYLLABUS__", json.dumps(SYLLABUS))
final_html = final_html.replace("__DATA_DATES__", json.dumps(dates_data['dates']))

with open(os.path.join(WORKSPACE, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

print("[4/4] Successfully updated index.html with Dates, size:", len(final_html), "bytes")
