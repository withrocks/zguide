#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import sys

should_log = bool(sys.argv[1]) if len(sys.argv) > 1 else False
def log(msg):
    if should_log:
        print(msg)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    log("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(0.2)

    #  Send reply back to client
    socket.send(b"World")
