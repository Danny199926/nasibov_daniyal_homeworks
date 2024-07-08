import requests

url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect'
headers = {
    'X-RapidAPI-Key': 'b468431d00mshf11ce665afaa453p1a191ejsn8061f65d86cd',
    'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
}
data = {
    'q': 'hello world'
}
responce = requests.post(url, headers=headers, data=data)
print(responce.json())