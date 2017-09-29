from sys import exit

def start():
	print("You're standing in front of a house. To your right there is a mailbox. Would you like to open it?")
	choice = input("> y/n ")
	if choice == 'y':
		print("There is a key in the mailbox. You have taken it and proceeded to the front door.")
		haunted_house()
	else:
		exit("You get run over by a bus. Good bye")


def haunted_house():
	print("The door has two locks: top and bottom. Which one would you like to try first?")
	choice = input("> ")
	if choice == 'bottom':
		print("The key fit nicely, unlocked the door and you stepped in. There is a staircase in front of you.")
	else:
		exit("The key breaks and a piano falls on top of you. Try again")


start()
























'''
Rules for if-statements

1. Every if-statement must have an else.
2. If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies.
3. Never nest if-statements more than two deep and always try to do them one deep.
4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after. 
5. Your Boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable. 


Rules for Loops

1. Use a while-loop only to loop forever, and that means probably never. This only applies to Python.
2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over. 


Tips for Debugging

1. Do not use a "debugger".
2. The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong. 
3. Make sure parts of your programs works as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little. 
'''