import parsl
from parsl import python_app

parsl.load()

@python_app
def hello_python (message):
    import random
    i = random.randint(1,10)
    return f'Hello {message} {i}'


# invoke the Python app and print the result
print(hello_python('World (Python)').result())
