account=[]
balance=0
print("-----------WELCOME TO BANK OF INDIA-----------")
print("\n")
while True:
    a=input("ENTER 'd' TO Deposite & 'w' to withdraw money & enter exit to exit : " )
    if (a=="d"):
        value=int(input("Enter the entries you want to add : "))
        for i in range(1,value+1):
            deposite=int(input("Enter the amount to deposite : "))
            account.append(deposite)
            balance+=deposite
        print(f"Current balance is {balance}")

    if (balance <= 0):
        print("Your account is empty you can't withdraw money" )   
        break
    
    if (a=="w"):
        rupee=int(input("Enter amount to withdraw : "))
        balance-=rupee
        
        print(f"Current balance is {balance}")    

    if (a=="exit"):
        print("THANK YOU FOR WISITING OUR ATM :) ")
        break