# Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі.
# Він приймає повідомлення певного формату, де буде ідентифікатор пристрою,і друкує
# нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме унікальний
# ідентифікатор пристрою на сервер, повідомляючи про свою присутність.
#


import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print(f'Connect user IP: {self.client_address}')
        print(f'Message: {data.decode()}')
        socket.sendto(data, self.client_address)


with socketserver.UDPServer(('7.7.7.77', 8888), UDPHandler) as server:
    server.serve_forever()


"""UDP_client"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello mr.Selector', ('7.7.7.77', 8888))
data = sock.recv(1024)
print(data.decode())