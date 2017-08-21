from sys import argv

script = argv

filename = input("Type the name of the file: ")

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())
