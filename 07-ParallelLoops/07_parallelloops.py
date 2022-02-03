import parsl
from parsl import python_app
from parsl.data_provider.files import File

parsl.load()


@python_app
def generate(limit):
    from random import randint

    """Generate a random integer and return it"""
    return randint(1, limit)


rand_numbers = []
for i in range(1, 5):
    rand_numbers.append(generate(i))

# Wait for all apps to finish and collect the results
outputs = [r.result() for r in rand_numbers]

print(outputs)
