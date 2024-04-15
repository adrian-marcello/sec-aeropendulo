import socket

UDP_IP = "192.168.15.3"
UDP_PORT = 12345

def conectar():
    

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    return sock