#!/usr/bin/env python
import pika
import sys

name=sys.argv[1]

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#este es el canal al que nos vamos a suscribir
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

#creamos la cola en ese canal.
#   exclusive=true es que cuando este consumidor se muere, la cola desaparece
#   al no poner queue_name la cola tiene un nombre aleatorio (mola si hay muchos consumidores)
result = channel.queue_declare(exclusive=True)

#esto es para coger el nombre y trabajar con el
queue_name = result.method.queue

#con esto le estamos diciendo al exchange "logs" que nos mande todos los mensajes a esta cola
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] ' + name + ': Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] " + name + ": " + str(body))


#y lo de siempre, cuando llega un mensaje se ejecuta "callback"
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
