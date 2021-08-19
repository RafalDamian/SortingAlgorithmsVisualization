from random import randint

def list_generator(n=10, min=1, max=10):
    return [randint(min, max) for _ in range(n)]
