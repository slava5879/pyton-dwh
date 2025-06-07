import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Sample data
data = {'Captain': ['James T. Kirk', 'Jean-Luc Picard'],
        'Actor': ['William Shatner', 'Patrick Stewart']}
df = pd.DataFrame(data)

# Convert Pandas DataFrame to Arrow Table
table = pa.Table.from_pandas(df)

# Write to Parquet file
pq.write_table(table, '.\\src\\org\\output\\example.parquet')