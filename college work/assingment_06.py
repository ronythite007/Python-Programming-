list_A=[]
terms=int(input("Enter the entries to add :-"))

for i in range(1,terms+1):
    s={}
    prn=int(input("Enter the PRN :-"))
    date=int(input("Enter the date :-"))
    month=int(input("Enter the month of birth :-"))
    s["PRN"]=prn
    s["Date"]=date
    s["Month of birth"]=month
    list_A.append(s)

print(list_A)
print(" ")

list_B=[]
terms=int(input("Enter the entries to add :-"))

for i in range(1,terms+1):
    k={}
    prn=int(input("Enter the PRN :-"))
    date=int(input("Enter the date :-"))
    month=int(input("Enter the month of birth :-"))
    k["PRN"]=prn
    k["Date"]=date
    k["Month of birth"]=month
    list_B.append(k)

print(list_B)

list_SE_COMP=list_A+list_B

print(list_SE_COMP)
# sorrted list on the basis of the date of birth 
sorted=sorted(list_SE_COMP ,key=lambda n:n["Month of birth"] )
print(sorted)