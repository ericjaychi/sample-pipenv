# Import the package we installed in our Pipfile.
import requests

# Grabbing the JSON from a test API.
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Print the date to confirm if it worked or not.
print(response.json())
