"""Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам
та обмінюватися повідомленнями."""

import socketserver

users = dict()


class TreadingTCPServer(socketserver.ThreadingTCPServer, socketserver.TCPServer):
    pass


class TCPHandler(socketserver.BaseRequestHandler):
    clients = []

    def handle(self):
        self.clients.append(self.request)
        print('Connect IP: {}'.format(self.client_address[0]))

        data = self.request.recv(1024).strip()
        ip, port = self.client_address
        users.setdefault(ip, f"User {len(users)}")
        user = users.get(ip)
        # self.request.send(f'Message: [{user}] --> {data.decode()}'.encode())
        for client in self.clients:
            client.sendall(f'Message: [{user}] --> {data.decode()}'.encode())

        self.clients.remove(self.request)
        self.request.close()


with TreadingTCPServer(('127.0.0.1', 3223), TCPHandler) as server:
    server.serve_forever()
