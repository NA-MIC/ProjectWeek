import re
import os

PROJECTS_DIR = "/Users/tkapur/repos/ProjectWeek/PW45_2026_Boston/Projects"
OUT_PATH = "/Users/tkapur/repos/ProjectWeek/PW45_2026_Boston/projects_list.md"
BASE_URL = "https://projectweek.na-mic.org/PW45_2026_Boston/Projects"


def extract_section(text, start_pattern, stop_patterns):
    m = re.search(start_pattern, text, re.MULTILINE)
    if not m:
        return ""
    rest = text[m.end():]
    stop = re.search("|".join(stop_patterns), rest, re.MULTILINE)
    chunk = rest[:stop.start()] if stop else rest
    chunk = re.sub(r'<!--.*?-->', '', chunk, flags=re.DOTALL)
    chunk = re.sub(r'<img[^>]*/?\s*>', '', chunk)
    chunk = re.sub(r'!\[.*?\]\(.*?\)', '', chunk)
    return chunk.strip()


def get_images_from_section(text, start_pattern, stop_patterns):
    """Return list of (width, url) tuples from a section."""
    m = re.search(start_pattern, text, re.MULTILINE)
    if not m:
        return []
    rest = text[m.end():]
    stop = re.search("|".join(stop_patterns), rest, re.MULTILINE)
    chunk = rest[:stop.start()] if stop else rest

    results = []
    # HTML img tags: <img width="NNN" ... src="URL" ...>
    for tag in re.finditer(r'<img\b[^>]+>', chunk):
        tag_text = tag.group()
        url_m = re.search(r'src="(https://[^"]+)"', tag_text)
        if not url_m:
            continue
        url = url_m.group(1)
        if re.search(r'youtube|youtu\.be', url, re.I):
            continue
        w_m = re.search(r'width="([0-9]+)"', tag_text)
        width = int(w_m.group(1)) if w_m else 0
        results.append((width, url))
    # Markdown images: ![alt](url)
    for m2 in re.finditer(r'!\[[^\]]*\]\((https://[^)]+)\)', chunk):
        url = m2.group(1)
        if re.search(r'youtube|youtu\.be', url, re.I):
            continue
        results.append((0, url))
    return results


def pick_best_image(text):
    """Pick the best image: prefer Illustrations section, then largest width."""
    stop = [r'^# ', r'^## ']

    # Try Illustrations section first
    illus = get_images_from_section(text, r'^# Illustrations', stop)
    if illus:
        # Pick the one with the largest declared width; fall back to first
        best = max(illus, key=lambda x: x[0])
        return best[1]

    # Fall back to any image in the file
    all_imgs = get_images_from_section(text, r'^---\s*$', [r'^\Z'])
    if not all_imgs:
        # Try whole file
        results = []
        for tag in re.finditer(r'<img\b[^>]+>', text):
            url_m = re.search(r'src="(https://[^"]+)"', tag.group())
            if url_m and not re.search(r'youtube|youtu\.be', url_m.group(1), re.I):
                w_m = re.search(r'width="([0-9]+)"', tag.group())
                results.append((int(w_m.group(1)) if w_m else 0, url_m.group(1)))
        for m2 in re.finditer(r'!\[[^\]]*\]\((https://[^)]+)\)', text):
            url = m2.group(1)
            if not re.search(r'youtube|youtu\.be', url, re.I):
                results.append((0, url))
        all_imgs = results

    if not all_imgs:
        return None
    best = max(all_imgs, key=lambda x: x[0])
    return best[1]


projects = []
for name in sorted(os.listdir(PROJECTS_DIR)):
    if name == "Template":
        continue
    readme_path = os.path.join(PROJECTS_DIR, name, "README.md")
    if not os.path.exists(readme_path):
        continue

    with open(readme_path) as f:
        text = f.read()

    title_m = re.search(r'^project_title:\s*(.+)', text, re.MULTILINE)
    if not title_m:
        continue
    title = title_m.group(1).strip().strip("'")

    lead_m = re.search(
        r'^key_investigators:.*?^\s*-\s*name:\s*([^\n]+)\n\s*affiliation:\s*([^\n]+)',
        text, re.MULTILINE | re.DOTALL)
    if lead_m:
        lead = f"{lead_m.group(1).strip()} @ {lead_m.group(2).strip()}, +"
    else:
        name_m = re.search(r'^key_investigators:.*?^\s*-\s*name:\s*([^\n]+)', text, re.MULTILINE | re.DOTALL)
        lead = (name_m.group(1).strip() + ", +") if name_m else None

    proj_url = f"{BASE_URL}/{name}/"
    img_url = pick_best_image(text)

    desc = extract_section(text, r'^# Project Description', [r'^## ', r'^# '])
    # Convert any numbered list items in description to bullets so they
    # don't interfere with the outer project numbering in the rendered markdown
    desc = re.sub(r'(?m)^\d+\.\s+', '- ', desc)

    projects.append(dict(title=title, proj_url=proj_url, img_url=img_url,
                         desc=desc, lead=lead))


lines = ["# PW45 2026 Boston — Project Links\n"]

for i, p in enumerate(projects, 1):
    lead_str = f' ({p["lead"]})' if p['lead'] else ''
    lines.append(f'{i}. **[{p["title"]}]({p["proj_url"]})**{lead_str}\n')

    if p['img_url']:
        lines.append(
            f'<a href="{p["proj_url"]}">'
            f'<img src="{p["img_url"]}" style="max-width:480px;width:100%">'
            f'</a>\n'
        )

    if p['desc']:
        lines.append(p['desc'] + '\n')

    lines.append('')

with open(OUT_PATH, 'w') as f:
    f.write('\n'.join(lines))

print(f"Written {len(projects)} projects to {OUT_PATH}")
for i, p in enumerate(projects, 1):
    img = p['img_url'] or '(none)'
    print(f"  {i:2}. {p['title'][:50]} → {img[:60]}")
