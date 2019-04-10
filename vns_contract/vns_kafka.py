from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from kafka.structs import TopicPartition
import time

def pushProducer(url, topic_name, msg):
    producer = KafkaProducer(bootstrap_servers=[url])   
    producer.send(topic_name, msg)
    producer.close()


def pollConsumer(url, offset, topic_name, func):
    consumer = KafkaConsumer(group_id='0',bootstrap_servers=[url],auto_offset_reset=offset)
    consumer.subscribe(topics=(topic_name))
    while True:
        msg = consumer.poll(timeout_ms=2000)
        #print(msg)
        func(msg)
        #time.sleep(2)

def syncConsumer(url, offset, topic_name, func):
    consumer = KafkaConsumer(bootstrap_servers=[url])
    print(consumer.partitions_for_topic(topic_name))
    consumer.assign([TopicPartition(topic=topic_name, partition=0)])
    #consumer.subscribe(topics=('VNS'))
    #consumer.assign(partitions=0)
    consumer.seek(TopicPartition(topic=topic_name, partition=0), offset)
    for message in consumer:
        func(message)

