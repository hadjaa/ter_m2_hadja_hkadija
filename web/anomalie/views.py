from django.shortcuts import render
from django.http import JsonResponse
import json
from kafka import KafkaConsumer
KAFKA_BROKER_URL = "localhost:9092"
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"

def home(request):
    return render(request, 'home.html')

def anomalie(request):
    consumer = KafkaConsumer(ANOMALIES_TOPIC, bootstrap_servers=[KAFKA_BROKER_URL])
    message = consumer.poll(timeout_ms=500)
    data = []
    if message is not None and len(message) != 0:
        for message in consumer:
            record = json.loads(message.value.decode('utf-8'))
            data.append(record)
            break
    return JsonResponse({'data': data})
