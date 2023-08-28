import sys

import requests

if len(sys.argv) != 2:
    print("Usage: pdm test/post.py <name>")
    sys.exit(1)


# The URL you want to send the POST request to
url = "http://localhost:8000/items/"
# The data you want to send in the POST request (as a dictionary)
data = {"name": f"item_post_route_{sys.argv[1]}"}

# Make the POST request
response = requests.post(url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Request successful!")
    print("Response content:", response.text)
else:
    print("Request failed. Status code:", response.status_code)
