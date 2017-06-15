import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8000))

while True:
    msg, addr = s.recvfrom(1024)
    print "got %r from %r" % (msg, addr)
