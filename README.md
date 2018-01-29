# rabbitMQ
learning the basics of RabitMQ


## Installation

Guide: https://www.rabbitmq.com/install-rpm.html

Commands for my CentOS7, non root, with Pika (python client)
```
sudo yum install erlang
sudo rpm --import https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
sudo yum install  rabbitmq-server
sudo chkconfig rabbitmq-server on
sudo /sbin/service rabbitmq-server start
sudo yum install python2-pika python34-pika

```
