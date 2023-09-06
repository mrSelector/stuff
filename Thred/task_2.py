"""Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!».
Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!».
За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення
виконує видалення цього файлу. Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд.
Створіть файл руками та перевірте виконання програми.

"""
import asyncio
import os

# """Створюємо файл"""
# with open('maybe_wow.txt', 'w') as f:
#     f.write('Wow')


async def read(future):
    """Співпрограма шукає слово у файлі, якщо знаходить то створює подію"""

    while True:
        try:
            with open('maybe_wow.txt', 'r') as file:
                if 'Wow' in file.read():
                    # print('Nice')
                    file.close()
                    future.set_result('File deleted')
                    break
                else:
                    print('"Wow" not found')
                    await asyncio.sleep(5)
        except FileNotFoundError:
            print('File not found')
            await asyncio.sleep(5)


async def file_del(future):
    """Співпрограма очікує на подію, якщо є подія то видаляє файл"""
    result = await future
    os.remove('maybe_wow.txt')
    print(result)


async def main():
    """Спіпрогама створює 'футур' то 'таски' """
    fut = asyncio.Future()
    asyncio.create_task(read(fut))
    asyncio.create_task(file_del(fut))
    await fut


if __name__ == "__main__":
    asyncio.run(main())

