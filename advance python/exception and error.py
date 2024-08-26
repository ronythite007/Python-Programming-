a=input("enter the number:- ")

print(f"multiplication table of{a}")
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
    print(e)
print("ende of the code")
