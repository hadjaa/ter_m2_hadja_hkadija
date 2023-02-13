import json
import os
from joblib import load
import logging
from multiprocessing import Process
import pandas as pd
import numpy as np
from kafka import KafkaConsumer, KafkaProducer
from settings import ANOMALIES_TOPIC, NUM_PARTITIONS, PRODUCER_TOPIC, KAFKA_BROKER_URL, DATA_PROCESSING_GROUP

model_path = os.path.abspath('../model/isolation_forest.joblib')
clf = load(model_path)


def detect():
    consumer = KafkaConsumer(PRODUCER_TOPIC, group_id=DATA_PROCESSING_GROUP, bootstrap_servers=[KAFKA_BROKER_URL])

    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

    while True:
        message = consumer.poll(timeout_ms=500)
        if message is None or len(message) == 0:
            continue
        for message in consumer:
            # Message that came from producer
            # print("the message is ", message, " and has type ", type(message))
            value = message.value
            record = json.loads(value.decode('utf-8'))
            #data = pd.DataFrame.from_dict(record, orient='index')
            #print ("the data", data)
            data = pd.DataFrame.from_dict(record["data"], dtype= "string")
            data = data[['precip_totl_tp', 'prsn_atmos_max_tp_prcedt', 'prsn_atmos_min_prmier_tmp', 'rad_gobal', 'tmp_air', 'tmp_pt_rose', 'humid_rlative_air','vent_vitess_tmp']]

            prediction = clf.predict(data)

            # If an anomaly comes in, send it to anomalies topic
            if prediction[0] == -1:
                score = clf.score_samples(data)
                record["score"] = np.round(score, 3).tolist()
                record = json.dumps(record).encode("utf-8")
                print("Anomalie found", record)
                producer.send(ANOMALIES_TOPIC,record)
                producer.flush()

    consumer.close()

if __name__ == '__main__':
    # One consumer per partition
    for _ in range(NUM_PARTITIONS):
        p = Process(target=detect)
        p.start()