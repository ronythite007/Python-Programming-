# gusssing the right number from random import
import random

random_number=random.randint(1,50)

randoms=None
count=0
while randoms != random_number:
    guess=int(input("enter your guess:- "))
    count+=1
    if guess==random_number:
        print("you guessed right")
        break
    else:
        if random_number>guess:
            print("guess larger  no.")
        else:
            print("guess smaller number")    
print(f"you guessed in {count} chances")


