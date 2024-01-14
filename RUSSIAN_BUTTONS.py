import telebot

class Russian_Buttons:

    MenuButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MenuButton.row("🛒  Товары")
    MenuButton.row("📃  О нас", "🆘  Связаться")
    MenuButton.row("🌐  Поменять язык")



    CatalogButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    CatalogButton.row("🏠  Главное меню")
    CatalogButton.row("Бандаж для пупочной грыжи")
    CatalogButton.row("Бинт эластичный ленточный с текстильным покрытием")
    CatalogButton.row("Воротник для шеи ортопедический (взрослый)")
    CatalogButton.row("Воротник для шеи ортопедический (детский)")
    CatalogButton.row("Гольфы от варикоза")
    CatalogButton.row("Гетры компрессионные при варикозе (летние)")
    CatalogButton.row("Гетры компрессионные при варикозе")
    CatalogButton.row("Корректор осанки ортопедический (детский)")
    CatalogButton.row("Корректор осанки ортопедический (взрослый)")
    CatalogButton.row("Повязка для руки (взрослая)")
    CatalogButton.row("Повязка для руки (детская)")
    CatalogButton.row("Пояс до родовой для беременных")
    CatalogButton.row("Пояс после родовой и после кесарева сечения")
    CatalogButton.row("Пояс эластичный")
    CatalogButton.row("Пояс послеоперационный")
    CatalogButton.row("Корсет для позвоночника при грыже")
    CatalogButton.row("Наколенник эластичный")
    CatalogButton.row("Наколенник эластичный (летний)")

