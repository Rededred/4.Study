# GIL - Global Interpriter Lock
import threading

def worker():
    for _ in range(1000000):
        pass

# Создаём 2 потока, которые переключаются друг на друга
# с помощью GIL. В один момент только один процесс!
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждём, когда оба потока завершатся
thread1.join()
thread2.join()
