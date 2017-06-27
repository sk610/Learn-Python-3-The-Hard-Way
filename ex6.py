# A string is usually a bit of text you want to display to someone or "export" out of the program you are writing.

# defined 2 variables : types_of_people and x.
types_of_people = 10
# f is format, and puts types_of_people value between {}
x = f"There are {types_of_people} types of people."

# defined 3 variables: binary, do_not and y.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# printed variables
print(x)
print(y)

# printed more variables
print(f"I said: {x}.")
print(f"I also said: '{y}'")

# defined that variable hilarious is False, and defined that joke_evaluation is a string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
