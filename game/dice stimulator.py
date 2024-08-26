import random

while True:
    print(random.randint(1,6))
    rolling_again=input("if you to roll dice again press? y/n:") 
    if rolling_again=="y":
        continue
    if rolling_again=="n":
        break

   
