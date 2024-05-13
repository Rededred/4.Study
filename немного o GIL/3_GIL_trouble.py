"""
Взаимодействие потоков с GIL может привести к
неожиданным результатам, особенно если не
учитывать блокировки и многозадачность.
Когда несколько потоков пытаются изменить
одни и те же данные, могут возникнуть гонки
данных (race conditions).
"""

import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Создаём два потока
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждём, пока оба потока завершатся
thread1.join()
thread2.join()

print("Counter:", counter)