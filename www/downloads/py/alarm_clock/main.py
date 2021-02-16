from datetime import date
from time import strftime, strptime
import win32api
import time
import schedule
import threading

ENDCMD = "END"
wakeUpTime = "7:20"
beep_time = "20"
freqency = "1300"

def beep_func():
    print("beep")
    win32api.Beep(int(freqency), (int(beep_time)*1000))

def done():
    print("exited")
    exit()

def alarm_clock(wake_up_time):
    schedule.every().day.at(wake_up_time).do(beep_func)

    while True:
        schedule.run_pending()
        time.sleep(1)

def listen():

    while True:
        cmd = input("Here : ")

        if cmd == ENDCMD:
            done()


thL = threading.Thread(target=listen)
thAlarm = threading.Thread(target=alarm_clock, args=(wakeUpTime,))

beep_func()
# print("Starting listening thread!")
# thL.start()

# print("Starting alarm clock thread")
# thAlarm.start()
