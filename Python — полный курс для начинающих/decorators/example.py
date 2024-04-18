def deco(func):
    def wrapper(*args, **kwargs):
        print('Additional action')
        result = func(*args, **kwargs)
        print('Additional action')
        return result
    return wrapper

# def say_hello():
#     print('Hello!')
# deco(say_hello)

# print('==='*15)

@deco
def add_numbers(*, a: int, b: int) -> int:
    # print(f'Hello, {name}!')
    print('Adding numbers...')
    return a + b
# say_hello(name='Андрюха')
print(add_numbers(a=1, b=2))
# print('==='*15)


