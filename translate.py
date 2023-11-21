import os
import requests
import openai

openai.api_key = os.getenv("OPEN_AI_API_TOKEN")


def get_lang(lang):
  if lang == '-en':
    lang = 'english'

  elif lang == '-fr':
    lang = 'french'

  elif lang == '-es':
    lang = 'spanish'

  elif lang == '-de':
    lang = 'german'

  elif lang == '-it':
    lang = 'italian'

  elif lang == '-ru':
    lang = 'russian'

  elif lang == '-pl':
    lang = 'polish'

  elif lang == '-nl':
    lang = 'dutch'

  elif lang == '-pt':
    lang = 'portuguese'

  elif lang == '-sv':
    lang = 'swedish'

  elif lang == '-tr':
    lang = 'turkish'

  elif lang == '-uk':
    lang = 'ukrainian'

  elif lang == '-vi':
    lang = 'vietnamese'

  return lang


def translate(lang, text):
  language = get_lang(lang)
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role":
              "system",
              "content":
              f"Your role is to translate to {language} the text sent by the user"
          },
          {
              "role": "user",
              "content": text
          },
      ])
  return response["choices"][0]["message"]["content"]
