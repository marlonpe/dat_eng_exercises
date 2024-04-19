import os
import subprocess
import psycopg2
import pytest

def count_records(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM web_events")
        return cursor.fetchone()[0]

@pytest.fixture
def db_connection():
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    yield connection
    connection.close()

def test_full_integration_flow(db_connection):

    subprocess.run(["python", "src/clickstream_generator.py"], check=True)
    subprocess.run(["python", "src/data_inserter.py"], check=True)

    record_count = count_records(db_connection)
    assert record_count > 0