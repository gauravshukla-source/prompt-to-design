# Hotfix: Prompt Coverage Must Not Block Generation

## Why the previous package could still fail
The traceback showed an older `app/agents/orchestrator.py`:

```python
if not validation.valid:
    errors = [i for i in validation.issues if i.severity == 'error']
    if errors:
        raise ValueError(...)
```

That is not the corrected orchestrator in the tested package. This hotfix adds a defensive policy: prompt coverage issue codes are advisory even if an older validator incorrectly labels them as `error`.

## Install
Replace the entire project with this ZIP, preserving your `.env` only if you have local secrets that are not stored in the project.

Then verify:

```bash
python -m pytest -q
```

Expected: `23 passed`.

## Important
If your local traceback still shows the old `if not validation.valid:` code after replacing the project, you are running a different working directory or an old Cloud Run image.
