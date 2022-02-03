import parsl
from parsl import python_app, bash_app
from parsl.data_provider.files import File

parsl.load()


@bash_app
def generate(name, outputs=[]):
    return "echo $(( RANDOM % (10 - 5 + 1 ) + 5 )) &> {}".format(name)


@bash_app
def concat(inputs=[], outputs=[], stdout="stdout.txt", stderr="stderr.txt"):
    files_list = [i.filepath for i in inputs]
    return "cat {0} >> {1}".format(" ".join(files_list), outputs[0])


@python_app
def total(inputs=[]):
    total = 0
    with open(inputs[0].filepath, "r") as f:
        for l in f:
            total += int(l)
    return total


# Create 5 files with random numbers
output_files = []
for i in range(5):
    file_name = "random-%s.txt" % i
    output_files.append(generate(file_name, outputs=[File(file_name)]))

# Concatenate the files into a single file
cc = concat(inputs=[i.outputs[0] for i in output_files], outputs=[File("all.txt")])

# Calculate the average of the random numbers
totals = total(inputs=[cc.outputs[0]])

print(totals.result())
