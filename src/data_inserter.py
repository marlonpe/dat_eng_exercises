import psycopg2
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            print("Connection succeeded")
        except Exception as e:
            print(f"Error in connection: {e}")
            exit()
        
        return self.conn

    def close(self):
        if self.conn is not None:
            self.conn.close()


class DataInserter:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def load_data_from_file(self, filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Error reading json {e}")
            exit()

    def insert_data_into_db(self, data):
        cursor = self.db_connection.cursor()
        try:
            for record in data:
                inserted_time = datetime.now()
                clickstream_data = json.dumps(record)
                cursor.execute(
                    "INSERT INTO web_events (inserted_time, clickstream_data) VALUES (%s, %s)",
                    (inserted_time, clickstream_data)
                )
            self.db_connection.commit()
            print("Data successfully loaded into db")
        except Exception as e:
            print(f"Error in data insertion: {e}")
            exit()
        finally:
            cursor.close()


def main():
    connector = DatabaseConnector()
    conn = connector.connect()

    inserter = DataInserter(conn)
    data = inserter.load_data_from_file("clickstream_data.json")
    inserter.insert_data_into_db(data)

    connector.close()


if __name__ == "__main__":
    main()