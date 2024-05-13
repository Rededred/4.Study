def read_write(source, target):
    rBytes = True
    with open(source, mode='rb') as read_file, open(target, mode='wb') as write_file:
        while rBytes:
            rBytes = read_file.read(1024)
            write_file.write(rBytes)

