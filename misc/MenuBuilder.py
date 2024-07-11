import string
from typing import List

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class MenuOption:
    text_content: string
    callback_data: string
    active: bool

    def __init__(self, text_content: string, callback_data: string, active: bool = True):
        self.callback_data = callback_data
        self.text_content = text_content
        self.active = active


class MenuBuilder:
    _options: List[MenuOption]
    _menu: InlineKeyboardMarkup
    _row_width: int

    @property
    def menu(self):
        return self._menu

    @property
    def row_width (self):
        return self._row_width

    @property
    def options (self):
        return self._options

    def __init__(self, options: List[MenuOption], row_width: int = 1):
        self._options = options
        self._row_width = row_width

        self._menu = InlineKeyboardMarkup()
        self._menu.row_width = self.row_width

        self._generate_menu()

    def _generate_menu(self):
        for option in self._options:
            if option.active:
                temp_opt = InlineKeyboardButton(text=option.text_content, callback_data=option.callback_data)
                self._menu.add(temp_opt)
