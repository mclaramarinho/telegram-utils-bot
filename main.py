##libraries
import os
from img_to_text import img_to_text
from keep_alive_background import keep_alive

from remove_bg import remove_bg

import requests
import telebot

##locals
from qr_code import qr_code
from shorten import shorten
from text_content import ABOUT_TEXT, CONTACT_TEXT, HELP_TEXT
from translate import translate
from sumup_text import sumup_text
from toPDF import toPDF

BOT_TOKEN = os.getenv("BOT_API_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(
      message.chat.id,
      "Hello! I'm a bot that can help you with your daily needs. Type /help to see the available features."
  )


@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(commands=['about'])
def about(message):
  bot.send_message(message.chat.id, ABOUT_TEXT)


@bot.message_handler(commands=['contact'])
def contact(message):
  bot.send_message(message.chat.id, CONTACT_TEXT)


@bot.message_handler(commands=['url'])
def shorten_url(message):
  url = message.text[5:len(message.text)]
  if len(url) != 0:
    short = shorten(url)
    bot.send_message(message.chat.id, short)
  else:
    bot.send_message(
        message.chat.id,
        "Please enter a valid URL.\nExample:\n/url https://example.com")


@bot.message_handler(commands=['qr'])
def qr(message):
  url = message.text[4:len(message.text)]
  if len(url) != 0:
    code = qr_code(url)
    bot.send_photo(message.chat.id, code)
  else:
    bot.send_message(
        message.chat.id,
        "Please enter a valid URL.\nExample:\n/qr https://www.example.com")


@bot.message_handler(commands=['count'])
def count(message):
  text = message.text[7:len(message.text)]
  if len(text) != 0:
    count = len(text)
    one_line_response = f"""The text sent has {count} characters, including spaces"""
    bot.send_message(message.chat.id, count)
  else:
    bot.send_message(message.chat.id,
                     "Please enter a text. \nExample:\n/count Hello World")


## HANDLE FILES SENT
@bot.message_handler(content_types=['document'])
def file_handling(message):
  ## REMOVE BACKGROUND COMMAND
  if (message.caption == '/rembg'):
    file_id = message.document.file_id
    file_path = bot.get_file(file_id).file_path

    if ('.jpg' in file_path) or ('.png' in file_path) or ('.jpeg'
                                                          in file_path):

      remove = remove_bg(file_path)
      OUTPUT_PATH = f'no-bg{file_path[10:len(file_path)]}.png'
      if remove == True:
        bot.send_photo(message.chat.id, open(OUTPUT_PATH, 'rb'))
      else:
        bot.send_message(message.chat.id,
                         'Sorry, I couldn\'t remove the background.')

    else:
      bot.send_message(
          message.chat.id,
          'Sorry, I can only remove background from .jpg, .png and .jpeg files.'
      )
    os.remove(file_path[10:len(file_path)])

  ## CONVERT TO PDF COMMAND
  elif (message.caption == '/convert'):
    file_id = message.document.file_id
    file_path = bot.get_file(file_id).file_path

    if ('.docx' in file_path) or ('.doc' in file_path) or (
        '.ppt' in file_path) or ('.pptx' in file_path) or ('.xlsx'
                                                           in file_path):
      convertion = toPDF(file_path=file_path)
      if convertion is True:
        OUTPUT_PATH = f'converted-{file_path[10:len(file_path)]}.pdf'
        send_document = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument?'
        data = {
            'chat_id': message.chat.id,
            'parse_mode': 'HTML',
            'caption': 'Here\'s the file you requested.'
        }

        r = requests.post(send_document,
                          data=data,
                          files={'document': open(OUTPUT_PATH, 'rb')},
                          stream=True)
        os.remove(OUTPUT_PATH)
      else:
        bot.send_message(message.chat.id,
                         'Sorry, I couldn\'t convert the file.')
    elif ('.pdf' in file_path):
      bot.send_message(
          message.chat.id,
          'Hmm... It seems that the file is already in PDF format.')
    else:
      bot.send_message(
          message.chat.id,
          'Sorry, I can only convert .docx, .doc, .ppt, .pptx, .xlsx files.')
    os.remove(file_path[10:len(file_path)])

  ## OCR COMMAND
  elif (message.caption == '/ocr'):
    file_id = message.document.file_id
    file_path = bot.get_file(file_id).file_path

    if ('.jpg' in file_path) or ('.png' in file_path) or ('.jpeg'
                                                          in file_path):
      response = img_to_text(file_path)
      if response == False:
        bot.send_message(message.chat.id,
                         'Sorry, I couldn\'t recognize the text.')
      else:
        bot.send_message(message.chat.id, response)

    else:
      bot.send_message(message.chat.id,
                       'Sorry, I can only read .jpg, .png and .jpeg files.')
    os.remove(file_path[10:len(file_path)])


@bot.message_handler(commands=['sumup'])
def sumup(message):
  text = message.text[6:len(message.text)]
  response = sumup_text(text)
  one_line_response = f"""
  Here\'s the summed up version of the text sent:
  {response}
  """
  bot.send_message(message.chat.id, one_line_response)


@bot.message_handler(commands=['translate'])
def handle_translate(message):
  lang = message.text[10:14]
  text = message.text[15:len(message.text)]
  text = translate(lang, text)
  bot.send_message(message.chat.id, f'Here\'s the translated text:\n {text}')


keep_alive()
bot.infinity_polling()
