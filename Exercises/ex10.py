tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
baskslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(baskslash_cat)
print(fat_cat)


# Study drills

# 1. Ok
test1 = "Testing \a this command"
test2 = "Testing \b this command"
test3 = "Testing \f this command"
test4 = "Testing \r this command"
test5 = "Testing \v this command"
test6 = "Testing \000 this command"
#test7 = "Testing \xhh this command"
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
#print(test7)

# 2. Ok
christmas = '''
Jingle bells, Jingle bells
Jingle all the way
Oh what fun it is to ride
In a 1 horse open sleigh.
'''
print(christmas)


# 3. Ok

player = 'Zidane'
club = 'Man United'
soccer = f"{player} is my favorite player of all time, \n\t I wish he played for {club} though!"
print(soccer)
