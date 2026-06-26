import re
import os
from urllib.parse import quote

PROJECTS_DIR = "/Users/tkapur/repos/ProjectWeek/PW45_2026_Boston/Projects"
OUT_PATH = "/Users/tkapur/repos/ProjectWeek/PW45_2026_Boston/projects_list.md"
BASE_URL = "https://projectweek.na-mic.org/PW45_2026_Boston/Projects"
RAW_BASE = "https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects"

# Manual image overrides: folder name → image URL to use instead of auto-selected
IMAGE_OVERRIDES = {
    "AiAgentForSlicerautomateddentaltools":
        "https://github.com/user-attachments/assets/32b13db1-2e45-4067-8fd6-1d18a84fd662",
    "AiModelDevelopmentForLungUltrasoundAnalysis":
        "https://github.com/user-attachments/assets/22010591-075d-4910-9e31-184b91568813",
    "CastInterfaceModuleFor3DSlicerServiceProvidersImageDisplayClientAndHub":
        "https://github.com/user-attachments/assets/7c8aefc0-d697-4813-9193-53fe08944c99",
    "ClinicalInformationExtractionViaLocallyFineTunedLlms":
        "https://github.com/user-attachments/assets/ab930885-cd8a-4af6-9f1b-c9d12d150dcb",
    "ExploringUltrasoundMultiFrameImageStorageStructuredReportSupportForSlicerOhif":
        "https://github.com/user-attachments/assets/6574e377-dc30-4454-9938-78fb3db31f39",
    "FanMaskAndOcrBoundBoxEditingForOhifBasedDicomDeIdentificationVerificationMode":
        "https://github.com/user-attachments/assets/f4a099f4-5f71-40a3-a22f-f84ace253d0e",
    "Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis":
        "https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/Mr2CbctRestoringAndExtendingAutomatedCbctMriRegistrationForTmjAnalysis/Screenshot01.jpg",
    "SliceyAiCodingAgentFor3DSlicer":
        "https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW45_2026_Boston/Projects/SliceyAiCodingAgentFor3DSlicer/SliceyScreenshot01.jpg",
    "Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer":
        "https://github.com/user-attachments/assets/51fcdf47-e1a7-4318-ac84-38637db7b6bc",
}


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
        url_m = re.search(r'src="([^"]+)"', tag_text)
        if not url_m:
            continue
        url = url_m.group(1)
        if re.search(r'youtube|youtu\.be', url, re.I):
            continue
        w_m = re.search(r'width="([0-9]+)"', tag_text)
        width = int(w_m.group(1)) if w_m else 0
        results.append((width, url))
    # Markdown images: ![alt](url)
    for m2 in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', chunk):
        url = m2.group(1)
        if re.search(r'youtube|youtu\.be', url, re.I):
            continue
        results.append((0, url))
    return results


def resolve_img_url(url, folder):
    """Convert a relative image path to a raw GitHub URL."""
    if url.startswith('http'):
        return url
    clean = url[2:] if url.startswith('./') else url.lstrip('/')
    return f"{RAW_BASE}/{folder}/{quote(clean)}"


def pick_best_image(text, folder):
    """Pick the best image: prefer Illustrations section, then largest width."""
    stop = [r'^# ', r'^## ']

    # Try Illustrations section first
    illus = get_images_from_section(text, r'^# Illustrations', stop)
    if illus:
        best = max(illus, key=lambda x: x[0])
        return resolve_img_url(best[1], folder)

    # Fall back to any image in the file
    all_imgs = get_images_from_section(text, r'^---\s*$', [r'^\Z'])
    if not all_imgs:
        results = []
        for tag in re.finditer(r'<img\b[^>]+>', text):
            url_m = re.search(r'src="([^"]+)"', tag.group())
            if url_m and not re.search(r'youtube|youtu\.be', url_m.group(1), re.I):
                w_m = re.search(r'width="([0-9]+)"', tag.group())
                results.append((int(w_m.group(1)) if w_m else 0, url_m.group(1)))
        for m2 in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', text):
            url = m2.group(1)
            if not re.search(r'youtube|youtu\.be', url, re.I):
                results.append((0, url))
        all_imgs = results

    if not all_imgs:
        return None
    best = max(all_imgs, key=lambda x: x[0])
    return resolve_img_url(best[1], folder)


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

    # Extract GitHub repo URL — prefer Background and References section
    repo_url = None
    repo_name = None
    bg_section = extract_section(text, r'^# Background and References', [r'^# '])
    search_texts = [bg_section, text] if bg_section else [text]
    for search in search_texts:
        for line in search.splitlines():
            if re.match(r'^\s*-\s*\[\d+\]', line):  # skip citation lines like "- [1] ..."
                continue
            m2 = re.search(r'https://github\.com/([^/\s")\]>]+/[^/\s")\]>]+)', line)
            if m2 and 'user-attachments' not in m2.group(0):
                repo_url = m2.group(0).rstrip('.,>')
                repo_name = m2.group(1).rstrip('.,>')
                break
        if repo_url:
            break

    proj_url = f"{BASE_URL}/{name}/"
    img_url = IMAGE_OVERRIDES.get(name) or pick_best_image(text, name)

    desc = extract_section(text, r'^# Project Description', [r'^## ', r'^# '])
    # Convert any numbered list items in description to bullets so they
    # don't interfere with the outer project numbering in the rendered markdown
    desc = re.sub(r'(?m)^\d+\.\s+', '- ', desc)

    projects.append(dict(title=title, proj_url=proj_url, img_url=img_url,
                         desc=desc, lead=lead, repo_url=repo_url,
                         repo_name=repo_name if repo_url else None))


lines = ["# Project Week# 45, June 22-26, 2026 @ MIT, Boston, USA\n"]

for i, p in enumerate(projects, 1):
    lead_str = f' ({p["lead"]})' if p['lead'] else ''
    repo_str = f' ([{p["repo_name"]}]({p["repo_url"]}))' if p['repo_url'] else ' (no github repo yet)'
    lines.append(f'{i}. **[{p["title"]}]({p["proj_url"]})**{lead_str}{repo_str}\n')

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
