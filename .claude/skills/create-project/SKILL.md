---
name: create-project
description: Create a new NA-MIC Project Week project page from template, searching past projects for context
argument-hint: "[project-name]"
allowed-tools:
  - Read
  - Write
  - Grep
  - Glob
  - Bash
---

# Create Project Week Project

This skill creates a new project page for NA-MIC Project Week.

## Usage

Invoke with: `/create-project <project-name>`

Example: `/create-project SlicerCBM`

## Instructions

When this skill is invoked:

1. **Search for past projects** with the same or similar name:
   - Use grep/glob to find existing projects across all PW directories
   - Read the most recent versions to understand project history and context
   - Note key investigators, objectives achieved, and ongoing work

2. **Identify the current Project Week**:
   - Find the highest numbered PW directory (e.g., PW44_2026_GranCanaria)
   - This is where the new project will be created

3. **Read the current template**:
   - Located at `PW##_YEAR_Location/Projects/Template/README.md`
   - Use this exact structure for the new project

4. **Create a feature branch** (IMPORTANT - never commit to master):
   ```bash
   git checkout master
   git checkout -b PW##_YEAR_Location/ProjectName
   ```

5. **Create the project page**:
   - Folder name: Convert project name to PascalCase with no spaces/special characters
   - Path: `PW##_YEAR_Location/Projects/<FolderName>/README.md`
   - Populate with content from past projects, updated for current objectives

6. **Required fields in frontmatter**:
   - `layout: pw##-project` (match current PW number)
   - `permalink: /:path/`
   - `project_title:` Full descriptive title
   - `category:` One of: IGT and Training, DICOM, VR/AR and Rendering, Segmentation / Classification / Landmarking, Quantification and Computation, Registration, Cloud / Web, Infrastructure, Other
   - `presenter_location:` "In-person" or "Online"
   - `key_investigators:` List with name, affiliation, country

7. **Content sections**:
   - Project Description: Brief overview paragraph
   - Objective: Numbered list of specific goals
   - Approach and Plan: How objectives will be achieved
   - Progress and Next Steps: Initially placeholder, updated during event
   - Illustrations: Images/videos demonstrating the work
   - Background and References: Links to code, data, publications

8. **Commit and push the branch**:
   ```bash
   git add PW##_YEAR_Location/Projects/ProjectName/
   git commit -m "PW##_YEAR_Location: Add project ProjectName"
   git push -u origin PW##_YEAR_Location/ProjectName
   ```

9. **Create PR to upstream** (IMPORTANT: must use --head flag for fork-based PRs):
   ```bash
   # Get fork owner from origin remote
   FORK_OWNER=$(git remote get-url origin | sed 's/.*[:/]\([^/]*\)\/ProjectWeek.*/\1/')
   BRANCH=$(git branch --show-current)

   gh pr create \
     --repo NA-MIC/ProjectWeek \
     --base master \
     --head "$FORK_OWNER:$BRANCH" \
     --title "PW##: Add ProjectName project" \
     --body "## Summary
   - Add ProjectName project for PW##

   ## Key Investigators
   - Name (Affiliation)"
   ```

## Tips

- Keep the folder name concise but descriptive
- Reference past achievements in the Background section
- Link to relevant GitHub repos, documentation, and publications
- Use presenter_location "In-person" if attending in person
- NEVER commit directly to master - always use feature branches
