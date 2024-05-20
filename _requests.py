import requests

r = requests.get('https://api.restful-api.dev/objects', headers={'Accept': 'application/json'})

print(f"Status Code: {r.status_code}, Content: {r.json()}")
