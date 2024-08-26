
def add(a):
    def greet():
        print ("hellow rohan")
    a()
    print("i am the richest person")
    return greet
@add
def hellow():
        print("hi guys")  


hellow()





import random

a=random.randint(1,10)
print(a)