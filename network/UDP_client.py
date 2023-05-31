import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello mr.Selector', ('7.7.7.77', 8888))
data = sock.recv(1024)
print(data.decode())