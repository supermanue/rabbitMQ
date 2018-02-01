#!/usr/bin/env python
#DOC: https://www.rabbitmq.com/tutorials/tutorial-six-python.html

import pika
from time import sleep
from random import randint

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

#por aqui te entran los mensajes
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#props son las pripiedades. Aqui tiene de nuevo:
#   correlation_id (lo que identifica al mensaje)
#   routing_key (la cola donde mandas de vuelta la respuesta)
#   ack: pa decir cuando haya llegado

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    sleep (randint(1,5))
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
