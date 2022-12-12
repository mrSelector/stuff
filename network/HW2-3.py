# Задание 2
# Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети. Он принимает
# сообщения определенного формата, в котором будет идентификатор устройства и печатает
# новые подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный
# идентификатор устройства на сервер, уведомляя о своем присутствии.

import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print(f'Connect user IP: {self.client_address}')
        print(f'Message: {data.decode()}')
        socket.sendto(data, self.client_address)


with socketserver.UDPServer(('7.7.7.77', 8888), UDPHandler) as server:
    server.serve_forever()




