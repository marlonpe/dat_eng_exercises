{{ config(materialized='table') }}

WITH raw_data AS (
    SELECT
        inserted_time,
        clickstream_data ->> 'user_id' AS user_id,
        clickstream_data ->> 'timestamp' AS event_timestamp,
        clickstream_data ->> 'event_type' AS event_type,
        clickstream_data ->> 'product_id' AS product_id,
        clickstream_data ->> 'referrer_url' AS referrer_url,
        clickstream_data ->> 'current_url' AS current_url,
        clickstream_data ->> 'location' AS location,
        clickstream_data ->> 'device' AS device,
        clickstream_data ->> 'browser' AS browser,
        (clickstream_data ->> 'session_duration')::int AS session_duration
    FROM web_events
)

SELECT
    event_timestamp,
    user_id,
    event_type,
    product_id,
    referrer_url,
    current_url,
    location,
    device,
    browser,
    session_duration
FROM raw_data
WHERE session_duration IS NOT NULL