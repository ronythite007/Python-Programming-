import random as rand
football=[]
print("Number of students playing football")
for i in range (1,30):
    a = rand.randint(1,67)
    while a in football:
        a = rand.randint(1,67)     
    
    football.append(a)  
print(football)

import random as rand
badmenton=[]
print("Number of students playing badmenton")
for i in range (1,25):
    a = rand.randint(1,67)
    while a in badmenton:
        a = rand.randint(1,67)     
    
    badmenton.append(a)  
print(badmenton)

import random as rand
cricket=[]
print("Number of students playing cricket")
for i in range (1,45):
    a = rand.randint(1,67)
    while a in cricket:
        a = rand.randint(1,67)     
    
    cricket.append(a)  
print(cricket)
#same using loop
print("\n")
list=[]          
for i in football:
    if i in badmenton:
        list.append(i)
print("\n")
print("Q1")
print("play both football and badmenton",list)
list2=[]
for s in badmenton:
    if s not in cricket:
        list2.append(s)
print("\n")
print("Q2")
print("The student play only cirket and badmenton",list2)
list3=[]
for k in football:
    if k not in cricket:
        if k not in badmenton:
            list3.append(k)
print("\n")
print("Q3")
print("The who palyneither cricket nor badmenton",list3)
list4=[]
for ckt in football:
    if ckt in cricket:
        if ckt not in badmenton:
            list4.append(ckt)
print("\n")
print("Q4")
print("The student cricket and football but not badmenton",list4)