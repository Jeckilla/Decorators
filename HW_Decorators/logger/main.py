from tools import logger, test_1

@logger
def hello_world():
    return 'Hello World'

@logger
def summator(a, b=0):
    return a + b

@logger
def div(a, b):
    return a / b



if __name__ == '__main__':
    test_1()
    hello_world()
    summator(4.3, b=2.2)
    div(9, 3)


