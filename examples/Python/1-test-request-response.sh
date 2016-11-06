python hwserver.py &
pid=$!
echo "Started server, pid=$pid"

echo "Starting client..."
python hwclient.py

echo "Client finished executing, killing the server"
kill -9 $pid
