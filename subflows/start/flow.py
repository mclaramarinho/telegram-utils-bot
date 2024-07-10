from telebot.types import Message, CallbackQuery

from bot import Session, bot
from subflows.start.StartSection import StartSection

session = Session()


def is_in_start_section():
    return session is None or session.step == 0


def check_if_session_undefined():
    return session.username is None and session.uid is None


@bot.message_handler(func=lambda message: is_in_start_section())
def greeting(message: Message):
    send_greeting(message)


@bot.callback_query_handler(func=lambda cb: check_if_session_undefined())
def handle_lazy_user(cb: CallbackQuery):
    send_greeting(cb.message)


def send_greeting(message: Message):
    global session
    session.set_user(message.chat)
    start_section = StartSection(session.username)
    bot.send_message(chat_id=session.uid, text=start_section.start_message, reply_markup=start_section.menu)
