people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


if cars > people or trucks < cars:
    print("Oh my, its true")
elif cars < people or trucks > cars:
    print("This is crazy")
else:
    print("high five!")

"""
Study Drills

1. elif and else works like it would in normal speech. It gives the code multiple conditions, and then if it doesnt meet any of those the block of code is skipped.

2. The answers will be different.

3.Ok.

4. 
"""
