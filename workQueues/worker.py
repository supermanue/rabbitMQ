#!/usr/bin/env python
import pika
import time
import sys


name=sys.argv[1]
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(" [*] " + name + ' Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] " + name + " Received " + str(body))
    time.sleep(body.count('.'))
    
    print( " [x] " + name + " Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
