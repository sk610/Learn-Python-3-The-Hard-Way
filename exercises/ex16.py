# close - closes the file. Like file -> save in your editor.
# read - Reads the contents of the file. You can assign the results to a variable.
# readline - reads just one line of a text file.
# truncate - empries the file; watch out if you care about the file.
# write('stuff') - writes 'stuff' to the file.
# seek(0) - move the read/write location to the begining of the file.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # 'w' stands for write.

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you to write three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}" + '\n' + f"{line2}" + '\n' + f"{line3}" + '\n')

print("And finally, we close it.")
target.close()
