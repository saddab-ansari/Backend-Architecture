# 05 — Todo API with JWT Authentication

**Concepts covered:** JWT token generation and validation (`jose`), password hashing (`bcrypt` via `passlib`), OAuth2 password flow (`OAuth2PasswordBearer`, `OAuth2PasswordRequestForm`), role-based access control, user-scoped data ownership (`ForeignKey`, `owner_id`), dependency injection chains (`Depends` stacking across files), multi-router architecture (`auth`, `todos`, `admin`, `users`).

**Project:** A fully authenticated Todo API — users register, log in, and receive a JWT access token. Every todo is tied to its owner via a foreign key, so users can only see and modify their own data. A separate admin router allows privileged users (role-checked via the token payload) to view and delete any todo. Includes a user-facing endpoint to view profile info and securely change passwords.

<img width="1882" height="1027" alt="TodoAPP Swagger" src="https://github.com/user-attachments/assets/ce33c7e4-b299-46fc-8cd5-5cf2520561b0" />
<img width="1895" height="1042" alt="image" src="https://github.com/user-attachments/assets/44e2b87f-c626-454c-a6c7-99a154afc115" />

**Status:** Complete
