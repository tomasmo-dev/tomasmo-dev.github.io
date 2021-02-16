import threading
import time
import serial

from pynput.keyboard import Key, Listener

lastData = None

ar = serial.Serial('COM3', 9600, timeout=0.1)

def on_press(ser):
     global lastData
     if lastData != 'S':
          lastData = 'S'

          ser.write(b'S')

def on_release(ser):
     global lastData
     if lastData != 'E':
          lastData = 'E'

          ser.write(b'E')

def Listen(instance):
     print("Listening serial")
     while True:
          data = ar.readline()

          if data:
               print(data.decode("ASCII"))


time.sleep(2)
listening = threading.Thread(target=Listen, args=(ar, ), daemon=True)
listening.start()

time.sleep(2)
print("Listening to keyboard")

with Listener(on_press=lambda press: on_press(ar), on_release=lambda _ : on_release(ar)) as listen:
     listen.join()
     
          

