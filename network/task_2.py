import socket
import socketserver


class UDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data, socket = self.request
        print('Connect IP: {}'.format(self.client_address))
        print('Message: {}'.format(data.decode()))


with socketserver.UDPServer(('127.0.0.1', 3223), UDPHandler) as server:
    server.serve_forever()