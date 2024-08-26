#Group A Q4
list=[]
a=int(input("Enter the no of books to add : "))
for i in range(1,a):
    s={}
    name=input("Enter the name of Book :")
    cost=int(input("Enter th cost of the book : "))
    s["name"]=name
    s["cost"]=cost
    list.append(s)
print(list)
# deleting duplicate entries
list_without_duplicate=[]
for i in list:
    if i not in list_without_duplicate:
        list_without_duplicate.append(i)
print(list_without_duplicate)

count=0
cheap=0
cheap_book=[]
for i in list_without_duplicate:
    if i["cost"]>500:
        count+=1
    if i["cost"]<500:
        cheap+=1
        cheap_book.append(i["name"])
print(f"The book having cost greater than 500 are {count}")
print(f"The books having cost less than 500 are {cheap}")
print(cheap_book)

