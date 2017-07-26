# imports argv from sys.
from sys import argv

# argv script name and filename arguments.
script, filename = argv

# assign opening a file name to txt.
txt = open(filename)


# prints a message about the file.
print(f"Here's your file {filename}:")
# prints out the text from the file.
print(txt.read())
txt.close()

# prints the message to the user to type the filename.
print("Type the filename again:")
# asks the user to input the name of the file and assigns it to file_again variable.
file_again = input("> ")
# assigns opening of the file_again variable to txt_again.
txt_again = open(file_again)

# prints out what is the in the file_again to the user.
print(txt_again.read())
txt_again.close()
