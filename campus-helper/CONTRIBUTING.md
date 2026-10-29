# Contributing to campus-helper

Welcome! This guide takes you from zero to your first Pull Request (PR).

## Step-by-step

1. **Find an issue.** Open the **Issues** tab and pick one that is not assigned.
   Comment "I'd like to work on this" and wait to be assigned.
2. **Fork the repo.** Click **Fork** (top right). This makes your own copy.
3. **Clone your fork.**
   ```bash
   git clone https://github.com/<your-username>/campus-helper.git
   cd campus-helper
   ```
4. **Create a branch.** Never work on `main`.
   ```bash
   git checkout -b fix-issue-3-attendance
   ```
5. **Make your changes.** Edit the files, then run the tests:
   ```bash
   python -m pytest
   ```
6. **Commit.**
   ```bash
   git add .
   git commit -m "Fix attendance percentage formula"
   ```
7. **Push to your fork.**
   ```bash
   git push origin fix-issue-3-attendance
   ```
8. **Open a Pull Request.** On your fork's GitHub page, click **Compare & pull request**.
   Fill in the template and write `Closes #3` (use your issue number).
9. **Respond to review.** The maintainer may ask for changes. Push more commits to the
   same branch and the PR updates automatically.

## How points work

Points are awarded **when your PR is merged**, based on the issue's label:

| Label | Points |
|-------|--------|
| `good first issue` (docs, typos, CONTRIBUTORS.md) | 5 |
| `html/css` | 10 |
| `bug` | 15 |
| `enhancement` | 20 |

Rules:
- One issue per PR, and one PR per issue.
- Your PR must reference the issue (`Closes #N`).
- Tests that passed before must still pass.
- Be kind. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Stuck?

Ask in the issue comments. Nobody minds beginner questions.
