"""Regenerate the static pages with Python's standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = 'uploads/2/0/8/8/20880284/'
SITE = 'https://www.tptate.com'
DESCRIPTION = 'Tamara Tate, PhD, UC Irvine researcher on generative AI, writing, and AI literacy in secondary and postsecondary education; Co-PI of the IES WRITE AI Center.'

def part(name):
    return (ROOT / 'content' / (name + '.html')).read_text()

def render(title, page, content):
    home = page == 'index.html'
    canonical = SITE + ('/' if home else '/' + page)
    links = [('Research','index.html#selected-publications'), ('Projects','index.html#funded-projects'),
             ('Teaching','resources.html'), ('Speaking','index.html#speaking'), ('Media','index.html#media'),
             ('CV',ASSETS+'tate_cv.pdf')]
    active = {url: ' aria-current="page"' if url == page else '' for _,url in links}
    nav = ''.join(f'<li><a href="{url}"{active[url]}>{label}</a></li>' for label,url in links)
    page_title = 'Tamara Tate, PhD | UC Irvine' if home else title + ' | Tamara Tate, PhD'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page_title)}</title>
  <meta name="description" content="{escape(DESCRIPTION,quote=True)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{escape(page_title,quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/social-preview.png">
  <meta property="og:image:alt" content="Tamara Tate, PhD. How students become better writers. Technology and literacy.">
  <link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="wrap header-inner">
  <a class="brand" href="index.html">Tamara Tate, PhD<span>UC Irvine</span></a>
  <nav aria-label="Main navigation"><ul>{nav}</ul></nav>
</div></header>
<main class="wrap" id="main">
{content}
</main>
<footer><div class="wrap footer-inner"><span>Tamara Tate, PhD · UC Irvine</span><a href="mailto:tatet@uci.edu">tatet@uci.edu</a></div></footer>
</body>
</html>"""

def write(title,page,content):
    (ROOT/page).write_text(render(title,page,content)+'\n')

sections=('selected-publications','funded-projects','teaching','speaking','media')
homepage=f"""<div class="hero">
  <div class="hero-copy">
  {part('intro')}
  <div class="actions">
    <a class="action primary" href="#selected-publications">Explore research</a>
    <a class="action" href="resources.html">Teaching resources</a>
    <a class="action" href="{ASSETS}tate_cv.pdf">Download CV</a>
  </div>
  </div>
  <div class="portrait"><img src="{ASSETS}tate11_orig.jpg" alt="Tamara Tate" width="533" height="800" fetchpriority="high"></div>
</div>
<section class="section highlights"><h2>Current research projects</h2>{part('project-overview')}</section>
<section class="bio">{part('bio')}</section>
{part('featured')}
{''.join(part(name) for name in sections)}
<details class="section archive earlier"><summary>Conference work, resources, and earlier press coverage</summary>{part('earlier-work')}</details>"""
write('Home','index.html',homepage)
write('Teaching resources','resources.html',part('resources'))
for slug, title in [('prior-research','Prior Research'),('technology','Technology'),('writing','Writing'),('exceptional-learners','Exceptional Learners')]:
    write(title,slug+'.html',f'<section class="section archive"><h1>{title}</h1>{part(slug)}</section>')
