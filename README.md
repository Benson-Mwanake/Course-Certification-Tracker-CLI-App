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
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       └── 14cd0018c693_init.py
│   │   ├── models.py
│   │   └── seed.py
│   ├── debug.py
│   ├── helpers.py
│   ├── __init__.py
│   └── __pycache__
├── main.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone git@github.com:Benson-Mwanake/Course-Certification-Tracker-CLI-App.git
   cd Course-Certification-Tracker-CLI-App
   ```

2. Install dependencies using **pipenv**:

   ```bash
   pipenv install
   ```

3. Activate virtual environment:

   ```bash
   pipenv shell
   ```

4. Initialize and seed the database:

   ```bash
   python -m lib.db.seed
   ```

---

## Usage

Run the CLI with:

```bash
python main.py
```

---

## Tech Stack

* **Python 3.11+**
* **SQLAlchemy** (ORM)
* **Alembic** (database migrations)
* **SQLite** (local database)

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
