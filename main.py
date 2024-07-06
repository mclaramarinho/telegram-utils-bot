from dotenv import load_dotenv
from keep_alive_background import keep_alive

load_dotenv()


from subflows import url_shortener_flow, start_flow


from subflows import url_shortener, rem_bg, to_pdf



from bot import bot
keep_alive()
bot.infinity_polling()
