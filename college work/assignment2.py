a=int(input("enter the numer of student:- "))

mix_list=[]
for i in range (0,a):
    b=input("enter the marks of data structure subject :- ")
    if b.isdigit():
        mix_list.append(int(b))  # Convert to integer if it's a digit
    else:
        mix_list.append(b)
        
print("marks and absent student", mix_list)

int_list=[]
for item in mix_list:
    if isinstance(item, int):
        int_list.append(item)
print(int_list)

sum=0
for j in int_list:
    sum=sum+j
print(sum)

aveg=sum/a
print(f"The aveg marks is {aveg}")
print("maximum marks",max(int_list))
print("minimum marks",min(int_list))
count=0
for value in mix_list:
    if value=='a':
        count+=1
print("The no of student where absent for test are:-",count)