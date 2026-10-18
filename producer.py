import json
import time
import random
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=str.encode
)

# Simulate 10 ride requests
ride_id = 1
for _ in range(10):
    ride_data = {
        "ride_id": ride_id,
        "pickup_lat": round(random.uniform(40.70, 40.80), 4),
        "pickup_lon": round(random.uniform(-74.00, -73.90), 4),
        "dropoff_lat": round(random.uniform(40.70, 40.80), 4),
        "dropoff_lon": round(random.uniform(-74.00, -73.90), 4),
        "passenger_count": random.randint(1, 4),
        "price": round(random.uniform(15.50, 85.20), 2)
    }
    
    # Send to Kafka
    producer.send('ride_events', key=str(ride_id), value=ride_data)
    print(f"Produced ride {ride_id}")
    ride_id += 1
    time.sleep(1)

producer.flush()
print("Finished producing 10 ride events!")