import requests
import random
import string

def random_name(length=5):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# Random threshold price generator
def random_threshold(min_val=50.0, max_val=200.0):
    return round(random.uniform(min_val, max_val), 2)

# Random symbol generator
def random_symbol(length=4):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

def seed_alerts(num_alerts):
    url = "http://localhost:8000/alerts/"
    payload = [{"name": random_name(), "threshold_price": random_threshold(), "symbol": random_symbol()} for i in range(num_alerts)]

    headers = {
        'Content-Type': 'application/json'
    }
    for data in payload:
        response = requests.request("POST", url, headers=headers, json=data)
        print(response.text)

seed_alerts(10)
