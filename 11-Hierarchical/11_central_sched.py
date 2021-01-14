import parsl
from parsl import python_app, bash_app

parsl.load()

@bash_app
def pi(tag, stdout='hello-stdout'):
    return f'cd app; python 05_monte_carlo_pi.py {tag} > {tag}.txt'

# invoke the Python app and print the result
bag = [pi('result1'), pi('result2')]

for i in bag:
    i.result()

for i in ['app/result1.txt', 'app/result2.txt']:
    with open(i, 'r') as f:
        print(f.read())