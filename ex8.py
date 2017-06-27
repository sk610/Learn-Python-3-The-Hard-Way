# formatter is a string that is essentially blanks. By using {} we define that something will go between those braces. As we move forward to printing items, we assign numbers (1,2,3,4) or strings(one, two, etc) or boolean (True or False) to go into those places.
# When we use formatter after .format we are just taking the original string and putting it in the place of curly braces, thus resulting in 16 curlys. 

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Valera1",
        "Valera2",
        "Valera3",
        "Valera4"
))
