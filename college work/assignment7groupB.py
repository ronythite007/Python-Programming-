student=[]
no_of_students=int(input("Enter the no.of students roll.no to be store:-"))
for i in range (1,no_of_students):
    a=int(input(f"{i}]Enter the Roll nos. :- "))
    student.append(a)
print(student)
student.sort()

print("The sorted list of student")
print(student)
search=int(input("Enter the roll no. to be search :-"))
first=0
last=len(student)-1

while first<=last:

    mid=(first+last)//2
    if search == student[mid]:
        print("The student has attende the training program")
        break

    if search < student[mid]:
        last= mid-1

    else :
        first= mid+1

if first>last:
    print("The student did't attain the traning progaram")