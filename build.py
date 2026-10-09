#!/usr/bin/env python3
"""Generates the static site. Edit CONTENT below, run `python3 build.py`, commit the output.
GitHub Pages serves the generated .html files directly; Python is only needed on your machine."""
import html, os

NAME = "Tri Nguyen"
EMAIL = ""  # e.g. "you@example.com". Leave empty to hide the email link.
LINKEDIN = "https://www.linkedin.com/in/tri-game-design/"
EDB = "https://nhantri132.github.io/enemy-design-database/"
SITE_DESC = "Tri Nguyen is a gameplay designer focused on combat, enemy AI and NPCs. Credits include Star Wars Jedi: Survivor and Marvel's Wolverine."

# kind: "featured" gets a large row; "other" a compact one.
PROJECTS = [
 dict(slug="giant-skull", title="Giant Skull", studio="Giant Skull", role="Senior Gameplay Designer",
      year="Current", kind="featured", tools="", platform="",
      blurb="Senior gameplay designer focused on AI enemies and NPCs.",
      intro="I'm working at Giant Skull as a Senior Gameplay Designer focused on AI enemies and NPCs.",
      sections=[dict(h="Reel", video="6fN6n3jFXZ0")], link=("Giant Skull", "https://www.giantskull.com")),
 dict(slug="marvels-wolverine", title="Marvel’s Wolverine", studio="", role="Combat Designer",
      year="", kind="featured", tools="", platform="",
      blurb="Designed, prototyped and implemented enemy AI.",
      intro="I worked on Marvel’s Wolverine as a combat designer, working primarily on designing, prototyping, and implementing enemy AI.",
      sections=[dict(h="Reel", video="_U56cQFx_Vw")]),
 dict(slug="star-wars-jedi-survivor", title="Star Wars Jedi: Survivor", studio="Respawn Entertainment", role="Combat Designer",
      year="", kind="featured", tools="", platform="",
      blurb="A sentry droid, a lightsaber miniboss and the Bode Akuna boss fights.",
      intro="I worked at Respawn Entertainment as a combat designer on Star Wars Jedi: Survivor, the sequel to Star Wars Jedi: Fallen Order.",
      sections=[
        dict(h="DT Sentry Droid (all variants)", video="4ay22_N0cSU", points=[
          "Designed and implemented the enemy, including all weapon variants.",
          "Built a dismemberment system with conditional behaviors based on player actions.",
          "Worked with the animator to create combos driven by the enemy’s equipped weapons."]),
        dict(h="Lightsaber miniboss (single saber)", video="naO9H6MZibE", points=[
          "A miniboss fight with cinematics that enter and exit during the encounter.",
          "Created several in-world variants with unique mechanics, including invisibility and multiple weapon types (lightsaber, shock grenade, blasters)."]),
        dict(h="Bode Akuna (boss fights)", video="JtRbJhPb2EM", points=[
          "Designed and implemented multiple boss fights featuring an ally NPC, QTE cinematics, and multiple stage transitions.",
          "Facilitated and led the boss fight pod and kept the boss fights on schedule for shipping.",
          "Pitched and storyboarded the narrative and cinematic throughline for the final boss encounter, including how it shaped its mechanics and flow."])]),
 dict(slug="clawface", title="Clawface", studio="", role="Lead Game Designer", year="", kind="other",
      platform="Windows, Mac, Linux", tools="Unity", blurb="Weapons, enemy AI and dynamic level design, plus creative direction for a team of 18.",
      intro="",
      sections=[dict(h="Gameplay", video="A41UPDj2UNg", points=[
        "In charge of designing the weapon functions and balance, enemy AI behavior, and the dynamic level design.",
        "Creative director for a team of 18, maintaining and communicating a consistent vision from pre-production to release while hitting multiple deadlines."])]),
 dict(slug="wwe-undefeated", title="WWE Undefeated", studio="", role="Systems Designer", year="", kind="other",
      platform="Mobile", tools="Unity", blurb="Led the Class Moves overhaul of meta-systems and combat; wrote the tutorial; scripted AI bots.",
      intro="",
      sections=[dict(h="Gameplay", video="Xv6aqndl5Hk", points=[
        "Class Moves update: led the overhaul of the game’s meta-systems and combat to simplify deckbuilding and add variety to online matches. The release improved KPIs and retention.",
        "Style (passive abilities): designed the passive abilities that trigger during combat, aligned them with the combat designers’ character vision, and implemented them in spreadsheets and Unity.",
        "Tutorial: wrote, designed and scripted the full tutorial, iterating on each release based on data.",
        "AI bots: designed and scripted player AI bots using Unity behavior trees."])]),
 dict(slug="frozen-adventures", title="Frozen Adventures", studio="Jam City", role="Level Designer", year="", kind="other",
      platform="Mobile", tools="Unity", blurb="Match-3 levels tuned with live player data. Google Play Best Casual Games of 2020.",
      intro="", link=("Jam City", "https://www.jamcity.com"),
      sections=[dict(h="Gameplay", video="7jFVcO5nsdw", points=[
        "Designed match-3 levels within the Unity engine and tuned them using live player data.",
        "Worked on points of interest in rooms.",
        "Helped product managers iterate on live features by analyzing data in Tableau.",
        "Wrote specifications for new systems, features and mechanics.",
        "Listed in Google Play’s Best Casual Games of 2020."])]),
 dict(slug="harry-potter-hogwarts-mystery", title="Harry Potter: Hogwarts Mystery", studio="", role="Associate Game Designer", year="", kind="other",
      platform="Mobile", tools="Proprietary tools, Maya", blurb="Built cinematic scenes from scripts, animation and art; tuned in spreadsheets.",
      intro="",
      sections=[dict(h="Gameplay", video="rAFYdUbWLMg", points=[
        "Designed and created cinematic scenes using a narrative script, animations and art assets within proprietary development tools and Maya.",
        "Collaborated with writers, artists and animators to ship scenes under tight deadlines.",
        "Implemented tuning and balancing within spreadsheets."])]),
 dict(slug="cozmo", title="Cozmo", studio="", role="Game Design Intern", year="", kind="other",
      platform="Cozmo, Mobile", tools="Unity", blurb="Balanced progression and economy; wrote product features as PRDs.",
      intro="",
      sections=[dict(h="Gameplay", video="DHY5kpGTsDE", points=[
        "Balanced core systems within multiple spreadsheets and tested within Unity.",
        "Tuned unlock progression, in-game economy, and growth and decay rates for the player’s stats.",
        "Used data from analysts to increase user retention.",
        "Wrote and designed new product features with PRDs to be implemented."])]),
 dict(slug="unearned-bounty", title="Unearned Bounty", studio="Extrokold Games", role="Level Designer, Game Designer (intern)", year="Summer 2017", kind="other",
      platform="PC", tools="Unity", blurb="Multiplayer maps, tutorial, ships and UI flow for a naval combat game.",
      intro="Unearned Bounty is a 3D multiplayer naval combat action game with MOBA aspects. I worked as a game design intern over the summer of 2017 at Extrokold Games.",
      sections=[dict(h="Gameplay", video="IcMnpQWds30", points=[
        "Primarily worked on the multiplayer maps, creating new ones for different modes.",
        "Revised a couple of existing maps to make the player experience more enjoyable.",
        "Designed the player tutorial, many ships with their passive and active abilities, and the UI menu flow."])]),
 dict(slug="vector", title="Vector", studio="", role="Game Design Intern", year="", kind="other",
      platform="Vector, Mobile", tools="Proprietary tools, Lua", blurb="Voice-activated Easter eggs in Lua and tuning for the games played with Vector’s cube.",
      intro="",
      sections=[dict(h="Gameplay", video="Qy2Z2TWAt6A", points=[
        "Implemented Easter eggs and blacklist words using Lua for a voice-activated system.",
        "Tuned values for the games Vector plays with his cube."])]),
]

ABOUT = [
 "I’m a gameplay designer with almost a decade of design experience across a wide range of titles. I want to make games that are viscerally entertaining and emotionally meaningful.",
 "My strengths are organizing and communicating large reference libraries for design teams, and combining that research with my design experience to solve problems.",
]
SERVICES = [
 ("Gameplay and combat design", "Enemy AI, bosses, NPCs, weapons and encounter flow."),
 ("Talks on preparing for the industry", "What studios look for and how to get ready."),
 ("Design workshops and combat deep-dives", "Hands-on sessions for teams and students."),
 ("Career and portfolio mentorship", "Mentoring at Gameheads and to interns at Electronic Arts."),
 ("Reference libraries", "Organizing research so a whole team can use it."),
]

def e(s): return html.escape(s, quote=True)

def head(title, desc, depth, path):
    p = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#ECEFF1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar">
<a class="mark" href="{p}index.html">{NAME}</a>
<nav aria-label="Main"><a href="{p}index.html#work">Work</a><a href="{p}about.html">About</a><a href="{p}about.html#contact">Contact</a></nav>
</div></header>
"""

def foot(depth):
    p = "../" * depth
    mail = f'<a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a>' if EMAIL else ""
    return f"""<footer class="foot"><div class="wrap">
<p>{NAME}, gameplay designer.</p>
<p class="links">{mail}<a href="{LINKEDIN}" rel="noopener">LinkedIn</a><a href="{EDB}" rel="noopener">Enemy Design Database</a></p>
</div></footer>
<script src="{p}assets/main.js" defer></script>
</body></html>
"""

def meta_line(pr):
    bits = [x for x in (pr["role"], "" if pr["studio"] == pr["title"] else pr["studio"], pr["year"]) if x]
    return ", ".join(bits)

def video(vid, title):
    return f"""<div class="video" data-yt="{vid}" data-title="{e(title)}">
<button type="button" aria-label="Play video: {e(title)}"><img loading="lazy" alt="" onerror="this.remove()" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg"><span class="play" aria-hidden="true"></span></button></div>"""

def index():
    feat = [p for p in PROJECTS if p["kind"] == "featured"]
    oth = [p for p in PROJECTS if p["kind"] == "other"]
    fh = "".join(f"""<li><a class="frow" href="projects/{p['slug']}.html">
<span class="ftitle">{e(p['title'])}</span><span class="fmeta">{e(meta_line(p))}</span><span class="fblurb">{e(p['blurb'])}</span></a></li>""" for p in feat)
    oh = "".join(f"""<li><a class="orow" href="projects/{p['slug']}.html">
<span class="otitle">{e(p['title'])}</span><span class="ometa">{e(p['role'])}</span><span class="oblurb">{e(p['blurb'])}</span></a></li>""" for p in oth)
    return head(f"{NAME}, gameplay designer", SITE_DESC, 0, "index.html") + f"""
<main id="main">
<section class="hero"><div class="wrap herogrid">
<div class="herotext">
<h1>I design enemies that read the player and fight back.</h1>
<p class="lede">Gameplay designer with almost a decade across combat, enemy AI and NPCs. Credits include Giant Skull, Star Wars Jedi: Survivor and Marvel’s Wolverine.</p>
<p class="cta"><a class="btn" href="#work">See the work</a><a class="btn ghost" href="about.html">About me</a></p>
</div>
<figure class="arena" aria-label="Interactive demo: a small enemy that patrols, chases, telegraphs and strikes. Move your pointer around it.">
<canvas id="arena" width="640" height="440"></canvas>
<ol class="states" id="states" aria-live="off">
<li data-s="patrol">Patrol</li><li data-s="chase">Chase</li><li data-s="windup">Telegraph</li><li data-s="strike">Strike</li><li data-s="recover">Recover</li>
</ol>
<figcaption>Move your pointer (the blue dot). It’s a five-state enemy: it gives you a readable telegraph before every hit, then leaves itself open.</figcaption>
</figure>
</div></section>

<section class="wrap work" id="work">
<h2>Work</h2>
<ul class="flist">{fh}</ul>
<h3>Other professional work</h3>
<ul class="olist">{oh}</ul>
</section>
</main>
""" + foot(0)

def project_page(pr, i):
    parts = []
    if pr["intro"]: parts.append(f'<p class="lede">{e(pr["intro"])}</p>')
    facts = []
    for k, lab in (("role","Role"),("studio","Studio"),("platform","Platform"),("tools","Tools"),("year","When")):
        if pr.get(k): facts.append(f"<div><dt>{lab}</dt><dd>{e(pr[k])}</dd></div>")
    if pr.get("link"): facts.append(f'<div><dt>Link</dt><dd><a href="{pr["link"][1]}" rel="noopener">{e(pr["link"][0])}</a></dd></div>')
    body = []
    for s in pr["sections"]:
        pts = "".join(f"<li>{e(x)}</li>" for x in s.get("points", []))
        body.append(f"""<section class="case"><div class="casetext"><h2>{e(s['h'])}</h2>{('<ul>'+pts+'</ul>') if pts else ''}</div>{video(s['video'], pr['title'] + ': ' + s['h'])}</section>""")
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    return head(f"{pr['title']} | {NAME}", pr["blurb"], 1, "") + f"""
<main id="main" class="wrap project">
<p class="crumb"><a href="../index.html#work">All work</a></p>
<h1>{e(pr['title'])}</h1>
{''.join(parts)}
<dl class="facts">{''.join(facts)}</dl>
{''.join(body)}
<p class="next">Next project: <a href="{nxt['slug']}.html">{e(nxt['title'])}</a></p>
</main>
""" + foot(1)

def about():
    sv = "".join(f"<li><strong>{e(a)}</strong><span>{e(b)}</span></li>" for a, b in ABOUT_SV())
    mail = f'<li><a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a></li>' if EMAIL else ""
    return head(f"About | {NAME}", SITE_DESC, 0, "about.html") + f"""
<main id="main" class="wrap about">
<h1>About</h1>
<div class="aboutgrid">
<div class="photo"><img src="assets/tri.jpg" alt="Portrait of {NAME}" width="480" height="600" onerror="this.parentNode.hidden=true;this.closest('.aboutgrid').classList.add('nophoto')"></div>
<div>
{''.join(f'<p class="lede">{e(t)}</p>' for t in ABOUT)}
<h2>What I offer</h2>
<ul class="services">{sv}</ul>
<h2 id="contact">Contact</h2>
<ul class="contact">{mail}<li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li><li><a href="{EDB}" rel="noopener">Enemy Design Database</a>, a reference library of enemy designs I maintain.</li></ul>
</div></div>
</main>
""" + foot(0)

def ABOUT_SV(): return SERVICES

def write(path, s):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)

# GitHub Pages serves 404.html for unknown URLs; use an absolute base so it works at any depth.
BASE = "/"  # for a project site at user.github.io/<repo>/ set this to "/<repo>/"
nf = head("Page not found | " + NAME, "Page not found.", 0, "404.html").replace('href="assets/', f'href="{BASE}assets/').replace('href="index.html', f'href="{BASE}index.html').replace('href="about.html', f'href="{BASE}about.html')
nf += '<main id="main" class="wrap project"><h1>That page isn’t here.</h1><p class="lede">The link may be old. Every project is listed on the work page.</p><p class="cta"><a class="btn" href="' + BASE + 'index.html#work">Go to the work</a></p></main>' + foot(0).replace('src="assets/', f'src="{BASE}assets/').replace('href="assets/', f'href="{BASE}assets/')
write("404.html", nf)
write("index.html", index())
write("about.html", about())
for i, p in enumerate(PROJECTS):
    write(f"projects/{p['slug']}.html", project_page(p, i))
print("built", 2 + len(PROJECTS), "pages")
