import socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect('unix.sock')
sock.send('2, 5'.encode())
data = sock.recv(1024)

print(data.decode())
