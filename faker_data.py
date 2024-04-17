from faker import Faker
import json
import random

fake = Faker()

clickstream_data = []

for _ in range(500):
    event = {
        "user_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
        "event_type": random.choice(["click_product", "add_to_cart", "purchase", "search"]),
        "product_id": fake.uuid4(),
        "referrer_url": fake.url(),
        "current_url": fake.url(),
        "location": fake.city(),
        "device": random.choice(["iPhone", "Android Phone", "Desktop", "Tablet"]),
        "browser": random.choice(["Safari", "Chrome", "Firefox", "Edge"]),
        "session_duration": random.randint(300, 5000)
    }
    clickstream_data.append(event)

with open("clickstream_data.json", "w") as f:
    json.dump(clickstream_data, f, indent=4)

print("data written succesfully")