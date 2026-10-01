Real-Time Streaming & Big Data Pipeline

A senior-level data engineering project processing millions of NYC Taxi ride events in real-time using Apache Kafka, Spark, dbt, and Terraform.
Day 1: Architecture & Infrastructure (Terraform & LocalStack)

Objective: Establish the foundational cloud infrastructure using Infrastructure as Code (IaC) principles, provisioning a local Data Lake without incurring cloud costs.

Tech Stack: Docker, LocalStack (AWS S3 Emulator), Terraform, AWS CLI.
Implementation Steps

    Local Cloud Emulation: Deployed LocalStack via Docker to emulate AWS S3 locally, providing a zero-cost, zero-suspension-risk environment for development.
    Infrastructure as Code (Terraform): Wrote main.tf to programmatically provision an S3 bucket (raw-ride-data) for the Data Lake. Configured the AWS provider to bypass STS validation and point to the LocalStack endpoint.
    Execution: Successfully ran terraform init, terraform plan, and terraform apply to build the infrastructure without manual console intervention.


Day 2-4: Docker, Streaming, and Big Data Processing

Objective: Containerize the environment, stream real-time data using Kafka, and process it using Apache Spark.

Tech Stack: Docker, Apache Kafka, Apache Spark, Python, Boto3, LocalStack.
Implementation Steps

    Dockerized Environment: Created a docker-compose.yml file to spin up LocalStack (S3), Apache Kafka, and Zookeeper simultaneously.
    Streaming Ingestion (Kafka): Wrote a Python Producer (producer.py) to simulate real-time ride events and push them to a Kafka topic. Created the ride_events topic via the Kafka CLI.
    Data Lake Landing: Wrote a Python Consumer (consumer.py) using confluent-kafka and boto3 to read from Kafka and save raw JSON files directly into LocalStack S3, bypassing complex Java JAR dependencies.
    Big Data Processing (Spark): Wrote spark_consumer.py using PySpark. Spark reads the raw JSON files, applies data transformations (filtering for specific price ranges), and writes the output to an optimized Parquet format.

Architectural Pivot

Initially, Spark was configured to read directly from Kafka. However, due to Java/Scala version mismatches with the Kafka connector JAR, the architecture was decoupled. Python now handles the Kafka-to-S3 ingestion, and Spark processes the files from disk, which is a more robust pattern for this environment.