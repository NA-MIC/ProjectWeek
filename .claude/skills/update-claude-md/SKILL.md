---
name: update-claude-md
description: Update CLAUDE.md based on latest repo documentation for project creation
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
---

# Update CLAUDE.md

This skill updates CLAUDE.md to reflect the latest documentation in the repository.

## Instructions

1. **Find the current Project Week:**
   ```bash
   ls -d PW*_*/ | sort -V | tail -1
   ```

2. **Read ALL relevant documentation:**
   - `PW##_YEAR_Location/README.md` - project categories in frontmatter, event details
   - `PW##_YEAR_Location/Projects/Template/README.md` - current template structure
   - `PW##_YEAR_Location/ContributingProjectPages.md` - contribution guidelines, PR workflow
   - `.github/ISSUE_TEMPLATE/project.yml` - GitHub issue-based project creation
   - `.github/workflows/project-page-pull-request.yml` - automated PR creation, **branch naming convention**
   - `MAINTAINERS.md` - maintainer workflow info
   - `README.md` - upstream repo URL, general info

3. **Check git configuration:**
   ```bash
   git remote -v  # Get upstream URL
   git branch -a  # Understand branch structure
   ```

4. **List available skills:**
   ```bash
   ls .claude/skills/
   ```

5. **Update CLAUDE.md with these sections:**
   - Repository Overview (brief)
   - Key Documentation (references to actual files, not duplicated content)
   - Contribution Workflow (fork-based, PR to master, branch naming)
   - Commit Message Convention (from git log examples)
   - Available Skills (from .claude/skills/)
   - Commands (bundle exec jekyll serve, update-from-upstream.sh)

## Key things to capture:

- **CRITICAL: Never commit to master** - always use feature branches
- **Branch naming:** `PW##_YEAR_Location/ProjectName` (from workflow yml)
- **Full workflow:** branch → commit → push → PR to upstream
- **Upstream URL:** from git remote or README
- **PR target:** upstream `master` branch
- **Two project creation options:** GitHub issue OR manual PR (both use branches)
- **Commit format:** `PW##_YEAR_Location: Add project ProjectName`

## Do NOT:

- Copy/paste full templates or documentation into CLAUDE.md
- Remove existing useful information without reason
- Miss the contribution workflow details (this was missed before!)
- Forget to check GitHub Actions workflows for automation details
