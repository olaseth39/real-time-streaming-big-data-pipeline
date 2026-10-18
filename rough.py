import pandas as pd
import psycopg
from io import StringIO

# 1. Read the processed Parquet file
print("Reading processed Parquet file...")
df = pd.read_parquet('processed_rides.parquet')

# 2. Connect to PostgreSQL directly
print("Connecting to PostgreSQL...")
conn = psycopg.connect("host=0.0.0.0 port=5432 dbname=data_warehouse user=admin password=supersecretpassword")
cursor = conn.cursor()

# 3. Drop and recreate the table to avoid conflicts
print("Loading data into warehouse...")
#cursor.execute("DROP TABLE IF EXISTS rides_data")
cursor.execute("DROP TABLE IF EXISTS rides_data CASCADE")
cursor.execute("""
    CREATE TABLE rides_data (
        ride_id INTEGER,
        pickup_lat FLOAT,
        pickup_lon FLOAT,
        dropoff_lat FLOAT,
        dropoff_lon FLOAT,
        passenger_count INTEGER,
        price FLOAT
    )
""")
conn.commit()

# 4. Use COPY for fast bulk insert
output = StringIO()
df.to_csv(output, sep='\t', index=False, header=False)
output.seek(0)
cursor.copy_from(output, 'rides_data', null="", columns=df.columns.tolist())
conn.commit()

cursor.close()
conn.close()
print("Data successfully loaded to PostgreSQL as 'rides_data' table!")