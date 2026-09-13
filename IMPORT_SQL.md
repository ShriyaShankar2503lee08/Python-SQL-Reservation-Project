# How to import SQL from SQL.docx and create the MySQL backend

This repository already contains your SQL.docx file (the original SQL commands you uploaded). Follow these steps to extract and run the SQL so the Python front-end (PROJECT.py) can connect to the MySQL backend.

Option A — manual (recommended)
1. Open SQL.docx in Microsoft Word (or LibreOffice Writer).
2. Find the SQL commands in the document (CREATE DATABASE, CREATE TABLE, INSERT, etc.).
3. Copy the SQL statements into a file named `db_setup.sql` (plain text) in the repository root.
4. From a terminal run:

   mysql -u root -p < db_setup.sql

   Provide your MySQL root password when prompted. This will create the `hotel` database, tables, and sample data the program expects.

Option B — automatic extraction (Linux / macOS with docx2txt or pandoc)
If you don't want to copy/paste manually, you can try extracting plain text from the DOCX and then saving the SQL sections to db_setup.sql.

1. Install docx2txt (or pandoc):

   # Debian/Ubuntu
   sudo apt-get install docx2txt

   # or with pandoc
   sudo apt-get install pandoc

2. Extract plain text:

   docx2txt SQL.docx extracted_sql.txt

   # or with pandoc
   pandoc -f docx -t plain SQL.docx -o extracted_sql.txt

3. Open extracted_sql.txt, locate the SQL statements, copy them into db_setup.sql, and run:

   mysql -u root -p < db_setup.sql

Notes and troubleshooting
- If SQL.docx contains multiple code blocks or explanatory text, ensure you copy only valid SQL statements into db_setup.sql.
- If your MySQL user is not root, replace -u root -p with your admin credentials (or run commands in your MySQL client).
- The Python program PROJECT.py uses the database name `hotel` and tables named `pdata`, `food`, and `luggage`. Make sure these exist after you run the SQL.

If you want, I can:
- Convert SQL.docx to db_setup.sql for you and commit db_setup.sql into the repo (I will only do this with your explicit confirmation). 
- Add a sample db_setup.sql generated from the docx. If you want me to extract and commit it, reply "Yes extract and commit db_setup.sql".
