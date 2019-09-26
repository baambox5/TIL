def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('ahahsh')
    return wrapper


@hello
def bye():
    print('byebye')

bye()