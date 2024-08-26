student=[]
no_of_students=int(input("Enter the no.of students roll.no to be store:-"))
for i in range (1,no_of_students):
    a=int(input(f"{i}]Enter the Roll nos. :- "))
    student.append(a)
print(student)

search=int(input("Enter the roll no. to be search :-"))
flag=0
for rol in range(0,len(student)):

    if search==student[rol]:
        flag=rol
        break

if flag==0:
    print("Student did't attend the training program")

else:
    print(f"He has attended the Training Program") 