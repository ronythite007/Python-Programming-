no_of_student=int(input("Enter the number student you want to add :-"))
list=[]
for i in range (no_of_student):
    student={}
    name=input(f"Enter the name of student {i}: ")
    phone=input(f"Enter the phone of student {i} : ")
    student["name"]=name
    student["phone"]=phone

    list.append(student)
print(list)
sorted_list = sorted(list, key=lambda x: x['name'])
print(sorted_list)

# searching the name is present or not
search=input("Enter the  Name to search : ")
first=0
last=len(sorted_list)-1
while first<=last:
    mid=(first+last)//2

    if search==sorted_list[mid]["name"]:
        print("This person is present")
        break

    if search<sorted_list[mid]["name"]:
        last=mid-1

    if search>sorted_list[mid]["name"]:
        first=mid+1

if first <last:
    print("This person is not present ")
  
for i in range(len(sorted_list)):

    if search!=sorted_list[i]:
        student1={}
        name=input(f"Enter the name of student : ")
        phone=input(f"Enter the roll no. of student : ")
        student1["name"]=name
        student1["phone"]=phone
        sorted_list.append(student1)
        break
print(sorted_list)


