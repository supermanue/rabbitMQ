#!/usr/bin/env python
#DOC: https://www.rabbitmq.com/tutorials/tutorial-four-python.html
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#es directo porque vamos a emitir a un numero fijo de colas conocidas de antemano
#y diferentes mensajes van a diferentes colas
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

#esto entra como parametro de entrada. Se ejecuta como python emit_log.py <severity> <mensaje>
severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

#y mandamos el mensaje a la cola <severity> del unico exchange que tenemos
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()
