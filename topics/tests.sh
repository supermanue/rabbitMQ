#!/bin/sh

python receive_logs_topic.py receiver1 "#"  &
receive1_pid=$!
sleep 1
python receive_logs_topic.py receiver2 "kern.*"  &
receive2_pid=$!
sleep 1
python receive_logs_topic.py receiver3 "*.critical"  &
receive3_pid=$!
sleep 1

python emit_log_topic.py kern.critical mensaje critico de kernel
sleep 1

python emit_log_topic.py kern.issue problemilla del kernel
sleep 1


python emit_log_topic.py other.critical problema critico en otro sitio
sleep 1


python emit_log_topic.py other.issue problemilla en otro sitio
sleep 1

kill $receive1_pid
kill $receive2_pid
kill $receive3_pid
