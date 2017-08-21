'''
close - Closes the file.
read - reads the contents of the file.
readline - reads just one line of a text file.
truncate - empties the file.
write('stuff') - writes "stuff" to the file.
seek (0) - move the read/write location to the beginning of the file.
'''
# importing a module
from sys import argv
# defining what arguments we need
script, filename = argv
# printing a messgae to the user and using filename argument that the user provided
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# placing a string on the line where user inputs info.
input("?")

print("Opening the file...")
target = open(filename, 'w') # w means opening the file in write mode
print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we close it.")
target.close()

'''
Study drills
1. Ok
2. Ok
3. Ok
4. Looks like we don't need line 23. 
'''
