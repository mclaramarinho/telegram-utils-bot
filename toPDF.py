import requests
import json
import os

from save_file_from_tg import save_file_from_tg

BOT_TOKEN = os.getenv("BOT_API_TOKEN")


def toPDF(file_path):
  INPUT_PATH = file_path[10:len(file_path)]
  OUTPUT_PATH = f'converted-{INPUT_PATH}.pdf'
  save_file = save_file_from_tg(file_path)
  
  if save_file == True:
    instructions = {'parts': [{'file': 'document'}]}
    reqPDF = requests.post(
        'https://api.pspdfkit.com/build',
        headers={
            'Authorization':
            'Bearer pdf_live_84A62KSuJUl9iCyelUkxr0kSRgNEhQ8S18Vlj5Rlxwf'
        },
        files={'document': open(INPUT_PATH, 'rb')},
        data={'instructions': json.dumps(instructions)},
        stream=True)
    if reqPDF.status_code == 200:
      with open(OUTPUT_PATH, 'wb') as f:
        for chunk in reqPDF.iter_content(chunk_size=1024):
          if chunk:
            f.write(chunk)
      return True
    else:
      return False
  else:
    return False
