import pandas as pd
import psycopg

# 1. Read the processed Parquet file
print("Reading processed Parquet file...")
df = pd.read_parquet('processed_rides.parquet')

# 2. Connect to PostgreSQL directly
print("Connecting to PostgreSQL...")
conn = psycopg.connect("host=0.0.0.0 port=5432 dbname=data_warehouse user=admin password=supersecretpassword")
cursor = conn.cursor()

# 3. Drop and recreate the table
print("Loading data into warehouse...")
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

# 4. Insert data using executemany (simpler for small datasets)
insert_query = "INSERT INTO rides_data (ride_id, pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, passenger_count, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
records = df.values.tolist()
cursor.executemany(insert_query, records)
conn.commit()

cursor.close()
conn.close()
print("Data successfully loaded to PostgreSQL as 'rides_data' table!")