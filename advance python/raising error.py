def increament(num):

    try:
        return num+1
        
    except:
        raise ValueError("Please enter valid input")

a=increament(34)
print(a)