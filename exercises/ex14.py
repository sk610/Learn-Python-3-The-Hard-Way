from sys import argv

script, user_name, hometown = argv
popcorn = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(popcorn)

print(f"Where are you from originally {user_name}?")
home = input(popcorn)

print(f"Where do you live {user_name}?")
lives = input(popcorn)

print(f"What kind of computer do you have?")
computer = input(popcorn)

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are from {home}. Not sure where that is either.
And you have a {computer} computer. Nice.
''')
