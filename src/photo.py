import requests

def fetch_photo(cls):
    #fetch new image from lorem picsum
    filename = '../imagecache/todayspic.jpg'
    request = requests.get("https://picsum.photos/800", stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for c in request:
                image.write(c)
    else:
        print("Unable to download image, using previous cached image")
