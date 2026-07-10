# 04 — Todo API (SQLAlchemy)

**Concepts covered:** SQLAlchemy ORM integration, SQLite persistent storage, Dependency Injection (`Depends`, `get_db`), database models vs. Pydantic schemas (`**todo_request.model_dump()`), CRUD operations via ORM (`query`, `filter`, `add`, `commit`, `delete`), `Path` validation, and HTTP error handling (`HTTPException`).

<p align="center">
  <img width="1097" height="477" alt="image" src="https://github.com/user-attachments/assets/21df3d23-0187-4d8d-a8b1-83676ef600ff" />
</p>

**Project:** A foundational CRUD API built with FastAPI — transitioning from in-memory Python lists to a persistent SQLite database using SQLAlchemy. Built as a learning follow-along to understand database sessions, ORM mapping, and backend data routing. 

**Status:** Base CRUD Complete (Upgraded version in process).
