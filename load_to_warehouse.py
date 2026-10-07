import pandas as pd
from sqlalchemy import create_engine

# 1. Read the processed Parquet file created by Spark
print("Reading processed Parquet file...")
df = pd.read_parquet('processed_rides.parquet')

# 2. Connect to PostgreSQL Data Warehouse
print("Connecting to PostgreSQL...")
engine = create_engine('postgresql://admin:supersecretpassword@0.0.0.0:5432/data_warehouse')

# 3. Load data into Postgres table
print("Loading data into warehouse...")
df.to_sql('rides_data', engine, if_exists='replace', index=False)

print("Data successfully loaded to PostgreSQL as 'rides_data' table!")