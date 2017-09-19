

def swoop(stuff, increment):

	i = 0
	numbers = []


	while i < stuff:
	    print(f"At the top i is {i}")
	    numbers.append(i)

	    i = i + increment
	    print("Numbers now: ", numbers)
	    print(f"At the bottom i is {i}")


	print("The numbers: ")
	for num in numbers:
	    print(num)

crazy = 15
increment = 2
super = swoop(crazy, increment)

"""
Study Drills

1. Ok
2. Ok
3. 
"""