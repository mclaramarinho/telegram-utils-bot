import os
import requests

from save_file_from_tg import save_file_from_tg

REMBG_TOKEN = os.getenv("REMOVE_BG_API_TOKEN")


def remove_bg(file_path):
  INPUT_PATH = file_path[10:len(file_path)]
  OUTPUT_PATH = f'no-bg{INPUT_PATH}.png'
  save = save_file_from_tg(file_path)

  if save == True:
    res = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(INPUT_PATH, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': f'{REMBG_TOKEN}'},
    )
    if res.status_code == 200:
      with open(OUTPUT_PATH, 'wb') as f:
        f.write(res.content)
        return True
    else:
      return False
  else:
    return False
