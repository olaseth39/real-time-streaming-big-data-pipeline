import json
import boto3
from kafka import KafkaConsumer

# Connect to LocalStack S3
s3 = boto3.client('s3', endpoint_url='http://localhost:4566', aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')
bucket_name = 'raw-ride-data'

# Create the bucket if it doesn't exist
s3.create_bucket(Bucket=bucket_name)

# Connect to Kafka using kafka-python with a timeout
c = KafkaConsumer(
    'ride_events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='ride_group_4',
    consumer_timeout_ms=10000  # Stops after 10 seconds of no new messages
)

print("Listening for rides from Kafka... (Will stop after 10s of silence)")

ride_count = 0
for message in c:
    # Parse and save to S3
    ride_data = message.value.decode('utf-8')
    ride_json = json.loads(ride_data)
    file_name = f"ride_{ride_json['ride_id']}.json"
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=ride_data)
    print(f"Ride {ride_json['ride_id']} saved to LocalStack S3!")
    ride_count += 1

c.close()
print(f"Finished consuming. Saved {ride_count} rides to S3.")