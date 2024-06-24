import requests
import json

def upload(file_path):
  with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post("https://cold4.gofile.io/contents/uploadfile", files=files)
    response_json = json.loads(response.text)

    download_url = None
    if isinstance(response_json, dict):
      download_url = response_json.get("data", {}).get("downloadPage")
    elif isinstance(response_json, list):
      for item in response_json:
        if isinstance(item, dict):
          download_url = item.get("downloadPage")
          break

    return download_url