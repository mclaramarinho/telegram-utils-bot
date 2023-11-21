import requests
import json
import os

BOT_TOKEN = os.getenv("BOT_API_TOKEN")


def save_file_from_tg(file_path):
  INPUT_PATH = file_path[10:len(file_path)]
  res = requests.get(
      f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}")

  if (res.status_code == 200):
    open(INPUT_PATH, 'wb').write(res.content)
    return True
  else:
    return False
