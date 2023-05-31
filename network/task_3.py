# Створіть сокет, який приймає повідомлення з двома числами, що розділені комою.
# Сервер має конвертувати рядкове повідомлення у два числа й обчислювати його суму.
# Після успішного обчислення повертати відповідь клієнту.
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 3223))
sock.listen(3)
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        data = client.recv(1024).decode('utf-8')
        numbers = data.split(',')
        result = int(numbers[0]) + int(numbers[1])
        client.send(f'Result: {result}'.encode())
        client.close()
