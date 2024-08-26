"""In Python, seek() function is used to change 
the position of the File Handle to a given specific position."""

with open("data.txt","r") as f:
    f.seek(10)

    data=f.read(6)
    print(data)