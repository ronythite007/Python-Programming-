from tkinter import *
rohan_root=Tk()

rohan_root.geometry("5500x5500")
# using min and max for size of the interface
rohan_root.minsize(800,500)
rohan_root.maxsize(400,500)
#adding text
txt=Label(text="well come to Dhanashri Fabricators")
txt.pack()
# adding png image 
photo=PhotoImage(file="rohan_code.png")
rohan=Label(image=photo)
rohan.pack()

rohan_root.mainloop()
