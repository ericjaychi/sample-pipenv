# Import the package we installed in our Pipfile.
import requests

# Grabbing the JSON from a test API.
response = requests.get("http://date.jsontest.com")

# Print the date to confirm if it worked or not.
print("Today's date is " + response.json()["date"])
