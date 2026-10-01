from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("RideProcessing") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Read the raw JSON files from local disk
print("Reading raw ride data from local disk...")
df = spark.read.json("raw_data/*.json")

# 3. Clean and transform the data (e.g., filter out expensive rides)
print("Filtering expensive rides...")
cheap_rides = df.filter(col("price") < 50.0)

# 4. Show the processed data
cheap_rides.show()

# 5. Write to Parquet (Big Data format)
cheap_rides.write.mode("overwrite").parquet("processed_rides.parquet")
print("Data successfully processed and saved to Parquet!")