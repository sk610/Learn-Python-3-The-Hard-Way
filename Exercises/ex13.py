from sys import argv # importing from python modules.
# read the WYSS section for how to run this
script, first, second, third = argv # argv is "argument variable". It holds the arguments passed to the Python script when the script is ran.

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


'''
Study drills

1. Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv # argv is "argument variable". It holds the arguments passed to the Python script when the script is ran.
ValueError: not enough values to unpack (expected 4, got 3) - the script expected 4 arguments from me as it expects it per line 3.

2.

from sys import argv

script, team = argv

print("The script is called", script)
print("The team that won today is", team)

----

from sys import argv

script, teamWon, teamLost = argv

print("The script is called", script)
print("The team that won today is", teamWon)
print("The team that lost today is", teamLost)

3.

from sys import argv

script, name, lastname = argv

middlename = input("What's your middle name? ")

print("Your first name is", name)
print("Your last name is", lastname)
print("And your middle name is", middlename)

4. Ok.
