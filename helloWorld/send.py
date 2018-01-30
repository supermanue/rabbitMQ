#!/usr/bin/env python
#DOC: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika #pika is the name for rabbit Pyhton client
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello') #que creation

#send message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

#alter user
print(" [x] Sent 'Hello World!'")

#close connection
connection.close()
