from sys import argv

script, filename = argv

filename = open('test.txt')

print("Here is your file: ".format(filename))
print(filename.read())
