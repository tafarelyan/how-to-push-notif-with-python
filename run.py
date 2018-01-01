import json
import requests

url = 'https://api.pushbullet.com/v2/pushes'
headers = {
    'Access-Token': 'YOUR-API-TOKEN',
}

payload = {
    'type': 'note',
    'title': 'Hello World',
    'body': 'No content',
}

r = requests.post(url, headers=headers, json=payload)
print(json.dumps(r.json(), indent=2))
