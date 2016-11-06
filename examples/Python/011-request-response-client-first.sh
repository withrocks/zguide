#!/bin/bash

echo "Starting the client..."
python hwclient.py &
client_pid=$!
echo "Waiting a bit..."
sleep 1

echo "Then starting the server, expecting the same result as before..."
python hwserver.py &

echo "Wait for the client to finish..."
wait $client_pid

echo "Kill the server"
pkill -9 -f "hwserver.py"

