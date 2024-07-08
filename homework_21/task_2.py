# https://rapidapi.com/collection/list-of-free-apis - берёте любую api и пробуете обращаться к endpoint-ам для
# получения ответа, чем больше сделаете запросов, тем лучше
import requests

url = 'https://covid-19-data.p.rapidapi.com/country/code'
querystring = {"country": "usa","code": "us"}
headers = {
    'x-rapidapi-key': 'b468431d00mshf11ce665afaa453p1a191ejsn8061f65d86cd',
    'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
}
responce = requests.get(url, headers=headers, params=querystring)
print(responce.json())
