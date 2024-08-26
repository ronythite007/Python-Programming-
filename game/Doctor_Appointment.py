import pandas as pd

while True:
    def info():
        print("******* WELCOME TO CITY HOSPITAL *******")
        print("FOR LOGIN PRESS (1)\nFOR RESSISTRATION PRESS (2)\nFOR EXIT PRESS (3)")  
    info()
    print("")

    a=int(input("ENTER THE VALID NUMBER  :-"))
    print("")
    if a==1:
        print("# Fill The Below Information #")
        print("")
        e=input("ENTER YOUR EMAIL ID   :-")
        P=input("CREATE YOUR PASSWORD  :-")
        while True:
            rp=input("RE ENTER PASSWORD  :-")
            if rp !=P:
                print("RENTER CORRECT PASSWORD")
            if rp ==P:
                break    
    
        print("")
        print("You have succsesfuly LOGINED. Please do resistration now")   
        print("")
    if a==2:
        print("# Fill Resistration Details #")
        print("")
        r1=str(input("ENTER YOUR NAME                     :-"))
        r2=str(input("ENTER YOUR BIRTHDATE dd/mm/yy   :-"))
        r3=int(input("ENTER PATIENT CONTACT NUMBER    :-"))
        
        while True:
            r4=input("ENTER YOUR PASSWORD          :-")
            if r4 !=P:
                print("please enter correct password")
            if r4==P:
                break
        print("")
        print("You have succsesfully completed resistration process")

        print("")
        print("To Proceed ")
        Procss=input("ENTER F :-").lower()
        print("")
        if (Procss=="f"):

            hospital_name="CITY HOSPITAL"
            print(hospital_name)
            print("                                    **DOCTOR SCHEDULE LIST **")
            df=pd.DataFrame(columns=["Doctor Name","Education","Speciality","Availability Time","For Action Press Below Letters"])
            df.loc[0]=["Dr. Peter Parker","MBBS MS","Surgeon","7:00 to 10:00","Press 'P'"]
            df.loc[1]=["DR. joshi","MBBS MS","Surgeon","7:00 to 10:00","Press 'j'"]
            df.loc[2]=["Dr. Kulkarni","MBBS MS","Baby specialist","9:00 to 12:00","Press 'k"]
            df.loc[3]=["Dr. Shukla","MBBS MS","Women Specialist","7:00 to 10:00","Press 's'"]
            print(df)
          
        arr1 = ['kulkarni','joshi','Peter parker','Shukla']
        arr2 = ['k','j','p','s'] 
        date=input("DATE OF APPOINTMENT(eg- 23 march) :-")
        userInput=input("enter you prefrance:- ").lower()
        for i in range(len(arr2)):
                if userInput == arr2[i]:
                    doctorName = arr1[i]
                    print("")
                    print("***HERE IS YOUR APPOINTMENT LETTER***")
                    print(f"""Dear{doctorName},

We would like to remind you of your upcoming appointment with {doctorName} at {hospital_name} on {date} at [Time]. Please arrive 10-15 minutes early to allow time for any necessary paperwork.

If you are unable to make this appointment, please let us know as soon as possible so that we can reschedule. If you have any questions or concerns, please don't hesitate to contact us.

We look forward to seeing you soon.

Sincerely,

Incharge
{hospital_name}""")
    print("")
    
    if a==3:
        break
    