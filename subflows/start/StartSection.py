import string
from typing import List

from telebot.types import InlineKeyboardMarkup

from bot import Session
from misc.MenuBuilder import MenuOption, MenuBuilder


class StartSection:
    _startMessage: string
    _menu_options: List[MenuOption] = [
        MenuOption(text_content="Remove Background", callback_data="rem_bg"),
        MenuOption(text_content="Shorten URL", callback_data="shorten_url"),
        MenuOption(text_content="Convert to PDF", callback_data="to_pdf"),
        MenuOption(text_content="About Me", callback_data="about"),
    ]
    _menu: InlineKeyboardMarkup

    def _set_start_message(self, username: string):
        self._startMessage = f"Hello, {username}! How can I help you today?"

    @property
    def start_message(self):
        return self._startMessage

    @property
    def menu(self):
        return self._menu

    def __init__(self, username: string):
        self._set_start_message(username=username)
        self._menu = MenuBuilder(options=self._menu_options).menu
