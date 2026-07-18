# 03 — Modularization Phase

**Concepts covered:** Multi-file backend architecture, separation of concerns, `APIRouter` vs `FastAPI` app instance, module-to-module data flow, why monolithic files stop scaling.

## Why this folder exists

Up to Todo API v1, the entire application lived inside a single `main.py`. That works fine for a small project — but it doesn't scale. As features grow, one file holding models, database logic, and routes all at once becomes hard to navigate and harder to maintain.

This phase documents the shift from **one file doing everything** to **multiple files, each with one responsibility** — the architecture that every real backend project after this point is built on.

## The breakdown

Building a Todo app requires four distinct concerns:

- **`models.py`** — defines the shape of the data. What characteristics does a Todo have? Title, description, priority, completion status.
- **`database.py`** — handles where the data actually lives. The connection to the database itself.
- **`todos.py`** — contains the actual route logic for todos: creating, reading, updating, deleting. This file pulls structure from `models.py` and connection from `database.py`.
- **`main.py`** — the entry point that ties everything together. It doesn't contain the logic itself — it *compiles* the other files into one running application.

## How they connect

`todos.py` doesn't use `@app.get(...)` like a single-file project would. Instead, it uses `@router.get(...)` — because `todos.py` isn't the main application, it's a **router**: a self-contained set of routes waiting to be plugged in.

`main.py` then imports that router and connects it:

```python
app.include_router(todos.router)
```

This is what allows multiple files — each handling one job — to function together as a single running API, instead of one file trying to do everything at once.

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/05e44b60-6de3-488c-9021-65ce08a32d70" />

<div align="center">
  *AI-Generated image, for illustration purpose*
</div>
## Status: Complete
