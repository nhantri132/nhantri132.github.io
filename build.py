#!/usr/bin/env python3
"""Generates the static site. Edit CONTENT below, run `python3 build.py`, commit the output.
GitHub Pages serves the generated .html files directly; Python is only needed on your machine."""
import html, os

NAME = "Tri Nguyen"
EMAIL="nhantri132@gmail.com"
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
 dict(slug="clawface", title="Clawface", studio="", role="Lead Game Designer", year="", kind="related",
      platform="Windows, Mac, Linux", tools="Unity",
      blurb="Design lead on a twin-stick bullet hell shooter: six weapons, enemies that push the player to move, and dynamic levels.",
      intro="Clawface is a twin-stick bullet hell shooter. I designed the weapon functions and balance, enemy AI behavior and dynamic level design, and was creative director for a team of 18, keeping one consistent vision from pre-production to release while hitting multiple deadlines.",
      article=("Solving the Combat Design Puzzle of Clawface", "https://trigrows.medium.com/solving-the-combat-puzzle-of-clawface-661e887d40c0"),
      sections=[
        dict(h="Gameplay", video="A41UPDj2UNg"),
        dict(h="Depth from limited scope", points=[
          "The scope was small, so the combat had to get depth from a few pieces. I built reusable pieces that combine into many permutations: the weapons, a dynamic level system and the enemies, with enemy color swaps as one example of reuse.",
          "A score-driven leaderboard gave players a reason to keep playing for the top spot."]),
        dict(h="Six weapons, any two at once", points=[
          "Players dual-wield any two of six weapons, which supports different skill levels and preferences. Harder-to-use weapons reward skill with high damage.",
          "The set: Blaster (rapid fire, small hitbox), Boomerang (bounces off walls), Geyser (high damage, slow), LightningGun (chains between targets), Missile (explosive splash) and SpreadGun (strong up close, weak at range).",
          "Melee weapons and reloading were tested and then cut for concepts players understand immediately.",
          "About a month after release, analytics showed almost an even spread of use across the weapons."]),
        dict(h="Keeping players moving", points=[
          "The goal was constant movement and chained kills, and the risk was players kiting enemies around the arena. Some enemies explode near the player and the Red Bouncer damages on contact, which pushes players to keep moving.",
          "To balance that, an enemy below a health threshold becomes stunned. The player can move in and eat it to recover health. Stunned enemies explode after about 3 seconds and take the health with them.",
          "Eating raises the combo multiplier by 2x instead of 1x, so players going for the leaderboard eat enemies even at full health.",
          "Levels change mid-wave. Each tile is a pit (projectiles pass, characters cannot), a floor (both pass) or a wall (neither), so intensity rises and falls."]),
        dict(h="Balancing eat, dash and shoot", points=[
          "Eating became multi-directional after testing showed players had to think too hard about facing direction. A failed eat locks out dash and shoot, which stops button spamming.",
          "The continuous 0 to 100 percent health bar was too vague in the chaos. I switched to 9 discrete units: eating recovers 1 and getting hurt costs 3. Difficulty levels can change just those values.",
          "Players lost track of their aim with mouse and keyboard, so each weapon got a small laser line.",
          "Dash was the main way to avoid damage, so players can dash while shooting or eating. Cooldown and distance were tuned up to release.",
          "My takeaway: tiny changes can have huge effects on the player experience."])]),
 dict(slug="wwe-undefeated", title="WWE Undefeated", studio="", role="Systems Designer", year="", kind="related",
      platform="Mobile", tools="Unity", blurb="Led the Class Moves overhaul of meta-systems and combat; designed combat passives; scripted AI bots with behavior trees.",
      intro="WWE Undefeated is a mobile wrestling game. I worked across its meta-systems, combat and player AI.",
      sections=[
        dict(h="Gameplay", video="Xv6aqndl5Hk"),
        dict(h="Class Moves update", points=[
          "Led the overhaul of the game\u2019s meta-systems and combat to simplify deckbuilding and add variety to online matches.",
          "The release improved KPIs and retention."]),
        dict(h="Style: passive abilities", points=[
          "Designed the passive abilities that trigger during combat and aligned them with the combat designers\u2019 vision for each character.",
          "Implemented them in spreadsheets and Unity."]),
        dict(h="AI bots", points=[
          "Designed and scripted player AI bots using Unity behavior trees."]),
        dict(h="Tutorial", points=[
          "Wrote, designed and scripted the full tutorial, iterating on each release based on data."])]),
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
 "I\u2019m a gameplay designer with almost a decade of design experience across a wide range of titles. I specialize in combat design, particularly enemy AI design. My goal is to create enemies that make the world feel real, encourage the use of the entire hero kit, and challenge the player in a viscerally entertaining way.",
 "I love video games for the way players get lost in worlds and are encouraged to interact with the systems, mechanics, story, and themes in a way that\u2019s richer than any other art form out there.",
]
SERVICES = [
 ("Talks on preparing for the industry", "What studios look for and how to get ready. Talks at University of Utah, University of North Texas, University of Houston, and NYU."),
 ("Design workshops and combat deep-dives", "Hands-on sessions for teams and students. Workshop at University of Utah."),
 ("Career and portfolio mentorship", "Mentoring at Gameheads, EAE, Gamecraft, Electronic Arts interns, and Coog Interactive."),
]


# "Stuff I like": counts only, never ratings. 1 square = 50 items.
# Counts below come from the Goodreads, Letterboxd and RYM exports (Oct 2026). Games is from Backloggd stats screenshots (1,390 played).
STUFF = [
 dict(n=1390, big="1,390+", unit="games", color="blue", detail=["Finished 1,200+ of them, across 11 platforms. Mostly adventure, shooter, indie and RPG.", "Favorite: Disco Elysium"]),
 dict(n=692, big="690+", unit="books and comics", color="yellow", detail=["About 140,000 pages from 270+ authors.", "Recent favorite: House of X / Powers of X"]),
 dict(n=1494, big="1,490+", unit="films", color="red", detail=["Releases from 1902 to 2026, with the most from the 2010s.", "Favorite: Everything, Everywhere, All at Once"]),
 dict(n=3624, big="3,600+", unit="albums", color="blue", detail=["From 1,800+ artists, with releases from 1952 to 2026.", "Favorite: Kendrick Lamar\u2019s To Pimp a Butterfly"]),
 dict(n=187, big="185+", unit="TV seasons", color="yellow", detail=["A lot of anime, animation, sitcoms and Marvel series.", "Favorite: How To with John Wilson"]),
]
STUFF_TOTAL = "7,000+"
STUFF_SQ = 50

import hashlib, pathlib
ASSET_V = hashlib.md5(b"".join(pathlib.Path(__file__).parent.joinpath("assets", f).read_bytes() for f in ("style.css", "main.js"))).hexdigest()[:8]  # cache-busting for CSS/JS links

def e(s): return html.escape(s, quote=True)

COLORS = {"giant-skull":"blue","marvels-wolverine":"yellow","star-wars-jedi-survivor":"red","clawface":"blue","wwe-undefeated":"red"}
CYCLE = ["blue","yellow","red"]
def color_of(pr, i=0): return COLORS.get(pr["slug"]) or CYCLE[i % 3]

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
<meta name="theme-color" content="#F7F8FA">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Caveat:wght@700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{p}assets/style.css?v={ASSET_V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar">
<a class="mark" href="{p}index.html"><span class="pips" aria-hidden="true"><i></i><i></i><i></i></span>{NAME}</a>
<nav aria-label="Main"><a href="{p}index.html#work">Work</a><a href="{p}about.html">About</a></nav>
</div></header>
"""

def foot(depth):
    p = "../" * depth
    mail = f'<a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a>' if EMAIL else ""
    return f"""<footer class="foot"><div class="wrap">
<p>{NAME}, gameplay designer.</p>
<p class="links">{mail}<a href="{LINKEDIN}" rel="noopener">LinkedIn</a><a href="{EDB}" rel="noopener">Enemy Design Database</a></p>
</div></footer>
<script src="{p}assets/main.js?v={ASSET_V}" defer></script>
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
    rel = [p for p in PROJECTS if p["kind"] == "related"]
    oth = [p for p in PROJECTS if p["kind"] == "other"]
    fh = "".join(f"""<li><a class="fcard c-{color_of(p)}" href="projects/{p['slug']}.html">
<span class="ftitle">{e(p['title'])}</span><span class="fmeta">{e(meta_line(p))}</span><span class="fblurb">{e(p['blurb'])}</span></a></li>""" for p in feat)
    rh = "".join(f"""<li><a class="rcard" href="projects/{p['slug']}.html">
<span class="rtab c-{color_of(p)}">{e(p['role'])}</span><span class="rtitle">{e(p['title'])}</span><span class="rblurb">{e(p['blurb'])}</span></a></li>""" for p in rel)
    oh = "".join(f"""<li><a class="trow" href="projects/{p['slug']}.html">
<span class="pip c-{CYCLE[k % 3]}" aria-hidden="true"></span><span class="otitle">{e(p['title'])}</span><span class="ometa">{e(p['role'])}</span><span class="oblurb">{e(p['blurb'])}</span></a></li>""" for k, p in enumerate(oth))
    return head(f"{NAME}, gameplay designer", SITE_DESC, 0, "index.html") + f"""
<main id="main">
<section class="hero"><div class="wrap herogrid">
<div class="herotext">
<h1>Combat design with personality and depth</h1>
<p class="brandline">Gameplay designer with almost a decade across combat and enemy AI. Every solution comes with a reference, from prototype to ship.</p>
<p class="cta"><a class="btn" href="#work">See the work</a><a class="btn ghost" href="about.html">About me</a></p>
</div>
<figure class="arena" id="demo">
<p class="note" aria-hidden="true">this is basically what i do every day<svg viewBox="0 0 60 50" width="60" height="50"><path d="M6 6 C 30 4, 50 18, 46 42" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M36 36 L46 43 L52 31" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></p>
<span class="reg" aria-hidden="true">demo area</span>
<div class="formhead"><strong>Attack frame data</strong><span class="formnote">Illustrative numbers</span></div>
<canvas id="fd" width="640" height="320" role="img" aria-label="Training-mode view of a stick figure throwing a punch at a dummy, with hurtboxes, hitbox and pushbox drawn over it."></canvas>
<ul class="legend" aria-label="Box colors"><li><i class="k kg"></i>Hurtbox</li><li><i class="k kr"></i>Hitbox</li><li><i class="k kb"></i>Pushbox</li></ul>
<div class="fdctl">
<button type="button" class="fdbtn" id="fd-play">Pause</button>
<button type="button" class="fdbtn" id="fd-prev">Step back</button>
<button type="button" class="fdbtn" id="fd-next">Step forward</button>
<button type="button" class="fdbtn" id="fd-hb" aria-pressed="true">Hitboxes on</button>
<div class="seg" role="group" aria-label="Move"><button type="button" class="fdbtn" data-move="jab" aria-pressed="true">Jab</button><button type="button" class="fdbtn" data-move="heavy" aria-pressed="false">Heavy</button></div>
</div>
<div class="fdscrub"><label for="fd-scrub">Frame <span id="fd-frame">1 / 1</span></label><input type="range" id="fd-scrub" min="0" max="0" value="0"></div>
<ol class="framebar" id="fd-bar" aria-hidden="true"></ol>
<dl class="fdata" id="fd-data">
<div class="d"><dt>Damage</dt><dd id="d-dmg"></dd></div>
<div class="d st"><dt>Startup</dt><dd id="d-st"></dd></div>
<div class="d ac"><dt>Active</dt><dd id="d-ac"></dd></div>
<div class="d re"><dt>Recovery</dt><dd id="d-re"></dd></div>
<div class="d"><dt>On block</dt><dd id="d-ob"></dd></div>
<div class="d"><dt>On hit</dt><dd id="d-oh"></dd></div>
</dl>
</figure>
</div></section>

<section class="wrap work" id="work">
<h2>Work</h2>
<div class="fwrap"><p class="note n-gs" aria-hidden="true">where i’m at now<svg viewBox="0 0 60 50" width="60" height="50"><path d="M6 6 C 30 4, 50 18, 46 42" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M36 36 L46 43 L52 31" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></p><ul class="flist">{fh}</ul></div>
<h3 class="hnote">Related work<span class="note n-old" aria-hidden="true"><svg viewBox="0 0 60 50" width="60" height="50"><path d="M56 10 C 40 6, 22 14, 8 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M8 18 L7 31 L20 33" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>oldies but goodies</span></h3>
<ul class="rlist">{rh}</ul>
<h3>Earlier work</h3>
<ul class="table"><li class="thead" aria-hidden="true"><span></span><span>Project</span><span>Role</span><span>What I did</span></li>{oh}</ul>
</section>

</main>
""" + foot(0)

def project_page(pr, i):
    c = color_of(pr, i)
    lede = f'<p class="lede">{e(pr["intro"])}</p>' if pr["intro"] else ""
    art = pr.get("article")
    article_html = f'<p class="article">Full write-up: <a href="{art[1]}" rel="noopener">{e(art[0])}</a>, on Medium.</p>' if art else ""
    facts = []
    for k, lab in (("role","Role"),("studio","Studio"),("platform","Platform"),("tools","Tools"),("year","When")):
        if pr.get(k): facts.append(f"<div><dt>{lab}</dt><dd>{e(pr[k])}</dd></div>")
    if pr.get("link"): facts.append(f'<div><dt>Link</dt><dd><a href="{pr["link"][1]}" rel="noopener">{e(pr["link"][0])}</a></dd></div>')
    body = []
    for n, s in enumerate(pr["sections"]):
        pts = "".join(f"<li>{e(x)}</li>" for x in s.get("points", []))
        vid = video(s['video'], pr['title'] + ': ' + s['h']) if s.get('video') else ""
        inner = ("<ul>" + pts + "</ul>" if pts else "") + vid
        layout = "two" if (pts and vid) else ("video" if vid else "one")
        body.append(f"""<section class="case"><h2 class="c-{CYCLE[(n + 1) % 3]}">{e(s['h'])}</h2><div class="casebody {layout}">{inner}</div></section>""")
    nx = PROJECTS[(i + 1) % len(PROJECTS)]
    return head(f"{pr['title']} | {NAME}", pr["blurb"], 1, "") + f"""
<main id="main" class="wrap project">
<p class="crumb"><a href="../index.html#work">All work</a></p>
<header class="sheet">
<div class="sheet-title c-{c}"><h1>{e(pr['title'])}</h1></div>
<dl class="facts">{''.join(facts)}</dl>
<div class="sheet-memo"><span class="memolabel">Summary</span>{lede}{article_html}</div>
</header>
{''.join(body)}
<a class="nextcard c-{color_of(nx, i + 1)}" href="{nx['slug']}.html"><span>Next project</span><strong>{e(nx['title'])}</strong></a>
</main>
""" + foot(1)


def stuff_html():
    out = []
    for k, it in enumerate(STUFF):
        sq = "".join("<i></i>" for _ in range(round(it["n"] / STUFF_SQ)))
        out.append(f"""<li><button type="button" class="srow c-{it['color']}" aria-expanded="{'true' if k == 0 else 'false'}">
<span class="snum"><strong>{e(it['big'])}</strong><span>{e(it['unit'])}</span></span>
<span class="ssq" aria-hidden="true">{sq}</span>
<span class="sdetail">{" ".join(f"<span>{e(d)}</span>" for d in it['detail'])}</span></button></li>""")
    return "".join(out)

def about():
    sv = "".join(f"<li><span class=\"pip c-{CYCLE[k % 3]}\" aria-hidden=\"true\"></span><strong>{e(a)}</strong><span>{e(b)}</span></li>" for k, (a, b) in enumerate(ABOUT_SV()))
    mail = f'<li><a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a></li>' if EMAIL else ""
    return head(f"About | {NAME}", SITE_DESC, 0, "about.html") + f"""
<main id="main" class="wrap about">
<h1 class="hnote">About<span class="note n-old" aria-hidden="true"><svg viewBox="0 0 60 50" width="60" height="50"><path d="M56 10 C 40 6, 22 14, 8 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M8 18 L7 31 L20 33" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>that\u2019s me!</span></h1>
<div class="aboutgrid">
<div class="photo"><img src="assets/tri.jpg" alt="{NAME} throwing a kick at the camera, in glasses and a pink shirt" width="720" height="1104" onerror="this.parentNode.hidden=true;this.closest('.aboutgrid').classList.add('nophoto')"></div>
<div class="bio">{''.join(f'<p>{e(t)}</p>' for t in ABOUT)}</div>
</div>

<section id="stuff" class="stuff">
<h2 class="hnote">Stuff I like<span class="note n-old" aria-hidden="true"><svg viewBox="0 0 60 50" width="60" height="50"><path d="M56 10 C 40 6, 22 14, 8 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M8 18 L7 31 L20 33" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>yes, I log everything</span></h2>
<p class="stufflead"><strong>{STUFF_TOTAL}</strong> games, books, films, albums and TV seasons, and counting. Each square is {STUFF_SQ} of them. Tap a row for more.</p>
<ul class="stufflist">{stuff_html()}</ul>
</section>

<section id="how">
<h2>How I work</h2>
<ol class="steps">
<li class="step s-blue"><h3>Reference</h3><p>I keep a manually updated library of references and am inspired by the best.</p></li>
<li class="step s-yellow"><h3>Translate</h3><p>I communicate the ideas to all disciplines so the team and I can build in the same direction.</p></li>
<li class="step s-red"><h3>Build</h3><p>I own the enemy systems end to end and build them from the ground up, from prototype to ship.</p></li>
</ol>
</section>

<section id="library">
<h2 class="hnote">Reference library<span class="note n-old" aria-hidden="true"><svg viewBox="0 0 60 50" width="60" height="50"><path d="M56 10 C 40 6, 22 14, 8 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M8 18 L7 31 L20 33" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>the inside of my brain</span></h2>
<ul class="table">
<li><a class="trow" href="{EDB}" rel="noopener"><span class="pip c-blue" aria-hidden="true"></span><span class="otitle">Enemy Design Database</span><span class="ometa">Database</span><span class="oblurb">A searchable catalog of enemy designs, mainly from action-adventure games: type, size, weapons, actions, reactions and video references. I built it and maintain it.</span></a></li>
<li><a class="trow" href="https://www.youtube.com/@tringuyen-combatdesign" rel="noopener"><span class="pip c-yellow" aria-hidden="true"></span><span class="otitle">Combat animation references</span><span class="ometa">YouTube</span><span class="oblurb">A reference library of combat animation, organized for combat design.</span></a></li>
</ul>
</section>

<section id="offer">
<h2 class="hnote">What I offer<span class="note n-old" aria-hidden="true"><svg viewBox="0 0 60 50" width="60" height="50"><path d="M56 10 C 40 6, 22 14, 8 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M8 18 L7 31 L20 33" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>a professional yapper</span></h2>
<ul class="table services">{sv}</ul>
</section>

<section id="contact">
<h2>Contact</h2>
<ul class="contact c-blue">{mail}<li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li></ul>
</section>
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
