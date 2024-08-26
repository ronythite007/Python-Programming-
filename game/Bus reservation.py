from tabulate import tabulate as tb
import pandas as pd

print("                       *****WELCOME TO NEETA BUSES*****")
print("")
while True:
    print("""1.Install\n2.Resarvation\n3.Show\n4.Reserved Ticket\n5.Exit """)

    a=int(input("Enter your prefrance:-"))

    if a==3:
        print("none")
    if (a==1):
        bus_no=int(input("Enter The Bus No.       :- "))
        bus_time=int(input("Enter The Bus Timing (from) :- "))
        bus_time2=int(input("Enter The Bus Timing (To) :- "))
        bus_loca=input("Enter The Location        :- ")
    print("")
    dict={
        "Bus Name":[f"{bus_no}"],
        "Timing from": [f"{bus_time} Am"],
        "Timing To": [f"{bus_time} PM"],
        "Bus Location":[f"To {bus_loca}"]
    }

    df=pd.DataFrame(dict)

    print("")

    if (a==2):
        print("NOW RESERVE YOUR SEAT")
        while True:
            rsrv=int(input("Enter Your Bus No. :- "))
            if rsrv!=bus_no:
                print("Enter proper bus number")
            if rsrv==bus_no: 
                break
        print(tb(df, headers='keys', tablefmt='psql'))

        a=[]
        for i in range(18):
            value="empty"
            a.append(value)
        dt=pd.DataFrame(a,columns=["Seats"])
        
        print(tb(dt,headers='keys', tablefmt='psql'))
        print("")
        
        print("The Seats Are Available In Bus Are-18")
        reserved=input("Reserve you seat by your name :- ")
        seat=int(input(" enter seat number you want   :- "))
        date=input("Enter Date of reservation         :- ")
        dt.loc[seat,"Seats"]=reserved
        
        print(tb(dt,headers='keys', tablefmt='psql'))
        print("")

    if a==3:
        print(tb(df, headers='keys', tablefmt='psql'))
        print("")
    if a==4:
        print(f"""Dear [{reserved}],

Your seat is reserved in NEETA BUSES seat no.[{seat}] as name [{reserved}] 
on your bus from [{bus_loca} ] to [Destination City] on [{date}] at [{bus_time}]. 
Please be on time and bring this letter.

Thanks,
[NEETA BUSES]""")
    print("")    
    
    if a==5:
        break

    
