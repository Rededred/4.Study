# [print(i) if not i%5 else print(i**2) for i in range(1, 30+1)]


import time
t_start = time.perf_counter()
time.sleep(1)
all_time = time.perf_counter() - t_start
print(all_time)