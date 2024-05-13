"""Чтобы работать с потоками в Python, вы можете создавать
 экземпляры класса Thread из модуля threading и запускать
 их. Важно помнить, что GIL ограничивает многозадачность
 на уровне интерпретатора, поэтому потоки в Python подходят
 для задач, которые больше связаны с ожиданием ввода-вывода,
 чем с интенсивной обработкой данных."""

import threading

def print_numbers():
    for i in range(1, 6):
        print(f'Number: {i}')

def print_letters():
    for letter in 'abcde':
        print(f'Letter: {letter}')

# Создаём 2 потока
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждём, пока оба потока завершатся
thread1.join()
thread2.join()