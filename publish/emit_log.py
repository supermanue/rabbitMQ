#!/usr/bin/env python
#DOC: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#esto es lo importante.
#exchange es la pieza que gestiona a que cola/colas se envian los mensajes
#"fanout" es que el productor manda lo mismo a todos los consumidores que
# se registren en el exchange  "logs"

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

#con esto mandas un exchange al canal "logs"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()
