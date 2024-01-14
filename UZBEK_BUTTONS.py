import telebot

class Uzbek_Buttons:

    MenuButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MenuButton.row("🛒  Tovarlar")
    MenuButton.row("📃  Biz haqimizda", "🆘  Tezkor aloqa")
    MenuButton.row("🌐  Tilni o'zgartirish")

    CatalogButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    CatalogButton.row("🏠  Asosiy menu")
    CatalogButton.row("Kindik churrasi uchun bandaj")
    CatalogButton.row("To'qimachilik qoplamali elastik bandaj")
    CatalogButton.row("Ortopedik bo'yinbog' (kattalar uchun)")
    CatalogButton.row("Ortopedik bo'yinbog' (bolalar uchun)")
    CatalogButton.row("Varikoz tomirlaridan golflar")
    CatalogButton.row("Varikoz tomirlari uchun kompressli leggings (yozgi)")
    CatalogButton.row("Varikoz tomirlari uchun kompressli leggings")
    CatalogButton.row("Ortopedik holatni tuzatuvchi (bolalar uchun)")
    CatalogButton.row("Ortopedik holatni tuzatuvchi (kattalar uchun)")
    CatalogButton.row("Qo'l bandi (kattalar uchun)")
    CatalogButton.row("Qo'l bandi (bolalar uchun)")
    CatalogButton.row("Homilador ayollar uchun tug'ilishdan oldin kamar")
    CatalogButton.row("Tug'ilgandan keyin va sezaryen keyin kamar")
    CatalogButton.row("Elastik kamar")
    CatalogButton.row("Operatsiyadan keyingi kamar")
    CatalogButton.row("Hernisi bilan umurtqa pog'onasi uchun korset")
    CatalogButton.row("Elastik tizza yostig'i")
    CatalogButton.row("Elastik tizza yostig'i (yozgi)")
