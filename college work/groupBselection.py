import random
#bubble Search

list=[random.randint(35,100) for x in range(1,7)]
#before sorted
print(list)

for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[j]<list[i]:
            temp=list[j]
            list[j]=list[i]
            list[i]=temp
#sorted list
print(list)

list1=[]
for i in range(-5,0):
    list1.append(list[i])
print(list1)
list1.reverse()
print("Top 5 Students Marks")
print(list1)