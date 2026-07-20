## Backend Systems & Engineering Log
A continuous tracking repository documenting my progression through backend architecture and AI systems engineering. Rather than showcasing massive, AI-generated codebases, this repository serves as a transparent log of foundational builds, object-oriented principles, and system design recaps built entirely from the ground up.

### Current Highlight: Todo API with JWT Authentication
Located in `02_FastAPI_Fundamentals/06_Todo_API_with_JWT_Authentication`

Project: A fully authenticated Todo API — users register, log in, and receive a JWT access token. Every todo is tied to its owner via a foreign key, so users can only see and modify their own data. A separate admin router allows privileged users (role-checked via the token payload) to view and delete any todo. Includes a user-facing endpoint to view profile info and securely change passwords.

**Concepts covered:** JWT token generation and validation (`jose`), password hashing (`bcrypt` via `passlib`), OAuth2 password flow (`OAuth2PasswordBearer`, `OAuth2PasswordRequestForm`), role-based access control, user-scoped data ownership (`ForeignKey`, `owner_id`), dependency injection chains (`Depends` stacking across files), multi-router architecture (`auth`, `todos`, `admin`, `users`).

<img width="1882" height="1027" alt="TodoAPP Swagger" src="https://github.com/user-attachments/assets/ce33c7e4-b299-46fc-8cd5-5cf2520561b0" />
<img width="1895" height="1042" alt="image" src="https://github.com/user-attachments/assets/44e2b87f-c626-454c-a6c7-99a154afc115" />

**Status:** Complete

### Up Next: ApplyTrack
A from-scratch build — no course, no follow-along — designed to test how much of the Todo API actually stuck. Same core stack (FastAPI, SQLAlchemy, JWT auth), extended with a real three-table relational chain (Company → Application → InterviewRound), status enums, query-param filtering/pagination/sorting, and `.env`-based config instead of a hardcoded secret key.

**Status:** Planning — build starts this week

### Ongoing Course
**FastAPI - The Complete Course 2026** by Eric Roby — working through backend 
fundamentals, REST APIs, authentication, and database integration as the 
foundation for building production AI systems.

*JWT-authenticated Todo API complete. Moving on to ApplyTrack — a self-designed project to consolidate everything from the course before going further.*
