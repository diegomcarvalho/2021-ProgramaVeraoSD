import parsl
from parsl import python_app

# show result()

parsl.load()

@python_app
def double(x):
    return x * 2


# invoke the Python app and print the result
print(double(2).result()+double(2).result())
#print(double(2)+double(2))