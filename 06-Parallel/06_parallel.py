import parsl
from parsl import python_app
from parsl.data_provider.files import File

parsl.load()


@python_app
def wait_sleep_double(x, foo_1, foo_2):
    import time

    time.sleep(2)  # Sleep for 2 seconds
    return x * 2


# Launch two apps, which will execute in parallel, since they do not have to
# wait on any futures
doubled_x = wait_sleep_double(10, None, None)
doubled_y = wait_sleep_double(10, None, None)

# The third app depends on the first two:
#    doubled_x   doubled_y     (2 s)
#           \     /
#           doubled_z          (2 s)
doubled_z = wait_sleep_double(10, doubled_x, doubled_y)

# doubled_z will be done in ~4s
print(doubled_z.result())
