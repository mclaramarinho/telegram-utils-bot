import urllib.parse
import requests


def qr_code(url):
  url_encoded = urllib.parse.quote(url)
  request_url = f"https://api.qrserver.com/v1/create-qr-code/?data={url_encoded}&size=1000x1000"
  response = requests.get(request_url)
  return response.content
