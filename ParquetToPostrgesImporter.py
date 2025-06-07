import config
import duckdb
import pandas as pd
from sqlalchemy import create_engine

class ParquetToPostgresImporter:
    def __init__(self, pg_user, pg_password, pg_host='localhost', pg_port='5432', pg_db='postgres'):
        #self.parquet_file = parquet_file
        #self.pg_table = pg_table
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.pg_host = pg_host
        self.pg_port = pg_port
        self.pg_db = pg_db
        self.engine = None
        self.df = None

    def read_parquet(self, parquet_file_path):
        con = duckdb.connect()
        self.df = con.execute(f"SELECT * FROM read_parquet('{parquet_file_path}')").fetchdf()
        con.close()

    def write_to_postgres(self, pg_table, if_exists):
        if if_exists not in ['fail', 'replace', 'append']:
            raise ValueError("if_exists must be one of 'fail', 'replace', or 'append'.")
        if self.df is None:
            raise ValueError("DataFrame is empty. Run read_parquet() first.")
        self.engine = create_engine(
            f'postgresql+psycopg2://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_db}'
        )
        self.df.to_sql(pg_table, self.engine, if_exists=if_exists, index=False)
        print(f"Data successfully inserted into '{pg_table}' table in PostgreSQL database '{self.pg_db}'.")

if __name__ == "__main__":
    importer = ParquetToPostgresImporter(
        pg_user=config.user,
        pg_password=config.password,
        #pg_host='localhost',
        #pg_port='5432',
        #pg_db='postgres'
    )
    importer.read_parquet('.\\src\\org\\output\\example.parquet')
    importer.write_to_postgres(pg_table='example_table', if_exists='append')  # Change if_exists to append/replace/fail as needed