import telebot


import CONFIG

from UZBEK_BUTTONS import Uzbek_Buttons
from RUSSIAN_BUTTONS import Russian_Buttons

from RUSSIAN_INLINE_BUTTONS import Russian_Inline_Buttons

bot = telebot.TeleBot(CONFIG.TOKEN)

class Callback:
    pass


@bot.callback_query_handler(func=lambda call: True)
def inline(call):

    if call.data == "reg_uzbek_language":
        bot.send_message(call.message.chat.id, "<b>"
                                               '"ООО ""<i>SOUND HEALTH</i>""  Sizni kutib oladi !'
                                               '\n\nKompaniyamiz yuqori sifatli materiallardan tibbiy va ortopedik mahsulotlar ishlab chiqaradi'
                                               '\n\nBiz mahsulotimiz sifatini 100% kafolatlaymiz !'
                                               "</b>", parse_mode='html', reply_markup=Uzbek_Buttons.MenuButton)

    if call.data == "reg_russian_language":
        bot.send_message(call.message.chat.id, "<b>"
                                               '"ООО ""<i>SOUND HEALTH</i>""  Приветствует вас !'
                                               '\n\nНаша компания производит медицинские и ортопедические изделия из  высококачественных  материалов'
                                               '\n\nМы гарантируем качество своего товара на 100% !'
                                               "</b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButton)

    if call.data == "uzbek_language":
        bot.send_message(call.message.chat.id, "<b>"
                                               "O'zbek tili tanlandi  ✅"
                                               "</b>", parse_mode='html', reply_markup=Uzbek_Buttons.MenuButton)

    if call.data == "russian_language":
        bot.send_message(call.message.chat.id, "<b>"
                                               "Выбран русский язык  ✅"
                                               "</b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButton)

    if call.data == "ru_product_1":
        with open("PHOTOS/Products/Product 1.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  68,770  UZS"
                                                        "\nРазмер (44 - 46)  -  68,770  UZS"
                                                        "\nРазмер (46 - 48)  -  68,770  UZS"
                                                        "\nРазмер (50 - 52)  -  68,770  UZS"
                                                        "\nРазмер (54 - 56)  -  68,770  UZS"
                                                        "\nРазмер (58 - 60)  -  68,770  UZS"
                                                        "\nРазмер (58 - 60)  -  68,770  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_2":
        with open("PHOTOS/Products/Product 2.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "(8 см - 1,5 м)  -  13,900  UZS"
                                                        "\n(8 см - 3 м)  -  16,900  UZS"
                                                        "\n(8 см - 4 м)  -  17,900  UZS"
                                                        "\n(8 см - 5 м)  -  20,900  UZS"
                                                        "\n(10 см - 1,5 м)  -  12,900  UZS"
                                                        "\n(10 см - 3 м)  -  15,900  UZS"
                                                        "\n(10 см - 4 м)  -  19,900  UZS"
                                                        "\n(10 см - 5 м)  -  23,900  UZS"
                                                        "\n(12 см - 1,5 м)  -  11,900  UZS"
                                                        "\n(12 см - 3 м)  -  20,900  UZS"
                                                        "\n(12 см - 4 м)  -  22,900  UZS"
                                                        "\n(12 см - 5 м)  -  23,900  UZS"
                                                        "\n(14 см - 1,5 м)  -  11,900  UZS"
                                                        "\n(14 см - 3 м)  -  20,900  UZS"
                                                        "\n(14 см - 4 м)  -  24,900  UZS"
                                                        "\n(14 см - 5 м)  -  28,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_3":
        with open("PHOTOS/Products/Product 3.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "(40 - 42)  -  26,500  UZS"
                                                        "\n(44 - 46)  -  26,500  UZS"
                                                        "\n(48 - 50)  -  26,500  UZS"
                                                        "\n(52 - 54)  -  26,500  UZS"
                                                        "\n(56 - 58)  -  26,500  UZS"
                                                        "\n(60 - 62)  -  26,500  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_4":
        with open("PHOTOS/Products/Product 4.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Лет (6 - 8)  -  24,500  UZS"
                                                        "\nЛет (9 - 11)  -  24,500  UZS"
                                                        "\nЛет (12 - 15)  -  24,500  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_5":
        with open("PHOTOS/Products/Product 5.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (37 - 40)  -  25,900  UZS"
                                                        "\nРазмер (41 - 44)  -  25,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_6":
        with open("PHOTOS/Products/Product 7.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Лет (6 - 8)  -  57,900  UZS"
                                                        "\nЛет (9 - 11)  -  57,900  UZS"
                                                        "\nЛет (12 - 15)  -  57,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_7":
        with open("PHOTOS/Products/Product 6.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  72,900  UZS"
                                                        "\nРазмер (44 - 46)  -  72,900  UZS"
                                                        "\nРазмер (48 - 50)  -  72,900  UZS"
                                                        "\nРазмер (52 - 54)  -  72,900  UZS"
                                                        "\nРазмер (56 - 58)  -  72,900  UZS"
                                                        "\nРазмер (60 - 62)  -  72,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_8":
        with open("PHOTOS/Products/Product 8.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42) (взрослая)  -  33,900  UZS"
                                                        "\nРазмер (44 - 46) (взрослая)  -  33,900  UZS"
                                                        "\nРазмер (48 - 50) (взрослая)  -  33,900  UZS"
                                                        "\nРазмер (52 - 54) (взрослая)  -  33,900  UZS"
                                                        "\nРазмер (56 - 58) (взрослая)  -  33,900  UZS"
                                                        "\nРазмер (60 - 62) (взрослая)  -  33,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_9":
        with open("PHOTOS/Products/Product 9.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  33,900  UZS"
                                                        "\nРазмер (44 - 46)  -  33,900  UZS"
                                                        "\nРазмер (48 - 50)  -  33,900  UZS"
                                                        "\nРазмер (52 - 54)  -  33,900  UZS"
                                                        "\nРазмер (56 - 58)  -  33,900  UZS"
                                                        "\nРазмер (60 - 62)  -  33,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_10":
        with open("PHOTOS/Products/Product 10.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Лет (6 - 8)  -  33,000  UZS"
                                                        "\nЛет (9 - 11)  -  33,000  UZS"
                                                        "\nЛет (12 - 15)  -  33,000  UZS"
                                                        "\nЛет (6 - 8) (летние)  -  28,000  UZS"
                                                        "\nЛет (9 - 11) (летние)  -  28,000  UZS"
                                                        "\nЛет (12 - 15) (летние)  -  28,000  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_11":
        with open("PHOTOS/Products/Product 11.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  45,500  UZS"
                                                        "\nРазмер (44 - 46)  -  45,500  UZS"
                                                        "\nРазмер (48 - 50)  -  45,500  UZS"
                                                        "\nРазмер (52 - 54)  -  45,500  UZS"
                                                        "\nРазмер (56 - 58)  -  45,500  UZS"
                                                        "\nРазмер (60 - 62)  -  45,500  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_12":
        with open("PHOTOS/Products/Product 12.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  50,900  UZS"
                                                        "\nРазмер (44 - 46)  -  50,900  UZS"
                                                        "\nРазмер (48 - 50)  -  50,900  UZS"
                                                        "\nРазмер (52 - 54)  -  50,900  UZS"
                                                        "\nРазмер (56 - 58)  -  50,900  UZS"
                                                        "\nРазмер (60 - 62)  -  50,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_13":
        with open("PHOTOS/Products/Product 13.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  28,900  UZS"
                                                        "\nРазмер (44 - 46)  -  28,900  UZS"
                                                        "\nРазмер (48 - 50)  -  28,900  UZS"
                                                        "\nРазмер (52 - 54)  -  28,900  UZS"
                                                        "\nРазмер (56 - 58)  -  28,900  UZS"
                                                        "\nРазмер (60 - 62)  -  28,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_14":
        with open("PHOTOS/Products/Product 14.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  54,900  UZS"
                                                        "\nРазмер (44 - 46)  -  54,900  UZS"
                                                        "\nРазмер (48 - 50)  -  54,900  UZS"
                                                        "\nРазмер (52 - 54)  -  54,900  UZS"
                                                        "\nРазмер (56 - 58)  -  54,900  UZS"
                                                        "\nРазмер (60 - 62)  -  54,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_15":
        with open("PHOTOS/Products/Product 15.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  54,900  UZS"
                                                        "\nРазмер (44 - 46)  -  54,900  UZS"
                                                        "\nРазмер (48 - 50)  -  54,900  UZS"
                                                        "\nРазмер (52 - 54)  -  54,900  UZS"
                                                        "\nРазмер (56 - 58)  -  54,900  UZS"
                                                        "\nРазмер (60 - 62)  -  54,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_16":
        with open("PHOTOS/Products/Product 16.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  20,900  UZS"
                                                        "\nРазмер (44 - 46)  -  20,900  UZS"
                                                        "\nРазмер (48 - 50)  -  20,900  UZS"
                                                        "\nРазмер (52 - 54)  -  20,900  UZS"
                                                        "\nРазмер (56 - 58)  -  20,900  UZS"
                                                        "\nРазмер (60 - 62)  -  20,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_17":
        with open("PHOTOS/Products/Product 17.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  15,900  UZS"
                                                        "\nРазмер (44 - 46)  -  15,900  UZS"
                                                        "\nРазмер (48 - 50)  -  15,900  UZS"
                                                        "\nРазмер (52 - 54)  -  15,900  UZS"
                                                        "\nРазмер (56 - 58)  -  15,900  UZS"
                                                        "\nРазмер (60 - 62)  -  15,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_18":
        with open("PHOTOS/Products/Product 18.jpg", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  26,900  UZS"
                                                        "\nРазмер (44 - 46)  -  26,900  UZS"
                                                        "\nРазмер (48 - 50)  -  26,900  UZS"
                                                        "\nРазмер (52 - 54)  -  26,900  UZS"
                                                        "\nРазмер (56 - 58)  -  26,900  UZS"
                                                        "\nРазмер (60 - 62)  -  26,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_order_product":
        bot.send_message(call.message.chat.id, "<b>"
                                               "Контакт:  +998907043434"
                                               "</b>", parse_mode="html")