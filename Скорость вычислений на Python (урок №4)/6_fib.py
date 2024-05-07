from multiprocessing import Pool
import os
import os.path
import time

workers_number = 4
final_fibonacci_number = 40

import ctypes
fibc = ctypes.CDLL(os.path.abspath('6_fib.cpp'))