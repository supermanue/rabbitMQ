#!/bin/sh

python send.py
python receive.py &
receive_pid=$!
sleep 1
python send.py
sleep 1
python send.py
sleep 1
 python send.py
 sleep 1
kill $receive_pid
