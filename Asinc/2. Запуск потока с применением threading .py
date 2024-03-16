import threading

class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
    def run(self):
        print('Starting processing %i...' % x)
        is_prime(self.x)

my_input = [2, 193, 323, 1327, 433785907]

threads = []
