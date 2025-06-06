import requests
import json

endpoint = 'https://www.google.com'
api_key = 'abc'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "prompt": "Hello, Azure OpenAI!",
    "prompt": "Please explain GenAI and Agentic AI in plain English",
    "max_tokens": 50
}

response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)

