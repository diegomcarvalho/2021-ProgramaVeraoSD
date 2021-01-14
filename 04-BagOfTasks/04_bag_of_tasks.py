import parsl
from parsl import python_app

parsl.load()

# Map function that returns double the input integer
@python_app
def app_random():
    import random
    return random.random()

results =  []
for i in range(0, 10):
    x = app_random()
    results.append((i,x))

for r in results:
    print(f' Id={r[0]} -> {r[1].result()}')