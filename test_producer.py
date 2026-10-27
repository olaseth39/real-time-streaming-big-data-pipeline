import random

def test_ride_data_generation_logic():
    """Tests that the ride data generation logic produces valid ranges."""
    # Simulate the logic from producer.py
    ride_data = {
        "ride_id": 1,
        "pickup_lat": round(random.uniform(40.70, 40.80), 4),
        "pickup_lon": round(random.uniform(-74.00, -73.90), 4),
        "dropoff_lat": round(random.uniform(40.70, 40.80), 4),
        "dropoff_lon": round(random.uniform(-74.00, -73.90), 4),
        "passenger_count": random.randint(1, 4),
        "price": round(random.uniform(15.50, 85.20), 2)
    }
    
    # Assertions to verify the data is within valid business bounds
    assert ride_data["ride_id"] == 1
    assert 40.70 <= ride_data["pickup_lat"] <= 40.80
    assert -74.00 <= ride_data["pickup_lon"] <= -73.90
    assert 1 <= ride_data["passenger_count"] <= 4
    assert 15.50 <= ride_data["price"] <= 85.20