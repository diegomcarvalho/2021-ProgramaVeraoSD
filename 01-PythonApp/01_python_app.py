import parsl
from parsl import python_app

parsl.load()

factor = 5


@python_app
def good_double(factor, x):
    import random

    return x * random.random() * factor


print(good_double(factor, 42).result())
