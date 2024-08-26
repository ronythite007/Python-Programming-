f=open("sample.txt","r")
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} is in maths {m1}")
    print(f"Marks of student {i} is in physics {m2}")
    print(f"Marks of student {i} is in sst {m3}")

f.close()