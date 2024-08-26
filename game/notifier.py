import schedule
import time 
from plyer import notification

def info():
    notification.notify(
    title="Hi",
    message="Work Hard succses is waiting",
    timeout=10
   )

schedule.every().day.at(":h").do(info)

while True:
    schedule.run_pending()
    time.sleep(5)