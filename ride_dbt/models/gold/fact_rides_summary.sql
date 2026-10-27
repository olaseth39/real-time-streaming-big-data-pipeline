
SELECT 
    passenger_count,
    CASE 
        WHEN passenger_count <= 2 THEN 'Single/Pair'
        ELSE 'Group'
    END AS passenger_count_masked,  -- Security masking
    COUNT(*) AS total_rides,
    AVG(price) AS average_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM {{ ref('stg_rides') }}
GROUP BY passenger_count