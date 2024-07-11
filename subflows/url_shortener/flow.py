from telebot.types import CallbackQuery, Message

from bot import bot
from misc.backToMenu import back_to_menu
from subflows.start.flow import is_in_start_section, session, send_greeting
from subflows.url_shortener.ShortenerSection import ShortenerSection
from subflows.url_shortener.shortener import InvalidUrlException

shorten_section: ShortenerSection | None = None


def should_start_url_section(cb):
    return is_in_start_section() and cb.data == "shorten_url"


def is_waiting_url():
    return session.step == 2 and shorten_section.step == 0


def is_in_end_menu():
    return session.step == 2 and (shorten_section.step == 1 or shorten_section.step == 0)


@bot.callback_query_handler(func=lambda cb: should_start_url_section(cb))
def start_url_section(cb: CallbackQuery):
    global shorten_section
    session.change_step(cb.data)

    shorten_section = ShortenerSection()
    bot.send_message(chat_id=session.uid, text=shorten_section.welcome_message)


@bot.message_handler(func=lambda msg: is_waiting_url())
def receive_url(msg: Message):
    try:
        shorten_section.shorten(msg.text)
        bot.send_message(chat_id=session.uid, text=shorten_section.response_message,
                         reply_markup=shorten_section.end_menu)
    except InvalidUrlException as e:
        bot.send_message(chat_id=session.uid, text=shorten_section.error_message, reply_markup=back_to_menu)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=session.uid, text="An unexpected error occurred. Please try again later.",
                         reply_markup=back_to_menu)


@bot.callback_query_handler(func=lambda cb: is_in_end_menu())
def handle_shorten_url_end_menu(cb: CallbackQuery):
    if cb.data == "shorten_again":
        shorten_section.shorten_again()
        bot.send_message(chat_id=session.uid, text=shorten_section.welcome_message)
    elif cb.data == "back_to_menu":
        session.change_step("back_to_menu")
        send_greeting(cb.message)
