from random import randrange

def list_generator(n=10, min=-10, max=10):
    return [randrange(min, max) for _ in range(n)]
