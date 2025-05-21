from kafka import KafkaProducer
from json import dumps
from time import sleep
from random import randint
topic_name = 'RandomNumberStreaming'
kafka_server = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=kafka_server,value_serializer = lambda x:dumps(x).encode('utf-8'))
for e in range(100):
    data = str(randint(1, 100))
    producer.send(topic_name, value=data)
    print(str(data) + " sent")
    sleep(2)
producer.flush()
