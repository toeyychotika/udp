import socket
import math


UDP_IP = "127.0.0.1"
UDP_PORT = 5025
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
  
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:",data
    
    factorial = 1
    num = int(data)
    for i in range(1,num + 1):
       factorial = factorial*i

    result = str(factorial)
    

    if factorial:
        sent = sock.sendto(result,addr)
        print "Sent back"
    
