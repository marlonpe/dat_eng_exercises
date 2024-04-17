import psycopg2
import json
import os

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

try:
    conn = psycopg2.connect(
        dbname="postgres",#os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    print("connection succeed")
except Exception as e:
    print(f"Error in connection: {e}")
    exit()

cursor = conn.cursor()

try:
    with open("clickstream_data.json", "r") as file:
        data = json.load(file)
except Exception as e:
    print(f"Error reading json {e}")
    exit()


try:
    for record in data:
        inserted_time = datetime.now()
        clickstream_data = json.dumps(record)
        cursor.execute("INSERT INTO web_events (inserted_time, clickstream_data) VALUES (%s, %s)", (inserted_time, clickstream_data))
    conn.commit()
    print("Data successfuly load into db")
except Exception as e:
    print(f"Error in data insertion: {e}")
    exit()
finally:
    cursor.close()
    conn.close()

