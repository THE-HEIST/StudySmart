 Git & GitHub guide for StudySmart team

Goal: after reading this, you can work on your own branch, push/pull to the right place, and open a pull request to merge your work. No prior Git knowledge assumed.

## What Git and GitHub are

Git tracks your code history on your machine — each "commit" is a save point you can return to. GitHub hosts the team's shared copy online. You pull code down from GitHub, work locally, then push back up.

Team rule number one: **nobody codes directly on the `main` branch**. Everyone works on their own branch, then opens a pull request so the team reviews before it merges into `main`.

## First-time setup

Do this once per machine.

```bash
# Tell Git who you are (shows in commit history)
git config --global user.name "Nguyen Van A"
git config --global user.email "your-email@gmail.com"

# Clone the project
git clone https://github.com/<org-name>/The-Black-Opal.git
cd The-Black-Opal
```

If GitHub asks for a password when you push: GitHub no longer accepts account passwords — you need a Personal Access Token. Go to GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic), tick the `repo` scope, and paste that token as your password. Save it somewhere — it only shows once.

## The daily loop

This is the part that matters — memorize these 6 steps and you can work in a team.

### Step 1: Get the latest main

Always start from an up-to-date main, otherwise your branch builds on stale code:

```bash
git checkout main
git pull origin main
```

### Step 2: Create your own branch

```bash
git checkout -b feature/login
```

`-b` means create and switch in one go. Name it after the task: `feature/login`, `feature/priority-ranking`, `fix/sort-bug`. No spaces.

Check which branch you're on:

```bash
git branch
# the * marks your current branch
```

### Step 3: Code, then commit

Work normally. When you finish a meaningful chunk (a working function, a fixed bug), save a checkpoint:

```bash
git status                       # see what changed
git add src/core/login.py        # pick a file to include
git add .                        # or include everything
git commit -m "Add login with sha256 hashing"
```

Write commit messages that say **what you did**: "Add auto-increment id to LangaDB", "Fix reversed sort order". Not "update", "fix bug", "abc" — two weeks later nobody knows what those mean.

Commit small and often. One giant "did everything" commit is hard to review and hard to undo when something breaks.

### Step 4: Push your branch to GitHub

```bash
git push origin feature/login
```

On the first push of a branch, Git may suggest a longer command (`--set-upstream`) — copy and run it; after that plain `git push` works.

### Step 5: Open a pull request on GitHub

1. Open the repo on GitHub. You'll usually see a yellow banner "feature/login had recent pushes" with a **Compare & pull request** button — click it. If not, go to the **Pull requests** tab → **New pull request**, set `base: main` ← `compare: feature/login`.
2. Give it a clear title and a few lines of description: what you did, whether you tested it, anything reviewers should watch for.
3. Click **Create pull request**.
4. Ask the team to review. If they request changes, just fix locally, commit, and push to the same branch — the PR updates itself; no new PR needed.
5. Once approved, click **Merge pull request** on GitHub.

### Step 6: Clean up after the merge

```bash
git checkout main
git pull origin main             # get main with your merged code
git branch -d feature/login      # delete the old branch locally
```

Next task → back to Step 1 with a fresh branch.

## When you hit a conflict

Conflicts happen when you and someone else changed the same lines. GitHub shows "This branch has conflicts" on the PR. Fix it locally:

```bash
git checkout feature/login
git pull origin main
```

Git names the conflicting files. Open one and you'll see:

```
<<<<<<< HEAD
    your code
=======
    their code
>>>>>>> main
```

Edit that block into the correct final version (keep yours, keep theirs, or combine), and **delete all three marker lines** `<<<<<<<`, `=======`, `>>>>>>>`. Then:

```bash
git add .
git commit -m "Resolve conflict with main"
git push origin feature/login
```

The PR stops complaining. If you're not sure whose version to keep, ask the person who wrote the other side — don't guess.

## Project-specific notes

- **`session.txt` and `venv/` must never be committed** — they're in `.gitignore`. If `git status` still shows them, tell the team.
- **Watch out for `users.json` and `assignments.json`**: running the app changes both (your test data). Don't `git add .` on autopilot and push your test data over the shared dummy data. Look at `git status` before adding; to discard changes to a data file:

```bash
git checkout -- src/data/assignments.json
```

- One feature per PR. A PR that "adds login + fixes sort + restructures folders" will get sent back to be split.

## Emergencies

**Accidentally coded on main (not committed yet):**

```bash
git checkout -b feature/task-name    # carries your changes to a new branch
```

Your changes move with you; main is clean again.

**Accidentally committed to main (not pushed yet):**

```bash
git checkout -b feature/task-name    # new branch now holds that commit
git checkout main
git reset --hard origin/main         # reset main to match GitHub
```

**Throw away uncommitted changes to one file:**

```bash
git checkout -- some_file.py
```

Careful: this really deletes them, no undo.

**Wrong commit message (not pushed yet):**

```bash
git commit --amend -m "Correct message"
```

**Lost? Check where you are:**

```bash
git branch             # which branch
git status             # what's uncommitted
git log --oneline -5   # last 5 commits
```

If things get truly tangled: don't panic-delete the project folder and re-clone — message the team first. Most situations are fixable in a minute.

## Quick reference

| Command | Job |
|---|---|
| `git status` | See changed files and current branch |
| `git checkout main` + `git pull origin main` | Switch to main, update it |
| `git checkout -b feature/x` | Create and switch to a new branch |
| `git add .` | Stage changes for commit |
| `git commit -m "..."` | Save a checkpoint with a message |
| `git push origin feature/x` | Push your branch to GitHub |
| `git branch` | List branches, mark the current one |
| `git log --oneline -5` | Recent history |