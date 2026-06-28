# Problem Statement: CLI Research Log Manager

## Objective

Develop a single Python script (`paper_tracker.py`) to manage a command-line interface (CLI) research reading log. This project serves as a foundational exercise to implement and validate core object-oriented programming (OOP) principles, state management, and strict type hinting before transitioning to complex API frameworks.

## Core Constraints & Requirements

- **Constants & Basic Types:** Define a global constant for a reading target (e.g., `TARGET_PAPERS_PER_MONTH = 4`). Standard variables must be utilized to track ongoing progress.

- **The Class & Initializer:** Design a `ResearchPaper` class. The `__init__` method must accept arguments for the paper's title, authors, publication year, and a boolean state indicating whether the paper has been read.

- **Type Annotations:** Every variable, function argument, and method return type must be strictly annotated (e.g., `title: str`, `year: int`). This enforces the strict typing standards required for modern backend frameworks.

- **Standard Methods:**
  - Implement an `add_summary()` method to append text notes to a specific paper's record.
  - Implement a `mark_as_read()` method to mutate the boolean state of the paper.

- **Dunder Methods (Magic Methods):**
  - Implement `__str__` to ensure that printing the object outputs a clean, formatted string containing the title, author, and read status, rather than a default memory address.
  - Implement `__eq__` to enable the direct comparison of two paper objects by their title, facilitating duplicate entry prevention.

## Execution Scope

Persistent data storage (e.g., PostgreSQL, SQLite, or file I/O) is out of scope for this build. The script should validate its own logic by instantiating several sample paper objects at the bottom of the file and printing the expected outputs and state changes directly to the terminal.
