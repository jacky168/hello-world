import sys

# print out python version
print(sys.version)
# the absolute path of the executable binary for the Python interpreter
print(sys.executable)


def sayHello(name):
    msg = 'Hello, {0}'.format(name)
    return msg


name = 'Alex'
print(sayHello(name))
# if __name__ == '__main__':
#     name = 'Alex'
#     print(sayHello(name))
