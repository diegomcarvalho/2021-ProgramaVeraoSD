import parsl
from parsl import python_app, bash_app

parsl.load()

@bash_app
def hello_bash(message, stdout='hello-stdout'):
    return 'echo "Hello %s"' % message

# invoke the Bash app and read the result from a file
hello_bash('World (Bash)').result()

with open('hello-stdout', 'r') as f:
    print(f.read())