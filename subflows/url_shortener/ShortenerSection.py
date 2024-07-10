import string
from typing import List

from telebot.types import InlineKeyboardMarkup

from misc.MenuBuilder import MenuOption, MenuBuilder
from subflows.url_shortener import validate_url, shortener
from subflows.url_shortener.shortener import InvalidUrlException


# STEPS:
# 0 - Get URL
# 1 - Send short URL
# 2 - Ask if finished




class ShortenerSection:
    _step: int
    _prev: int
    _url: string
    _shortened_url: string

    _welcome_message: string = "Okay. Please send me the URL you want to shorten:"
    _error_message: string = "Hmm... This URL does not seem to be valid. Please verify and try again:"
    _response_message: string

    _end_menu: InlineKeyboardMarkup
    _end_menu_options: List[MenuOption] = [
        MenuOption(text_content="Shorten another URL", callback_data="shorten_again"),
        MenuOption(text_content="Back to main menu", callback_data="back_to_menu"),
    ]

    @property
    def end_menu(self):
        return self._end_menu if self.step == 1 else None

    @property
    def response_message(self):
        return self._response_message

    @property
    def welcome_message(self):
        return self._welcome_message

    @property
    def error_message(self):
        return self._error_message

    @property
    def short_url(self):
        return self._shortened_url

    @property
    def url(self):
        return self._url

    @property
    def step(self):
        return self._step

    @property
    def prev(self):
        return self._prev

    def __init__(self):
        self._step = 0
        self._prev = 0
        self._end_menu = MenuBuilder(self._end_menu_options).menu

    def shorten(self, url: string):
        try:
            is_valid = validate_url(url)
            if is_valid:
                self._url = url
                self._shortened_url = shortener(self._url)
                self._set_response_msg()
                self._prev = self._step
                self._step = 1
            else:
                raise InvalidUrlException()
        except Exception as ex:
            raise ex

    def _set_response_msg(self):
        self._response_message = f"Here is your shortened URL: {self.short_url}."

    def shorten_again(self):
        self._prev = self._step
        self._step = 0