# this will open the file and store
# in "file" variable
file = open("sample.txt","r")
data=file.read()
print(data)
file.close()

# writting a file
f=open("sample.txt","w")

with open("sample.txt","w"):
    f.write("Hellow Word")