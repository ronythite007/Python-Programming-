import random

lower="abcdefhijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
special="@#$&*_."

string=lower+upper+numbers+special

length=int(input("enter the length of the password:-"))

password= "".join(random.sample(string,length))
print(f"yopur password is:-{password}")

