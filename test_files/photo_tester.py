#photo tester file
import requests

#fetch new image from lorem picsum
for i in range(1, 11):
    filename = './testpic{id}.jpg'.format(id=i)
    request = requests.get("https://picsum.photos/800", stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for c in request:
                image.write(c)
    else:
        print("Unable to download image, using previous cached image")
