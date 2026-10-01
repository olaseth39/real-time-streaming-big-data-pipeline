import json
import time
import random
from confluent_kafka import Producer

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

# Optional: Callback to see if delivery succeeded
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Produced event to topic {msg.topic()} [partition {msg.partition()}]")

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
    
    # Convert to JSON and send to Kafka
    producer.produce('ride_events', key=str(ride_id), value=json.dumps(ride_data), callback=delivery_report)
    ride_id += 1
    
    # Sleep 1 second to simulate real-time streaming
    time.sleep(1)

# Wait for all messages to be delivered
producer.flush()
print("Finished producing 10 ride events!")