-- Initial schema

CREATE TABLE web_events (
    inserted_time TIMESTAMP PRIMARY KEY,
    clickstream_data JSONB
)