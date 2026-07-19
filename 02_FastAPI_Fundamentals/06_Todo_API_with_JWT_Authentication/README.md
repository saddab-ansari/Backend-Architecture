# 05 — Todo API with JWT Authentication

**Concepts covered:** JWT token generation and validation (`jose`), password hashing (`bcrypt` via `passlib`), OAuth2 password flow (`OAuth2PasswordBearer`, `OAuth2PasswordRequestForm`), role-based access control, user-scoped data ownership (`ForeignKey`, `owner_id`), dependency injection chains (`Depends` stacking across files), multi-router architecture (`auth`, `todos`, `admin`, `users`).

**Project:** A fully authenticated Todo API — users register, log in, and receive a JWT access token. Every todo is tied to its owner via a foreign key, so users can only see and modify their own data. A separate admin router allows privileged users (role-checked via the token payload) to view and delete any todo. Includes a user-facing endpoint to view profile info and securely change passwords.

**Status:** Complete
