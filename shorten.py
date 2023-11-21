import requests


def shorten(url):
  req_url = f"http://tinyurl.com/api-create.php?url={url}"
  response = requests.get(req_url)
  return response.text
