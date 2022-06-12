import requests
filename = "audio4.aac"
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': "e23fa0bfa3f047758b48d48d9c0ca34e"}
response = requests.post('https://api.assemblyai.com/v2/upload',headers=headers,data=read_file(filename))

print(response.json())
