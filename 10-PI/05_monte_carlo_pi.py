import parsl
from parsl import python_app

parsl.load()


@python_app
def pi(total):
    import random

    width = 10000
    center = width / 2
    c2 = center ** 2
    count = 0
    for i in range(total):
        # Drop a random point in the box.
        x, y = random.randint(1, width), random.randint(1, width)
        # Count points within the circle
        if (x - center) ** 2 + (y - center) ** 2 < c2:
            count += 1
    return count * 4 / total


@python_app
def my_sum(a, b, c):
    return (a + b + c) / 3


a, b, c = pi(10 ** 6), pi(10 ** 6), pi(10 ** 6)
avg_pi = my_sum(a, b, c)

print(f"Valor de pi = {avg_pi.result()}")

# A Pythonic way
# tasks = [pi(10**6) for i in range(3)]
# print(sum([i.result() for i in tasks])/len(tasks))
