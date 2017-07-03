from sys import argv # argv = argument variable. This variable holds the arguments passed to Python scripts when ran.
# read the WYSS section for how to run this
script, first, second, third = argv # "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but "unpack" is probably the best word to describe what it does. It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# Study Drills

# 1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.

# In terminal I only gave 3 values and got an error inidicating that: ValueError: not enough values to unpack (expected 4, got 3)

# Tried commenting out 3rd variable in line 8 and running the app in the terminal. Didn't get any errors. 


# 3. Combine input with argv to make a script that gets more input from a user. Don't overthink it. Just use argv to get something, and input to get something else from the user.

town1, town2, town3 = argv
city = input()

print("One town is:", town1)
print("The other one is:", town2)
print("The third one is:", town3)
print("The last one is", city)

