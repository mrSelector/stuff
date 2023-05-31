import socket


def parse(text_response):
    lines = text_response.split('\n')
    status, other = lines[0], lines[1:]
    protocol, code, message = status.split()
    headers = dict()
    plain_iterator = iter(other)
    for line in plain_iterator:
        line = line.strip('\r')
        line = line.strip()
        if line == '':
            break
        print(line)
        key, value = line.split(':', 1)
        headers.setdefault(key.strip(), value.strip())
        return ''.join(plain_iterator)







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
sock.send(content.encode())
answer = sock.recv(125600).decode()
print(answer)
print(parse(answer))