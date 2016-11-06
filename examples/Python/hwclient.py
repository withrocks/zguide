#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import codecs
import sys

context = zmq.Context()

should_log = bool(sys.argv[1]) if len(sys.argv) > 1 else False
def log(msg):
    if should_log:
        print(msg)

log(">Connecting to hello world server...")

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(5):
    log(">Sending request %s ..." % request)
    request = b"Hello"
    socket.send(request)

    #  Get the reply.
    response = socket.recv()
    log(">Received reply %s [ %s ]" % (request, response))
    message = codecs.decode(request + b" " + response, "utf-8")
    print(message)
