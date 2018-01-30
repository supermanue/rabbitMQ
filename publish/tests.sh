#!/bin/sh

python receive_logs.py logger_1 &
receive_pid=$!

python receive_logs.py logger_2 &
receive_pid2=$!

sleep 1
python emit_log.py hola
sleep 1
python emit_log.py hola 2
sleep 1
python emit_log.py hola 3
 sleep 3

kill $receive_pid
kill $receive_pid2
