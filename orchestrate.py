import subprocess
import sys
import os

BASE_DIR = "/home/seth/streaming-data-pipeline"
DBT_DIR = BASE_DIR + "/ride_dbt"
PYTHON = BASE_DIR + "/venv/bin/python"

def run_task(name, command, cwd=BASE_DIR):
    print(f"Running {name}...")
    subprocess.run(command, check=True, cwd=cwd)

def main():
    try:
        # 1. Run Producer
        run_task("Producer", [PYTHON, "producer.py"])
        
        # 2. Run Consumer
        run_task("Consumer", [PYTHON, "consumer.py"])
        
        # 3. Sync S3 to Local
        run_task("Sync S3", ["aws", "--endpoint-url=http://localhost:4566", "s3", "sync", "s3://raw-ride-data", BASE_DIR + "/raw_data"])
        
        # 4. Run Spark
        run_task("Spark", [PYTHON, "spark_consumer.py"])
        
        # 5. Load to Warehouse
        run_task("Load to Postgres", [PYTHON, "load_to_warehouse.py"])
        
        # 6. Run dbt
        run_task("dbt Run", [PYTHON, "-m", "dbt.cli.main", "run"], cwd=DBT_DIR)
        
        print("Pipeline completed successfully!")
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()