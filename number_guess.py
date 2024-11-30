import random

top_range = input("Enter top range: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0 :
        print("Enter larger number next time")
        quit()
else:
    print("Enter a number next time")
    quit()

random_number = random.randint(0 , top_range)
print(random_number)
guess = 0
while True:
    guess += 1
    guess_number = input("Make a guess: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Enter a number next time")
        

    if guess_number == random_number:
        print("You got it right!")
    else:
        print("You are wrong!")
        continue
    if guess == 1:
        print("You got it after "+str(guess)+" guess")
    
    else:
        print("You got it after "+str(guess)+" guesses")    
    break    
