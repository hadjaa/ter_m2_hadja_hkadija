from django.shortcuts import render
import json
from kafka import KafkaConsumer
KAFKA_BROKER_URL = "localhost:9092"
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"

def home(request):
    consumer = KafkaConsumer(ANOMALIES_TOPIC, bootstrap_servers=[KAFKA_BROKER_URL])
    message = consumer.poll(timeout_ms=500)
    data = [message]
    if message is not None and len(message) != 0:
        data.append({'checkin': 'test'})
        for message in consumer:
            record = json.loads(message.value.decode('utf-8'))
            print("found", record)
            data.append(record)
            break
    print("data", data)
    return render(request, 'home.html', {'data': data})
