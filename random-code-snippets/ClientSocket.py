import socket
import sys

s = socket.socket()
port = 3125
s.connect(('localhost', port))

# Custom Message #
inps = input("Enter text to transmit-")
s.sendall(inps.encode())
s.close()

inp = input("Enter quit or q-")
if inp=='q' or inp=='quit':
    print("DONE")
    sys.exit()
