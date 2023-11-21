import requests
import os
import json
from save_file_from_tg import save_file_from_tg

OCR_TOKEN = os.getenv("FREE_OCR_API_TOKEN")


def img_to_text(img_path):
  INPUT_PATH = img_path[10:len(img_path)]
  save = save_file_from_tg(file_path=img_path)
  if save == True:
    payload = {
        'isOverlayRequired': False,
        'apikey': OCR_TOKEN,
        'language': 'eng'
    }
    r = requests.post(
        'https://api.ocr.space/parse/image',
        files={INPUT_PATH: open(INPUT_PATH, 'rb')},
        data=payload,
    )
    decoded = r.content.decode()
    decoded = json.loads(decoded)
    result = decoded.get('ParsedResults')[0].get('ParsedText')
    return result
  else:
    return False
