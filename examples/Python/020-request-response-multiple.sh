#!/bin/bash
echo "Starting a single server..."
python hwserver.py &

pids=()
for i in `seq 1 3`; do
    python hwclient.py &
    pids+=($!)
done

echo "Waiting for all spawned clients..."
for p in "${pids[@]}"
do
    wait $p
done

echo "Killing the server..."
pgrep -f "hwserver.py"
pkill -9 -f "hwserver.py"
