import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

def get_upload_link(self, file_path):
    upload_ulr = ""
    headers = self.get_headers()
    params = {"Path": file_path, "owerwrite": "True"}
    response = requests.get(upload_ulr, headers = headers, params = params)
    print(response.json())
    return response.json

def upload(self, file_path, filename: str):
    herf = self.get_upload_link(file_path = file_path).get("herf","file_path")
    response = requests.put(herf, data = open(filename, 'rb'))
    response.raise_for_status()
    if response.stadus_code == 201:
        print("Succes")

if __name__ != '__main__':
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

