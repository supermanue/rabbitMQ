#!/bin/sh

python rpc_server.py &
server1_pid=$!
sleep 1
python rpc_client.py 10
sleep 1
python rpc_client.py 20
sleep 1
python rpc_client.py 30
sleep 1

echo "starting other server and non blocking calls makes everything go faster"
python rpc_server.py &
server2_pid=$!
sleep 1
python rpc_client.py 10 &
sleep 1
python rpc_client.py 20 &
sleep 1
python rpc_client.py 30 &
sleep 1
python rpc_client.py 40 &
sleep 1
python rpc_client.py 50 &
sleep 20



kill $server1_pid
kill $server2_pid
