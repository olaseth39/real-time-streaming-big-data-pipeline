SELECT 
    ride_id,
    CAST(pickup_lat AS FLOAT) AS pickup_lat,
    CAST(pickup_lon AS FLOAT) AS pickup_lon,
    CAST(dropoff_lat AS FLOAT) AS dropoff_lat,
    CAST(dropoff_lon AS FLOAT) AS dropoff_lon,
    CAST(passenger_count AS INTEGER) AS passenger_count,
    CAST(price AS NUMERIC(10,2)) AS price
FROM rides_data
WHERE passenger_count > 0