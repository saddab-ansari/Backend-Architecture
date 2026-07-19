# 05 — Todo API with JWT Authentication

**Concepts covered:** JWT token generation and validation (`jose`), password hashing (`bcrypt` via `passlib`), OAuth2 password flow (`OAuth2PasswordBearer`, `OAuth2PasswordRequestForm`), role-based access control, user-scoped data ownership (`ForeignKey`, `owner_id`), dependency injection chains (`Depends` stacking across files), multi-router architecture (`auth`, `todos`, `admin`, `users`).

**Project:** A fully authenticated Todo API — users register, log in, and receive a JWT access token. Every todo is tied to its owner via a foreign key, so users can only see and modify their own data. A separate admin router allows privileged users (role-checked via the token payload) to view and delete any todo. Includes a user-facing endpoint to view profile info and securely change passwords.

<img width="1882" height="1027" alt="TodoAPP Swagger" src="https://github.com/user-attachments/assets/ce33c7e4-b299-46fc-8cd5-5cf2520561b0" />
<img width="1887" height="1047" alt="TodoAPP auth box" src="https://github.com/user-attachments/assets/d5a9bc5d-e368-488d-82a3-6f13654e416f" />
<img width="877" height="852" alt="TodoAPP List" src="https://github.com/user-attachments/assets/18171bee-09af-420e-98cc-0da8b6e5d0bb" />

**Status:** Complete
