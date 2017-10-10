# Assigning a string to a variable.
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# printing a string.
print("Wait there are not 10 things in that list. Let's fix that.")
# returning a list of words in the string separated by a space.
stuff = ten_things.split(' ')
print(stuff)

# assigning a list to a variable.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# A While loop. While length of stuff does not equal 10.
while len(stuff) != 10:
	# Removing the last item from more_stuff list and assigning it to next_one.
	next_one = more_stuff.pop()
	# print(more_stuff)
	print("Adding: ", next_one)
	# adding the next_one variable to stuff.
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print('Let\'s do some things with stuff.')
# printing index 1 from stuff.
print(stuff[1])
# printing last index from stuff.
print(stuff[-1])
# removing the last item from stuff and printing it.
print(stuff.pop())
# print(stuff)
# Returns the string with a designated separator, an empty space in this example.
print(' '.join(stuff))
# Returning iteams from the string at 3 through 5 index (excluding 5) with # separator. (slicing a string)
print('#'.join(stuff[3:5]))
