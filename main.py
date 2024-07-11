from dotenv import load_dotenv
load_dotenv()


from subflows import url_shortener_flow, start_flow


from subflows import url_shortener, rem_bg, to_pdf


from bot import bot
if __name__ == '__main__':
    bot.infinity_polling()