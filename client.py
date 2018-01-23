import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5022
MESSAGE = "4"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
    sent = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print "Waiting..."
    data, server = sock.recvfrom(1024)
    print data

finally:
    print "Terminate"
    sock.close()
    

