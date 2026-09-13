#!/bin/bash
# run_sql_from_docx.sh
# Small helper: extracts plain text from SQL.docx and writes extracted_sql.txt.
# It does NOT try to guess SQL blocks — open extracted_sql.txt and copy SQL into db_setup.sql.

set -e
if command -v docx2txt >/dev/null 2>&1; then
  echo "Using docx2txt to extract SQL.docx -> extracted_sql.txt"
  docx2txt SQL.docx extracted_sql.txt
  echo "extracted_sql.txt created. Inspect and copy SQL blocks to db_setup.sql"
elif command -v pandoc >/dev/null 2>&1; then
  echo "Using pandoc to extract SQL.docx -> extracted_sql.txt"
  pandoc -f docx -t plain SQL.docx -o extracted_sql.txt
  echo "extracted_sql.txt created. Inspect and copy SQL blocks to db_setup.sql"
else
  echo "Install docx2txt or pandoc to extract SQL.docx automatically."
  echo "Fallback: open SQL.docx in Word/LibreOffice and copy SQL statements to db_setup.sql"
  exit 1
fi
