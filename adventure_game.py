name = input("Type your name: ")
print("Welcome to the adventure "+name+".Let's begin")
answer = input("Welcome traveller!Choose your pair of boots to wear on your journey (Combat/Millitary/Tactical/Trooper/No boot\)? ").lower()

if answer == "Combat" or answer == "Millitary" or answer == "Tactical" or answer == "Trooper":
    print("Okay,let's go!")
    answer1 = input("There are two ways to start,walk through bridge or swim in water\n(walk/swim)? ").lower()
    if answer1 == "walk":
        print("You won!")
    elif answer1 == "swim":
        print("You got your boots wet,you can't go further!")
    else:
        print("Choose a correct option!")
elif answer == "No boot":
    print("You can't go through the jungle without boots.You fail!")
else:
    print("Choose a correct option!")

