"""truncate() function is use to 
write only passed argument characters"""

f=open("sample.txt","w")
data=f.write("hellow world")
f.truncate(5)

f.close()