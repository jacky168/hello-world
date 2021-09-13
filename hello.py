import sys

# print out python version
print(sys.version)
# the absolute path of the executable binary for the Python interpreter
print(sys.executable)


def sayHello(name):
    msg = "Hello, {}".format(name)
    return msg


# print(sayHello(name))


def forLoop():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")


if __name__ == "__main__":
    name = "Alice"
    print(sayHello(name))

    # forLoop()
