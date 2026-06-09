# ETL Pipeline - Python

A production-style ETL pipeline that fetches data from a public API, transforms it, and loads it into a SQLite database.

## Technologies
- Python 3.8
- Pandas
- SQLAlchemy
- SQLite

## How to run
```bash
python3 pipeline.py
```

## What it does
- Extract: Fetches user data from JSONPlaceholder API
- Transform: Cleans and normalizes the data
- Load: Stores into SQLite database