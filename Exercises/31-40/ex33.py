
'''
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
'''
"""
Study Drills

1. Ok
2. Ok
3. Ok
4. Ok
5. 
"""

def swoop(stuff, increment):

	i = []
	numbers = []

	for i in range(0,7):
		print(f"At the top i is {i}")
		numbers.append(i)

	print("The numbers: ")
	for x in numbers:
		print(x)


stuff = 6
increment = 2

swoop(stuff, increment)