from sys import argv # argv = argument variable. This variable holds the arguments passed to Python scripts when ran.
# read the WYSS section for how to run this
script, first, second, third = argv # "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but "unpack" is probably the best word to describe what it does. It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)