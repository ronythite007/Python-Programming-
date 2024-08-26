import pandas as pd
df=pd.DataFrame(columns=["Doctor Name","Education","Speciality","Availability Time","For Action Press Below Letters"])
df.loc[0]=["Dr. Peter Parker","MBBS MS","Surgeon","7:00 to 10:00","Press 'P'"]
df.loc[1]=["DR. joshi","MBBS MS","Surgeon","7:00 to 10:00","Press 'j'"]
df.loc[2]=["Dr. Kulkarni","MBBS MS","Baby specialist","9:00 to 12:00","Press 'k"]
df.loc[3]=["Dr. Shukla","MBBS MS","Women Specialist","7:00 to 10:00","Press 's'"]
print(df)
