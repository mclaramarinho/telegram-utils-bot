from dotenv import load_dotenv
from keep_alive_background import keep_alive

load_dotenv()

import subflows.start.flow
from subflows import shorten_url, rem_bg, to_pdf, start



from bot import bot


keep_alive()
bot.infinity_polling()
