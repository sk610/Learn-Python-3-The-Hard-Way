from sys import argv

script, user_name, last_name = argv
question = '> '

print(f"Hi {user_name} {last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(question)

print(f"Where do you live {user_name}?")
lives = input(question)

print("What kind of computer do you have?")
computer = input(question)


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

'''
Study drills

1. Ok
2. Ok
3. Ok
4. Ok
'''
