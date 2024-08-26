import os
if __name__ == "__main__":
    print("welcome to robospeaker made by rohan")
    x = input("enter your command:- ")
    command = f" say {x}"
    os.system(command)