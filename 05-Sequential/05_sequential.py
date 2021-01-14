import parsl
from parsl import python_app, bash_app
from parsl.data_provider.files import File

parsl.load()

# Generate a random number
@python_app
def generate(limit):
      from random import randint
      """Generate a random integer and return it"""
      return randint(1,limit)

# Write a message to a file
@bash_app
def save(message, outputs=[]):
      return 'echo {} &> {}'.format(message, outputs[0])

message = generate(10)

outfile = File('output.txt')
saved = save(message, outputs=[outfile])

with open(saved.outputs[0].result(), 'r') as f:
      print(f.read())