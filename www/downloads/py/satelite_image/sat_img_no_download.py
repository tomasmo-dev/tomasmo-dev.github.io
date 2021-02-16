import datetime
from time import sleep
import requests
import json
import os

image_list = []

cur_date = datetime.datetime.now()

params = json.loads(open("school\\data.json").read())

start_d = datetime.date(2020, 1, 1)
end_d = datetime.date(cur_date.year, cur_date.month, cur_date.day)
delta = datetime.timedelta(days=1)

# while start_d <= end_d:
#     print(start_d)
#     start_d += delta
while start_d <= end_d:

    test_day = f"{start_d.year}-{start_d.month}-{start_d.day}"

    data = dict(lon = params["lon"], lat = params["lat"], dim = params["dim"], api_key = params["API_KEY"], date = test_day)

    response = requests.get(params["url"], params=data)
    
    try:
        image_list.append(response.content)
        print("img detected")
        print(response.content)

    except Exception as e:
        print(f"{start_d.year}-{start_d.month}-{start_d.day} - No image")
        print(response)
    #
    #
    sleep(0.5)
    start_d += delta
print(image_list)