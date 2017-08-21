# importing argv module
from sys import argv
# arguments that we need to pass to our script.
script, filename = argv
# opening the txt file and assinging this to a variable txt.
txt = open(filename)
# printing the filename.
print(f"Here's your file {filename}:")
# printing the contexts of the file as assigned in line 6.
print(txt.read())
closing = close(filename)
# printing a string
'''
print("Type the filename again:")
# asking for input of a file name and assining that input to a variable.
file_again = input("> ")
# opening the file assigned to file_again and assinging it to another variable
txt_again = open(file_again)
# printing contents of this file.
print(txt_again.read())
'''

'''
Study drills

1. Ok.
2. Ok.
3. Ok.
4. Ok.
5. If you use argv then you gotta know the name of the file in advance, while input allows user to provide that information.
6. Not ok.
7. Ok


'''
