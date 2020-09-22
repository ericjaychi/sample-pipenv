import requests

response = requests.get("http://date.jsontest.com")

print("Today's date is " + response.json()["date"])
