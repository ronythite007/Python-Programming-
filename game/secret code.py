import random

msg=input("enter your message:-")
r1="srx"
r2="zvy"
coding=True
if coding:    
    if len(msg) >= 3:
        msg1=msg[1:]+msg[0]
        c=r1+msg1
        d=c+r2
        print(d)
    else:
        s=msg[1]+msg[0]
        print(s)
else:
    if len(msg) >= 3:
        msg1=msg[-1]+msg[1:-1]
        c=msg1[3:-2]
        d=c[-1]+c[0:-1]
        print(d)
    else:
        s=msg[0]+msg[1]
        print(s)      