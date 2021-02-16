import time
from requests import get
from win10toast import ToastNotifier
from PIL import Image


running = True
toaster = ToastNotifier() #creates instance

while True:

    current_day = time.localtime(time.time())

    if current_day.tm_hour == 12 and running == True:   #Checks time

        running = False

        def check_for_pic():

            tm = time.localtime(time.time())    #Current time

            time_y = tm.tm_year
            time_mon = tm.tm_mon
            time_day = tm.tm_mday

            key = "DEMO_KEY"   #Api Key
                
            lon = 15.8 #Lontitude
            lat = 50.0 #Latitude
            dim = 0.5   #Zoom level

            url = "https://api.nasa.gov/planetary/earth/imagery?date={0}-{1}-{2}".format(time_y, time_mon, time_day)    #API url
            parameters = dict(lon = lon, lat = lat, dim = dim, key = key)   #parameters for api

            response = get(url, params=parameters).json() #gets response

            try:

                print(response["msg"]) #checks for a photo

            except:

                folder = open("C:\\IMG.png", "wb")
                folder.write(response.content)                 #Saves the photo
                folder.close()

                toaster.show_toast(title="Image", msg="Current Satellite Image Available!", duration=10, icon_path="sat_img.ico")   #makes notifications
                
                try:
                    img = Image.open("C:\\IMG.png") #Opens the picture for the user
                    img.show()
                    
                except IOError:
                    pass

        running = True

        check_for_pic()  
  
    time.sleep(1800)    #waits 1800 seconds
