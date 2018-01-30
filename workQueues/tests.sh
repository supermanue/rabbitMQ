#!/bin/sh

python worker.py worker1 &
worker1_pid=$!
sleep 1

python worker.py  worker2 &
worker2_pid=$!
sleep 1

python new_task.py 1 second.
python new_task.py 5 seconds.....
python new_task.py 1 second.
python new_task.py 5 seconds.....
python new_task.py 1 second.
python new_task.py 5 seconds.....

sleep 20

kill $worker1_pid
kill $worker2_pid
