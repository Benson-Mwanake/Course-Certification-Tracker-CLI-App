# Certification Tracker CLI

A Python CLI application for managing **institutions, courses, and certifications**. This tool allows users to track, update, and manage their learning journey using a simple command-line interface.

---

## Features

* Add and manage institutions.
* Record courses under institutions.
* Save certifications linked to courses.
* View certifications by institution and course.
* Update and remove institutions, courses, and certifications.
* Check validity and expiry of certifications.
* Data stored in a local SQLite database.
* Built with **SQLAlchemy** for ORM and **Alembic** for migrations.

---

## Project Structure

```
.
├── lib
│   ├── cli.py
│   ├── db
│   │   ├── alembic.ini
│   │   ├── certification_tracker.db
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── __pycache__
│   │   │   │   └── env.cpython-312.pyc
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       └── 99480ccd3e4b_init_tables.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   └── seed.cpython-312.pyc
│   │   └── seed.py
│   ├── debug.py
│   ├── helpers.py
│   ├── __init__.py
│   └── __pycache__
│       ├── cli.cpython-312.pyc
│       ├── helpers.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── main.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Prerequisites

Before you begin, make sure you have installed:

* **Python 3.12.3 (or higher)**
* **Pipenv** (for dependency management)
* **SQLite 3** (database engine)

---

## Installation & Setup

1.  Clone the repository:

    ```bash
    git clone git@github.com:Benson-Mwanake/Course-Certification-Tracker-CLI-App.git
    cd Course-Certification-Tracker-CLI-App
    ```

2.  Install dependencies using **pipenv**:

    ```bash
    pipenv install
    ```

3.  Activate the virtual environment:

    ```bash
    pipenv shell
    ```

4.  **Create Database Tables with Migrations:** The `alembic upgrade head` command applies all new migrations to your database, creating the necessary tables.

    ```bash
    cd lib/db
    alembic upgrade head
    ```

5.  Seed the database with sample data:

    ```bash
    python -m lib.db.seed
    ```

---
## Running New Migrations (Future Changes)
   ```bash
   cd lib/db
   alembic revision --autogenerate -m "describe changes"
   alembic upgrade head
   ```

---

## Usage

Run the CLI with:

```bash
python main.py
```

You will see a main menu like this:

```
===========================================
  Course & Certification Tracker
===========================================
1. Manage Institutions
2. Manage Courses
3. Manage Certifications
4. View Reports
5. Exit
-------------------------------------------
```

### 1. Manage Institutions

* **Add Institution** → Create a new institution with name, location, year, and type (e.g., University, Bootcamp).
* **List Institutions** → Displays all saved institutions with details.
* **Update Institution** → Edit institution details (name, location, year, type).
* **Delete Institution** → Remove an institution and cascade delete its courses & certifications.

### 2. Manage Courses

* **Add Course** → Assign a new course to an institution.
* **List Courses** → View all courses grouped under their institutions.
* **Update Course** → Edit course details like name, description, or duration.
* **Delete Course** → Remove a course and cascade delete its certifications.

### 3. Manage Certifications

* **Add Certification** → Add a certification under a course, with title, level, issue date, and optional expiry date.
* **List Certifications** → Show all certifications, grouped by course and institution.
* **Update Certification** → Edit details of an existing certification.
* **Delete Certification** → Remove a certification permanently.

### 4. View Reports

* **View All Certifications by Institution** → Displays certifications grouped under their institutions and courses.
* **View Expiring (≤30 days) / Expired** → Displays certifications that are about to expire or have already expired.

### Example Workflow

1. Add an institution → *"Moringa School"*.
2. Add a course under it → *"Software Engineering"*.
3. Add a certification → *"Web APIs Professional"* with issue/expiry dates.
4. List certifications to confirm everything is saved.
5. Use reports to view certifications grouped by institution.

---

## Debugging

For quick inspection of the database contents, run:

```bash
python -m lib.debug
```

This will print out all institutions, courses, and certifications with their statuses.

---

## Tech Stack

* **Python 3.12.3**
* **SQLAlchemy** (ORM)
* **Alembic** (migrations)
* **SQLite** (local database)

---

## Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit changes with clear messages
4. Push to your fork and open a Pull Request

---

## License

**MIT License**

Copyright © 2025 **Benson Mwanake**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Author

Developed by **Benson Mwanake** as part of the **Moringa School Phase 3 Final Project**.
