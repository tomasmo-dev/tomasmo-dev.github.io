from requests import get

url = "https://api.nasa.gov/planetary/apod?hd=true&api_key=DEMO_KEY"

response = get(url).json()

print(response["url"])