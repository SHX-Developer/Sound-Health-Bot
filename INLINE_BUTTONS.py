from telebot import types

class Inline_Buttons:


    reg_language_inline = types.InlineKeyboardMarkup(row_width=2)
    reg_uzbek_language = types.InlineKeyboardButton(text="🇺🇿  O'zbekcha", callback_data="reg_uzbek_language")
    reg_russian_language = types.InlineKeyboardButton(text="🇷🇺  Русский", callback_data="reg_russian_language")
    reg_language_inline.add(reg_uzbek_language, reg_russian_language)


    language_inline = types.InlineKeyboardMarkup(row_width=2)
    uzbek_language = types.InlineKeyboardButton(text="🇺🇿  O'zbekcha", callback_data="uzbek_language")
    russian_language = types.InlineKeyboardButton(text="🇷🇺  Русский", callback_data="russian_language")
    language_inline.add(uzbek_language, russian_language)