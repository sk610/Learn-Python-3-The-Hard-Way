print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 or door #3?""")

door = input("> ")

if door == "1":
     print("There's a giant bear here eating a cheese cake.")
     print("What do you do?")
     print("1. Take the cake.")
     print("2. Scream at the bear.")

     bear = input("> ")

     if bear == "1":
         print("The bear eats your face off. Good job!")
     elif bear == "2":
         print("The bear eats your legs off. Good job!")
     else:
         print(f"Well, doing {bear} is probably better.")
         print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Ctulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You stand in front of Oasis.")
    print("1. You think it is fake and this is just a dream.")
    print("2. The water is poison and you're afraid to drink it.")
    print("3. This is just a test, and you move forward.")

    oasis = input("> ")

    if oasis == "1":
        print("Neo, wake up!")

    if oasis == "2":
        print("You take a step back and avoid water.")

    if oasis == "3":
        print("Good job, explorer!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
