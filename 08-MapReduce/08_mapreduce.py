import parsl
from parsl import python_app, bash_app
from parsl.data_provider.files import File

parsl.load()

# Map function that returns double the input integer
@python_app
def app_double(x):
    return x * 2


# Reduce function that returns the sum of a list
@python_app
def app_sum(inputs=[]):
    return sum(inputs)


# Create a list of integers
items = range(0, 4)

# Map phase: apply the double *app* function to each item in list
mapped_results = []
for i in items:
    x = app_double(i)
    mapped_results.append(x)

# Reduce phase: apply the sum *app* function to the set of results
total = app_sum(inputs=mapped_results)

print(total.result())
