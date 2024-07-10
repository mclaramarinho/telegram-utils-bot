from telebot.types import InlineKeyboardMarkup

from misc.MenuBuilder import MenuOption, MenuBuilder

options = [MenuOption(text_content="Back to menu", callback_data="back_to_menu")]
back_to_menu: InlineKeyboardMarkup = MenuBuilder(options=options).menu
