#!/bin/sh

python receive_log.py warning error  &
receive_pid=$!
sleep 1
python emit_log.py info hola
sleep 1
python emit_log.py warning hola
sleep 1
 python emit_log.py error  hola
 sleep 1
kill $receive_pid
