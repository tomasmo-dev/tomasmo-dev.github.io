import time
import pyautogui

TimeRn = None

target_x = 960
target_y = 1004

played = False

target_time = {"Hour":23, "Min":58, "Sec":58}

def clickPlay():
    time.sleep(0.45)
    pyautogui.click(x=target_x, y=target_y)


while played == False:
    TimeRn = time.localtime(time.time())

    if TimeRn.tm_hour == target_time["Hour"] and TimeRn.tm_min == target_time["Min"] and TimeRn.tm_sec == target_time["Sec"] and played == False:
        clickPlay()
        played = True


print("New year!")