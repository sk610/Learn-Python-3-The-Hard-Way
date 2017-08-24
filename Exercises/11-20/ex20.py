# importing a python module
from sys import argv
# defining args
script, input_file = argv
# defining print_all funtion and saying that we need an f argument (which is a file)
def print_all(f):
    # printing the contents of the argument passed to the function.
    print(f.read())
# defining rewind function with f argument.
def rewind(f):
    # 
    f.seek(0)
# defining a function and required arguments.
def print_a_line(line_count, f):
    # printing
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


'''
Study drills

1. Ok.

'''
