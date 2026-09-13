# Python-SQL Reservation Project

Python + MySQL interactive Reservation System (basic education project).

This repository contains a simple Python front-end (PROJECT.py) that talks to a MySQL back-end. The included SQL script (db_setup.sql) creates the database, tables and sample data the Python code expects.

Files you care about
- PROJECT.py — the Python front-end program (interactive CLI).
- db_setup.sql — SQL script to create the `hotel` database, tables (pdata, food, luggage) and sample rows.
- requirements.txt — Python dependency list.
- SQL.docx — original SQL docx (binary); use db_setup.sql instead for setup.
- 12th COMPUTER_SCIENCE IP (1).pdf — project document.

Quick setup (tested on Linux / macOS / Windows with WSL)

1) Install Python 3.8+ and pip

2) Install Python dependency

```bash
python -m pip install -r requirements.txt
```

3) Create the MySQL database and tables

- If you have a MySQL root/admin account, run:

```bash
mysql -u root -p < db_setup.sql
```

This creates a database named `hotel`, tables `pdata`, `food`, `luggage`, inserts a few sample food & luggage rows, and (optionally) creates a local user `Shriya` with password `lino`. If you prefer not to create the user, edit db_setup.sql and remove the CREATE USER / GRANT lines and instead use your existing credentials.

4) Configure database credentials

Option A — create a JSON file (recommended): create a file named `db_config.json` beside PROJECT.py with:

```json
{
  "host": "localhost",
  "database": "hotel",
  "user": "Shriya",
  "password": "lino"
}
```

Option B — export environment variables instead (Linux/macOS):

```bash
export DB_HOST=localhost
export DB_NAME=hotel
export DB_USER=Shriya
export DB_PASS=lino
```

The program will try db_config.json first, then environment variables, then fall back to sensible defaults.

5) Run the program

```bash
python PROJECT.py
```

Notes & behaviour
- The program appends a human-readable receipt to Bill.txt in the repository directory.
- If you get a connection error, double-check MySQL is running and that the database and tables exist (see db_setup.sql). Use the mysql client to inspect the tables:

```sql
USE hotel;
SHOW TABLES;
SELECT * FROM food;
SELECT * FROM luggage;
```

If you want me to automatically apply these changes to PROJECT.py (make the program more robust or remove hard-coded defaults), tell me and I will update the code in this repo.
