import pyautogui as py
import webbrowser as wb
import time

wb.open("web.whatsaap.com")
time.sleep(20)
for i in range(20):
    py.press("h")
    py.press("i")
    py.press("enter")
