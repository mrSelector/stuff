import os
import socket

unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)
sock.listen(7)
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        data = result.decode()
        numbers = data.split(',')
        res = int(numbers[0]) + int(numbers[1])
        print(res)
        client.send(f'Result: {res}'.encode())

