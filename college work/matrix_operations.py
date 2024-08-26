# matrix addtion
print("addition of matrix")
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[7,76,9],[4,5,23],[17,9,22]]
c=[]

for i in range(len(a)):
    row=[]
    for j in range(len(b)):
        row.append(0)
    c.append(row)

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=(a[i][j]+b[i][j])
for r in c:
    print(r)
print("")

# matrix substraction0
print("substrction of matrix")
a=[[12,90,3],[48,5,60],[47,88,29]]
b=[[7,76,9],[4,5,23],[17,9,22]]
c=[]

for i in range(len(a)):
    row=[]
    for j in range(len(b)):
        row.append(0)
    c.append(row)

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=(a[i][j]-b[i][j])
for k in c:
    print(k)

print(" ")
#matrix multiplication
print("Multiplication of matrix")
a=[[2,9,3],[8,5,6],[4,8,9]]
b=[[7,6,9],[4,5,2],[1,9,2]]
c=[]

for i in range(len(a)):
    row=[]
    for j in range(len(b)):
        row.append(0)
    c.append(row)

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]=a[i][k]*b[k][j]

for s in c:
    print(s)

a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
print()

print("transpose matrix")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[j][i],end=" ")
    print()