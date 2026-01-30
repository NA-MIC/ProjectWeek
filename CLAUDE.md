# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

NA-MIC Project Week website - Jekyll static site at https://projectweek.na-mic.org. Biannual hackathon for medical image computing (3D Slicer, VTK, ITK, OHIF).

## Key Documentation

- **Current event:** Find highest numbered `PW##_YEAR_Location/` directory
- **Project template:** `PW##_YEAR_Location/Projects/Template/README.md`
- **Contributing guide:** `PW##_YEAR_Location/ContributingProjectPages.md`
- **Categories:** Listed in `PW##_YEAR_Location/README.md` frontmatter (`project_categories`)

## Contribution Workflow

**IMPORTANT: Never commit directly to master. Always use branches and PRs.**

### Git Remote Setup

This repo uses a fork-based workflow with two remotes:
- `origin` - Your fork (e.g., `benzwick/ProjectWeek`)
- `upstream` - Main repo (`NA-MIC/ProjectWeek`)

Check remotes with: `git remote -v`

### Workflow Steps

1. Create feature branch: `PW##_YEAR_Location/ProjectName`
2. Commit changes to branch
3. Push branch to origin (your fork)
4. Create PR to upstream `master`

**For new projects:**
```bash
git checkout -b PW44_2026_GranCanaria/ProjectName
# create project files
git add PW44_2026_GranCanaria/Projects/ProjectName/
git commit -m "PW44_2026_GranCanaria: Add project ProjectName"
git push -u origin PW44_2026_GranCanaria/ProjectName
```

**For project updates:**
```bash
git checkout -b PW44_2026_GranCanaria/ProjectName-updates
# make changes
git commit -m "PW44 ProjectName: Update Objectives"
git push -u origin PW44_2026_GranCanaria/ProjectName-updates
```

### Creating Pull Requests

**IMPORTANT:** When creating PRs from a fork, you MUST use the `--head` flag to specify the fork owner and branch.

First, get the fork owner from the origin remote:
```bash
git remote get-url origin | sed 's/.*[:/]\([^/]*\)\/ProjectWeek.*/\1/'
```

Then create the PR with the correct flags:
```bash
gh pr create \
  --repo NA-MIC/ProjectWeek \
  --base master \
  --head FORK_OWNER:BRANCH_NAME \
  --title "PW44: Add ProjectName project" \
  --body "## Summary
- Brief description of changes

## Key Investigators
- Name (Affiliation)"
```

**Example** (for benzwick fork):
```bash
gh pr create \
  --repo NA-MIC/ProjectWeek \
  --base master \
  --head benzwick:PW44_2026_GranCanaria/SlicerCBM \
  --title "PW44: Add SlicerCBM project" \
  --body "## Summary
- Add SlicerCBM project for PW44

## Key Investigators
- Ben Zwick (UWA, Talk2View)"
```

**Upstream:** https://github.com/NA-MIC/ProjectWeek

## Commit Message Convention

```
PW44_2026_GranCanaria: Add project ProjectName
PW44 ProjectName: Update Objectives
```

## Available Skills

Skills in `.claude/skills/`:

- `/create-project [name]` - Create a new project page on a feature branch
- `/update-project [name] [start|finish]` - Update existing project with branch/PR workflow
- `/update-claude-md` - Update CLAUDE.md based on latest repo documentation

## Commands

```bash
bundle exec jekyll serve          # Local development
./update-from-upstream.sh         # Sync master with upstream and push
```
