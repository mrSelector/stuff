import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
    ]
content = "\n".join(content_items)
print(content)
sock.send(content.encode())
answer = sock.recv(4096).decode()
print(answer)