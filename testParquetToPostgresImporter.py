import config
import unittest
from unittest.mock import patch, MagicMock
from ParquetToPostrgesImporter import ParquetToPostgresImporter

class TestParquetToPostgresImporter(unittest.TestCase):
    @patch('duckdb.connect')
    def test_read_parquet(self, mock_duckdb_connect):
        # Mock DuckDB connection and query
        mock_con = MagicMock()
        mock_df = MagicMock()
        mock_con.execute.return_value.fetchdf.return_value = mock_df
        mock_duckdb_connect.return_value = mock_con

        importer = ParquetToPostgresImporter('user', 'password')
        importer.read_parquet('dummy_path.parquet')

        mock_duckdb_connect.assert_called_once()
        mock_con.execute.assert_called_once_with("SELECT * FROM read_parquet('dummy_path.parquet')")
        self.assertEqual(importer.df, mock_df)
        mock_con.close.assert_called_once()

    @patch('ParquetToPostrgesImporter.create_engine')
    def test_write_to_postgres(self, mock_create_engine):
        importer = ParquetToPostgresImporter('user', 'password')
        importer.df = MagicMock()
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Test valid if_exists
        importer.write_to_postgres('test_table', 'replace')
        mock_create_engine.assert_called_once()
        importer.df.to_sql.assert_called_once_with('test_table', mock_engine, if_exists='replace', index=False)

        # Test invalid if_exists
        with self.assertRaises(ValueError):
            importer.write_to_postgres('test_table', 'invalid')
        # Test df is None
        importer2 = ParquetToPostgresImporter(config.user, config.password)
        with self.assertRaises(ValueError):
            importer2.write_to_postgres('test_table', 'replace')

if __name__ == '__main__':
    unittest.main()