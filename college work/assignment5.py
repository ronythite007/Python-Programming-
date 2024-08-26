"""binary search is define as seraching algorithm used in a stored array by
repeatedly dividing the search internal in  half the list is to be stored"""

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n=int(input("enter the number to search :-"))

first=0
last=len(l)-1

while first<=last:
    mid=(first+last)//2
    if n==mid:
        print("The number is in",mid,"location")
        break
    
    if n<mid:
        last=mid-1

    else:
        first=mid+1    

if first>last:
    print("The number is not found")