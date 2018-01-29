#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

#este metodo es llamado cuando llega un mensaje.
#esta documentado chungamente.
#
#consumer_callback (method)
#   -The method to callback when consuming with the signature consumer_callback(channel, method, properties,body), where
#       channel: pika.Channel
#       method: pika.spec.Basic.Deliver
#       properties: pika.spec.BasicProperties
#       body: str, unicode, or bytes (python 3.x)
#
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#aqui decimos que cuando llegue un mensaje se llame a "callback"
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


#informar al usuario
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
