#'epoch' asgiref-3.6.0 django-4.1.6 sqlparse-0.4.3 tzdata-2022.7
import json
from datetime import datetime
import time;
import pandas as pd
from settings import PRODUCER_TOPIC, DELAY,KAFKA_BROKER_URL
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

if producer is not None:
    data = pd.read_csv('../model/data/south2_S.csv',
            parse_dates = ['Datetime'],
            usecols=['Datetime', 'precip_totl_tp', 'prsn_atmos_max_tp_prcedt', 'prsn_atmos_min_prmier_tmp', 'rad_gobal', 'tmp_air', 'tmp_pt_rose', 'humid_rlative_air','vent_vitess_tmp'] ); # todo: complte this line with test csv file.
    for index, row in data.iterrows():
        item = {
            'Datetime': str(row['Datetime']),
            'precip_totl_tp': row['precip_totl_tp'],
            'prsn_atmos_max_tp_prcedt': row['prsn_atmos_max_tp_prcedt'],
            'prsn_atmos_min_prmier_tmp': row['prsn_atmos_min_prmier_tmp'],
            'rad_gobal': row['rad_gobal'],
            'tmp_air': row['tmp_air'],
            'tmp_pt_rose': row['tmp_pt_rose'],
            'humid_rlative_air': row['humid_rlative_air'],
            'vent_vitess_tmp' : row['vent_vitess_tmp']
        }
        body = {"data" : [item], "current_datetime": datetime.utcnow().isoformat()}
        bodyJson = json.dumps(body).encode("utf-8")
        producer.send(PRODUCER_TOPIC, bodyJson)
        producer.flush()
        time.sleep(DELAY) 
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       