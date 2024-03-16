from multiprocessing import Process, Pipe

def process2(conn):
    conn.send([42, None, 'hello'])
    x = conn.recv()
    print(f'f: x={x}')
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=process2, args=(child_conn, ))
    p.start()
    y = parent_conn.recv()
    print(y)
    parent_conn.send(y[::-1])
    p.join()

