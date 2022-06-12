import requests
import json

transcript = "oqn28tnz56-6bed-402d-8d59-b94dd7b181c5"
endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript}"
headers = {
    "authorization": "e23fa0bfa3f047758b48d48d9c0ca34e",
}
response = requests.get(endpoint, headers=headers)
#print(response.json())
print(response.json()['text'])
f = open("data.txt","w")
f.write(response.json()['text'])
f.close()
