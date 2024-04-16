import socket
   
UDP_IP = "192.168.15.3"
UDP_PORT = 11666

ANGULO = 30

sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP

for i in range(0,ANGULO+1):

    sock.sendto(str(i).encode(), (UDP_IP, UDP_PORT))

# while True:
#     sock.sendto(str(ANGULO).encode(), (UDP_IP, UDP_PORT))

