

from multiprocessing import Pool, cpu_count

def worker(data):
    result = data * 2
    return result

data = [1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
    # Создаём пул процессов
    pool = Pool(processes=cpu_count())

    # Используем многопроцессорный пул для обработки данных
    results = pool.map(worker, data)
    # result = pool.(worker(i) for i in data)

    # Завершаем пул
    pool.close()
    pool.join()

    print('Результаты: ', results)