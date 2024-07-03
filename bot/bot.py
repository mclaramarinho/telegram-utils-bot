import telebot
import os

BOT_TOKEN = os.environ["BOT_API_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)
