from tkinter import *
rohan_root=Tk()
rohan_root.title("DF")
#TODO:important Lable options
#text= add's text
#bd=background
#fg=foreground
#font=sets the font
#1- font("comicsans",19,"bold")
#2- font="comicsans 19 bold"
# padx= border in x axis
# pady= border in y axis
#relie= border styling-SUNKEN, RAISED, GROOVE, RIDGE
#borderwidth
rohan_root.geometry("5500x5500")
# using min and max for size of the interface
rohan_root.minsize(800,500)
rohan_root.maxsize(400,500)
#adding text

txt=Label(text="""well come to Dhanashri Fabricators
          """,bg="black",fg="white",
          font="comicsans 19 bold",padx=15,pady=15
          ,borderwidth=10,relief="sunken" 
        )
photo=PhotoImage(file="rohan_code.png")
rohan=Label(image=photo)
rohan.pack()         
          
txt.pack()
rohan_root.mainloop()
