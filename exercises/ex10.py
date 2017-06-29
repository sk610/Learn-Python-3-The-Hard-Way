" I am 6'2\" tall." # escape double-quote inside string
' I am 6\'2" tall.' # escape single-quote inside string

# tab indent for the line below.
tabby_cat = "\tI'm tabbed in."
# starts "on a line." on a new line.
persian_cat = "I'm split\non a line."
# creates singular backslashes around "a"
backslash_cat = "I'm \\ a \\ cat."
# takes a fat_cat string and tabs in every line. We don't have to use \n here because we are using """ for the string. (Still used it "just because" in line 15)
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
