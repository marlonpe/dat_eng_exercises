{{ config(materialized='incremental', unique_key="inserted_time") }}

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

SELECT *
FROM raw_data

{% if is_incremental() %}
WHERE inserted_time > (SELECT max(inserted_time) from {{this}})
{% endif %}
