from telebot.types import Message

from bot import Session, bot
from subflows.start.StartSection import StartSection

session = Session()


def is_in_start_section():
    return session is None or session.step == 0


@bot.message_handler(func=lambda message: is_in_start_section())
def greeting(message: Message):
    global session
    session.set_user(message.chat)
    send_greeting()


def send_greeting():
    start_section = StartSection(session.username)
    bot.send_message(chat_id=session.uid, text=start_section.start_message, reply_markup=start_section.menu)

