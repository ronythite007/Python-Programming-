import random
#bubble Search

list=[random.randint(35,99) for x in range(1,67)]
#before sorted
print(list)

for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
#sorted list
print(list)

list1=[]
for i in range(-5,0):
    list1.append(list[i])
print(list1)
list1.reverse()
print("Top 5 Students Marks")
print(list1)