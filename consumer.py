import json
import boto3
from confluent_kafka import Consumer

# Connect to LocalStack S3
s3 = boto3.client('s3', endpoint_url='http://localhost:4566', aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')
bucket_name = 'raw-ride-data'

# Create the bucket if it doesn't exist
s3.create_bucket(Bucket=bucket_name)

# Connect to Kafka
c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'ride_group'})
c.subscribe(['ride_events'])

print("Listening for rides from Kafka...")

try:
    ride_count = 0
    while ride_count < 10:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        
        # Parse and save to S3
        ride_data = json.loads(msg.value())
        file_name = f"ride_{ride_data['ride_id']}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(ride_data))
        print(f"Ride {ride_data['ride_id']} saved to LocalStack S3!")
        ride_count += 1

except KeyboardInterrupt:
    pass
finally:
    c.close()
    print("Finished consuming.")