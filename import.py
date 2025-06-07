import config
import duckdb
import pandas as pd
from sqlalchemy import create_engine

# === Налаштування ===

# Шлях до Parquet-файлу
parquet_file = 'your_data.parquet'

# Параметри підключення до PostgreSQL
pg_user = config.user
pg_password = config.password
pg_host = 'localhost'
pg_port = '5432'
pg_db = 'postgres'
pg_table = 'example_table'

# === Крок 1: Завантаження з Parquet через DuckDB ===

# Використовуємо DuckDB для читання parquet
con = duckdb.connect()
df = con.execute(f"SELECT * FROM read_parquet('{parquet_file}')").fetchdf()

# === Крок 2: Запис у PostgreSQL через SQLAlchemy ===

# Формуємо рядок підключення
engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

# Запис даних у таблицю (створить або допише)
df.to_sql(pg_table, engine, if_exists='replace', index=False)

print(f"Дані успішно імпортовані в таблицю `{pg_table}`")
