import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 3223))

sock.send(b'7, 7')
result = sock.recv(1024)
print(result.decode())
sock.close()
