import socketserver


class ChatHandler(socketserver.BaseRequestHandler):
    clients = []

    def handle(self):
        self.clients.append(self.request)
        print(f"New connection from {self.client_address[0]}:{self.client_address[1]}")

        while True:
            try:
                # Очікування повідомлення від клієнта
                message = self.request.recv(1024).decode()
                if not message:
                    break

                # Виведення повідомлення клієнта на серверній консолі
                print(f"{self.client_address[0]}:{self.client_address[1]} says: {message}")

                # Розсилка повідомлення всім підключеним клієнтам (крім відправника)
                for client in self.clients:
                    client.sendall(message.encode())
            except ConnectionResetError:
                break

        # Закриття з'єднання з клієнтом
        self.request.close()
        self.clients.remove(self.request)
        print(f"Connection with {self.client_address[0]}:{self.client_address[1]} closed")


HOST = '127.0.0.1'
PORT = 55555

# Створення сервера
server = socketserver.ThreadingTCPServer((HOST, PORT), ChatHandler)
print(f"Server started on {HOST}:{PORT}")

# Запуск сервера (без обмеження кількості клієнтів)
server.serve_forever()
