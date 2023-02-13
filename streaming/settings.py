import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DELAY = 0.01
NUM_PARTITIONS = 1
OUTLIERS_GENERATION_PROBABILITY = 0.2
KAFKA_BROKER_URL = "localhost:9092"
PRODUCER_TOPIC = "incoming-data"
DATA_PROCESSING_GROUP = 'data-processing-group'
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"

SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
SLACK_CHANNEL = "anomalies-alerts"