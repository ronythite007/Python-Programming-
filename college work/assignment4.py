#linear search 
#it checks the all elements of the list one by one
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n=int(input("enter the number to search :-"))
flag=0
for i in range(0,len(l)):
    if n ==l[i]:
        flag=i
        break

if flag==0:
    print("number not found")
else:
    print("the number is at",flag+1,"location")