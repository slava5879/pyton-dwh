import config
import duckdb
import pandas as pd
from sqlalchemy import create_engine

# === Settings ===

# path to your Parquet file
parquet_file = '.\\src\\org\\output\\example.parquet'

# PostgreSQL settings
pg_user = config.user
pg_password = config.password
pg_host = 'localhost'
pg_port = '5432'
pg_db = 'postgres'
pg_table = 'example_table'

# === Step 1: Downloading *.parquet file via DuckDB ===

# use DuckDB to read parquet
con = duckdb.connect()
df = con.execute(f"SELECT * FROM read_parquet('{parquet_file}')").fetchdf()

# === Step 2: Write in PostgreSQL via SQLAlchemy ===

# Create SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

# insert data into PostgreSQL table
# if the table does not exist, it will be created
df.to_sql(pg_table, engine, if_exists='replace', index=False)

print(f"Data successfully inserted into '{pg_table}' table in PostgreSQL database '{pg_db}'.")
