import requests
#state of request
#https://app.assemblyai.com/processing-queue
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "https://cdn.assemblyai.com/upload/ad55b3a4-e896-4a3f-8cae-88fedbf770f3",
    "language_code": "es"
}
headers = {
    "authorization": "e23fa0bfa3f047758b48d48d9c0ca34e",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())
