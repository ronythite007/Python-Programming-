
#finally keyword allways exucuted even after function is exucuted
def fun():    
    try:
        l=[5,6,7,8,9]
        num=int(input("enter the number:- "))
        print(l[num])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
            print("I am allways axucuted")
x=fun()
print(x)