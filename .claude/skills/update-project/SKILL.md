---
name: update-project
description: Update an existing project page - creates branch, helps with edits, creates PR when ready
argument-hint: "[project-name] [action]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
---

# Update Project

This skill helps update an existing NA-MIC Project Week project page.

## Usage

```
/update-project ProjectName start    # Start editing (creates branch)
/update-project ProjectName          # Continue editing (shows current state)
/update-project ProjectName finish   # Commit, push, and create PR
```

## Actions

### `start` - Begin editing session

1. Find the project in the current Project Week directory
2. Create a feature branch:
   ```bash
   git checkout master
   git pull upstream master  # sync first
   git checkout -b PW##_YEAR_Location/ProjectName-updates
   ```
3. Show current project README for reference
4. Ready for user to request changes

### (no action) - Continue editing

1. Check we're on the correct branch
2. Show current state of project README
3. Show uncommitted changes if any
4. Ready for user to request more changes

### `finish` - Complete and create PR

1. Show diff of all changes made
2. Ask user to confirm
3. Commit changes:
   ```bash
   git add PW##_YEAR_Location/Projects/ProjectName/
   git commit -m "PW## ProjectName: Update <summary of changes>"
   ```
4. Push branch:
   ```bash
   git push -u origin PW##_YEAR_Location/ProjectName-updates
   ```
5. Check if PR already exists for this branch:
   ```bash
   FORK_OWNER=$(git remote get-url origin | sed 's/.*[:/]\([^/]*\)\/ProjectWeek.*/\1/')
   BRANCH=$(git branch --show-current)
   gh pr list --repo NA-MIC/ProjectWeek --head "$FORK_OWNER:$BRANCH" --json url
   ```
6. Create PR if none exists (IMPORTANT: must use --head flag for fork-based PRs):
   ```bash
   gh pr create \
     --repo NA-MIC/ProjectWeek \
     --base master \
     --head "$FORK_OWNER:$BRANCH" \
     --title "PW## ProjectName: <brief summary of updates>" \
     --body "## Summary
   - <bullet points describing changes made>"
   ```

   **IMPORTANT:** This is updating an EXISTING project, not adding a new one. The PR title should describe
   what was updated (e.g., "PW44 SlicerCBM: Update progress and add screenshots"), NOT "Add project".

7. Return PR URL to user

## Finding the project

Search in order:
1. Current PW directory: `PW##_YEAR_Location/Projects/ProjectName/`
2. Case-insensitive glob if exact match not found
3. Show options if multiple matches

## Tips

- User can make multiple rounds of changes before `finish`
- If user wants to abandon changes: `git checkout master` discards uncommitted work
- Branch naming includes `-updates` suffix to distinguish from new project branches
- Commit message should summarize what was actually changed (objectives, progress, etc.)
