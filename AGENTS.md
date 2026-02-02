# Agent Guide for xerox-python

This document contains critical knowledge for AI agents working on the xerox-python repository. Read this ENTIRELY before making any changes.

## Repository Structure Overview

This is a [Copier](https://copier.readthedocs.io/) template repository with a **special branch structure**:

```
main ─┬─ fastapi (single commit with FastAPI specializations)
      └─ flask   (single commit with Flask specializations)
```

**CRITICAL RULES:**

1. **NEVER merge `fastapi` or `flask` into `main`**
2. **ALWAYS rebase** these branches when updating them
3. Each framework branch must be **EXACTLY ONE COMMIT** on top of `main`
4. Framework branches contain framework-specific specializations only

## Branch Strategy Explained

### Main Branch
- Contains the base template shared by all frameworks
- Gets updates to dependencies, tooling, common patterns
- Examples: Python version support, type checker updates, Makefile conventions

### FastAPI Branch
- Single commit on top of `main`
- Contains ONLY FastAPI-specific code:
  - `uvicorn` app server
  - FastAPI routers (not Flask blueprints)
  - ASGI middleware
  - FastAPI-specific dependencies

### Flask Branch  
- Single commit on top of `main`
- Contains ONLY Flask-specific code:
  - `flask` app server
  - Flask blueprints (not FastAPI routers)
  - WSGI middleware
  - Flask-specific dependencies

## Making Changes

### Updating Main Branch

When making changes to `main`:

1. Make your changes on `main`
2. Commit and push to `origin/main`
3. **DO NOT** merge into framework branches
4. See "Rebasing Framework Branches" below

### Rebasing Framework Branches

After updating `main`, you **MUST** rebase both framework branches:

```bash
# 1. Checkout the framework branch
git checkout fastapi

# 2. Rebase onto main (will have conflicts)
git rebase main

# 3. Resolve conflicts by copying from the previous good version
# Use git reflog to find the previous good commit
git reflog
# Example: ac3789a was the last good fastapi commit
git show ac3789a:path/to/conflicted/file > path/to/conflicted/file

# 4. Continue the rebase
git add -A
git rebase --continue

# 5. Apply any additional fixes needed for main changes
# (e.g., API updates, new type ignore comments)

# 6. Squash everything into ONE commit
git reset --soft main
git commit -m "feat: Added a branch for FastAPI"

# 7. Verify single commit
git log --oneline main..fastapi
# Should show EXACTLY one commit

# 8. Repeat for flask branch
git checkout flask
# ... same process
```

### Testing Your Changes

**ALWAYS** test both framework branches before pushing:

```bash
# Test FastAPI
cd /path/to/test/location
rm -rf test-fastapi-final
cd xerox-python
uv run copier copy --trust --defaults --vcs-ref fastapi \
  --data project_name=test-fastapi-final \
  --data run_qa_checks=false --data initialize_git=false \
  --data push_to_github=false --skip-tasks . ../test-fastapi-final

cd ../test-fastapi-final/test-fastapi-final
echo "3.13" > .python-version
sed -i.bak 's/requires-python = ">=3.9, ~=3.14"/requires-python = ">=3.9, ~=3.13"/' pyproject.toml
UV_PYTHON=3.13 uv sync --quiet
make qa/full
# MUST show: "All quality checks pass!" with 0 diagnostics

# Test Flask (same process with flask branch)
```

### Common Pitfalls

#### ❌ WRONG: Merging
```bash
git checkout fastapi
git merge main  # NEVER DO THIS!
```

#### ✅ RIGHT: Rebasing
```bash
git checkout fastapi
git rebase main
# resolve conflicts
git reset --soft main
git commit -m "feat: Added a branch for FastAPI"
```

#### ❌ WRONG: Multiple commits on framework branch
```bash
git log --oneline main..fastapi
abc123 fix: update imports
def456 fix: resolve conflicts  
789ghi feat: Added a branch for FastAPI
# THREE commits - WRONG!
```

#### ✅ RIGHT: Single commit on framework branch
```bash
git log --oneline main..fastapi
abc123 feat: Added a branch for FastAPI
# ONE commit - CORRECT!
```

## Key Differences Between Frameworks

### FastAPI-Specific Files

- **main.py**: Uses `FastAPI()` app, async/await, lifespan context manager
- **Routers**: `from fastapi import APIRouter`, async route handlers
- **Middleware**: 
  - `CORSMiddleware` needs `# ty: ignore[invalid-argument-type]`
  - `TrackRequestsMiddleware` needs `# ty: ignore[invalid-argument-type]`
- **Dependencies**: `fastapi`, `uvicorn`, `httpx`, `logot`
- **Makefile**: `app/serve` uses `uvicorn`

### Flask-Specific Files

- **main.py**: Uses `create_app()` factory pattern, WSGI
- **Routes**: `from flask import Blueprint`, sync route handlers
- **Middleware**:
  - `MiddlewareManager(app)` needs `# ty: ignore[invalid-assignment]`
  - `app.wsgi_app.add_middleware()` needs `# ty: ignore[unresolved-attribute]`
- **Dependencies**: `flask`, `flask-buzz`, `flask-http-middleware`, `httpx`
- **Makefile**: `app/serve` uses `flask run`

### Shared Files (in main)

- **version.py**: Version detection logic
- **constants.py**: Enums like `DeployEnv`
- **pydantix.py**: Pydantic custom types (TimeDelta)
- **Base Makefile/pyproject.toml**: Common build/test/QA setup

## Recent Migration: mypy/basedpyright → ty

The repository recently migrated from `mypy` and `basedpyright` to `ty` as the type checker.

### Updated Comment Syntax

```python
# OLD (don't use):
# pyright: ignore[reportArgumentType]
# type: ignore[arg-type]

# NEW (use this):
# ty: ignore[invalid-argument-type]
# ty: ignore[unresolved-attribute]
```

### Updated Makefile Targets

```makefile
# OLD:
qa/types: qa/types-basedpyright qa/types-mypy

# NEW:
qa/types: qa/types-ty
```

## whenever Library API Update

The `whenever` library deprecated `parse_common_iso()` and `format_common_iso()`:

```python
# OLD (don't use):
TimeDelta.parse_common_iso("PT1S")
instance.format_common_iso()

# NEW (use this):
TimeDelta.parse_iso("PT1S")
instance.format_iso()
```

This affects:
- `pydantix.py` serialization
- Test files using `TimeDelta` or `Instant`

## Debugging Tips

### Finding Previous Good Commits

If you need to reference the last working version:

```bash
# View reflog to find previous commits
git reflog

# Show a file from a specific commit
git show <commit-hash>:path/to/file

# Copy a file from a previous commit
git show <commit-hash>:path/to/file > path/to/file
```

### Checking Branch Structure

```bash
# Visualize branch structure
git log --oneline --graph --all -10

# Should look like:
# * 0b201fd feat: Added a branch for Flask
# | * 07b1b86 feat: Added a branch for FastAPI
# |/  
# * ff437f6 (main) Latest main commit
# * e42f565 Previous main commit

# Count commits on a branch
git log --oneline main..fastapi | wc -l
# Should output: 1
```

### Verifying Test Success

After generating a test project, look for:

```
All checks passed!
All checks passed!
All quality checks pass!
```

And specifically check for **0 diagnostics** from the type checker.

## Emergency Recovery

If you accidentally merge instead of rebase:

```bash
# 1. Find the last good commit in reflog
git reflog | grep fastapi

# 2. Hard reset to that commit
git reset --hard <good-commit-hash>

# 3. Force push (use --force-with-lease for safety)
git push origin fastapi --force-with-lease
```

## Pushing Changes

When pushing all branches after updates:

```bash
# Push all three branches together
git push origin main fastapi flask --force-with-lease

# The --force-with-lease is necessary because:
# - Framework branches are rebased (history rewritten)
# - But it's safer than --force (won't overwrite others' work)
```

## Questions to Ask Yourself

Before pushing changes, verify:

- [ ] Did I rebase instead of merge?
- [ ] Does each framework branch have EXACTLY one commit?
- [ ] Did I test BOTH fastapi and flask branches?
- [ ] Did both QA runs show 0 diagnostics?
- [ ] Did all tests pass (17 tests each)?
- [ ] Are coverage requirements met (>85%)?
- [ ] Did I use `--force-with-lease` when pushing rebased branches?

## Common Tasks Reference

### Add a new dependency to both frameworks

```bash
# 1. Update main branch if it's a shared dependency
# 2. Update fastapi branch pyproject.toml.jinja with FastAPI-specific version
# 3. Update flask branch pyproject.toml.jinja with Flask-specific version
# 4. Test both branches
# 5. Push all three branches
```

### Update Python version support

```bash
# 1. Update main branch .python-version and pyproject.toml
# 2. Rebase both framework branches
# 3. Test with new Python version
# 4. Push all branches
```

### Fix a type checking error

```bash
# 1. Determine if it's in shared code (main) or framework-specific
# 2. Add appropriate # ty: ignore[...] comment
# 3. If in main: rebase both framework branches after
# 4. If in framework branch: fix that branch only
# 5. Test thoroughly
```

## Final Wisdom

> "The framework branches must NEVER be merged to main. They should remain as SINGLE COMMITS branching off from main, containing all framework-specific specializations."

When in doubt:
1. **Rebase**, don't merge
2. **Test** both branches before pushing
3. **Verify** single commit structure
4. **Ask** the human if you're unsure

This repository has a unique structure for a good reason - it allows maintaining multiple framework specializations while sharing common code. Respect the structure, and it will work beautifully.
