"""Розробіть сокет-сервер на основі бібліотеки asyncio."""

import asyncio


async def handle_client(reader, writer):
    """Отримання даних від клієнта"""

    data = await reader.read(100)
    message = data.decode()
    # print(message)
    response = f"from server --> {message}!"
    encoded_response = response.encode()

    # Відправка відповіді клієнту

    writer.write(encoded_response)
    await writer.drain()
    writer.close()


async def start_server():
    # Створення сервера
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)
    print("server started")
    async with server:
        await server.serve_forever()


asyncio.run(start_server())

"""Клієнт"""


async def send_message():
    """Підключення до сервера"""
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    """Відправка повідомлення серверу"""
    message = input('Enter message: ')
    encoded_message = message.encode()
    writer.write(encoded_message)
    await writer.drain()

    """Отримання відповіді від сервера"""
    data = await reader.read(100)
    response = data.decode()
    print(f'Response from server: {response}')
    writer.close()
    await writer.wait_closed()


"""Відправка повідомлення до сервера"""
asyncio.run(send_message())
