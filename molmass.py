import requests
import json

# Define the URL and headers
url = "http://ec2-3-145-132-103.us-east-2.compute.amazonaws.com/run"
headers = {
    "accept": "*/*",
    "Content-Type": "application/json"
}

# Define the data to be sent in the POST request
data = [
    {"input": "CC(=O)OC1=CC=CC=C1C(=O)O"}
]

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
