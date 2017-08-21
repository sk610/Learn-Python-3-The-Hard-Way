# assigned a string to the variable formatter
formatter = "{} {} {} {}"
# passing numbers to the formatter string
print(formatter.format(1, 2, 3, 4))
# passing strings to the formatter string in place of square brackets.
print(formatter.format("one", "two", "three", "four"))
# passing booleans to the string.
print(formatter.format(True, False, False, True))
# passing string to itself, thus resulting in 16 square bracket pairs.
print(formatter. format(formatter, formatter, formatter, formatter))
# passing strings to the string. It doesn't matter if strings are not on the same line as long as they are separated by commas, just like in line 6.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
