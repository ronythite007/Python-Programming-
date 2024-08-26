import random
    
def game(comp,you):
    if comp==you:
        return None
    if comp=="s":
        if you=="w":
            return False
        if you=="g":
            return True
    if comp=="w":
        if you=="s":
            return True
        if you=="g":
            return False
    if comp=="g":
        if you=="w":
            return True
        if you=="s":
            return False      

print("comp turn:snake(s),water(w),Gun(g)?")
print("your turn:snake(s),water(w),Gun(g)?")
print("if you wanr to end game type 0")
a=random.randint(1,3)
if a==1:
    comp="s"
if a==2:
    comp="w"
if a==3:
    comp="g"

while True:
    you=input("your turn:snake(s),water(w),Gun(g):")

    if you=="0":
        break

    b=game(comp,you)

    print(f"comp choosen:{comp}")
    print(f"you choosen:{you}")

    if b==None:
        print("tai")
    if b== False:
        print("\"comp\" won the match")
    if b== True:
        print("\"you\" won the match")
    
    print("*"*20)