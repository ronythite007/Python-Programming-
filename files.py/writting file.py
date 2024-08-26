# for length of sentance
f = open ('sample.txt','r')
data=f.read()
data1=data.split()
count=0
for i in data1:
    print (i)
    length=len(i)
    count+=length
print(count)    

# for counting the letters

f = open ('sample.txt','r')
data=f.read()
data1=data.split()
count=0
for i in data1:
    print (i)
    count+=1
print(count)





