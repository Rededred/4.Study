
print("before import")
from math import sqrt

print("before functionA")
def functionA():
    from forThought1 import functionB
    functionB()
    print("Function A")


print("before functionB")
def functionB():
    print("Function B {}".format(sqrt(100)))

print("before name guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after name guard")