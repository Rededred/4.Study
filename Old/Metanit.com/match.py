def print_hello(language):
    match language:
        case 'russian':
            print('Привет')

        case 'english' | 'american': print('Hello')

        case 'german':
            print('Hallo')

        case _: print('Undefined')


print_hello('english')
print_hello('american')
print_hello('german')
print_hello('russian')
print_hello('hahaha')
