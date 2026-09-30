Real-Time Streaming & Big Data Pipeline

A senior-level data engineering project processing millions of NYC Taxi ride events in real-time using Apache Kafka, Spark, dbt, and Terraform.
Day 1: Architecture & Infrastructure (Terraform & LocalStack)

Objective: Establish the foundational cloud infrastructure using Infrastructure as Code (IaC) principles, provisioning a local Data Lake without incurring cloud costs.

Tech Stack: Docker, LocalStack (AWS S3 Emulator), Terraform, AWS CLI.
Implementation Steps

    Local Cloud Emulation: Deployed LocalStack via Docker to emulate AWS S3 locally, providing a zero-cost, zero-suspension-risk environment for development.
    Infrastructure as Code (Terraform): Wrote main.tf to programmatically provision an S3 bucket (raw-ride-data) for the Data Lake. Configured the AWS provider to bypass STS validation and point to the LocalStack endpoint.
    Execution: Successfully ran terraform init, terraform plan, and terraform apply to build the infrastructure without manual console intervention.