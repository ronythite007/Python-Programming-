def addition():
    try:
        return int(input("enter the number:- "))+1    
    except:
        raise ValueError(" invalid syntax")

a=addition()
print(a)