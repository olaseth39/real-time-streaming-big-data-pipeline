SELECT 
    passenger_count,
    COUNT(*) AS total_rides,
    AVG(price) AS average_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM {{ ref('stg_rides') }}
GROUP BY passenger_count