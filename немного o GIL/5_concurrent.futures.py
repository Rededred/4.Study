"""
Помимо multiprocessing, существует несколько
библиотек и фреймворков, которые предоставляют
более высокоуровневый доступ к многопроцессорной
обработке. Например, concurrent.futures позволяет
использовать пулы потоков и процессов, предоставляя
удобный интерфейс для выполнения параллельных задач.

Используя concurrent.futures, вы можете легко
переключаться между пулами потоков и процессов
в зависимости от требований вашего приложения.
"""
import concurrent.futures

def worker(data):
    result = data * 2
    return result

data = [1, 2, 3, 4, 5, 6, 7]

# Создаём пул потоков
with concurrent.futures.ThreadPoolExecutor() as executor:
    # ВОТ ЭТО ТЕМКА, ВОТ И НОРМАЛЬНОЕ ИСПОЛЬЗОВАНИЕ ЛИСТ.МЭП() или list comprehension !!!
    # results = list(executor.map(worker, data))
    results = [worker(i) for i in data]

print('Результаты: ', results)