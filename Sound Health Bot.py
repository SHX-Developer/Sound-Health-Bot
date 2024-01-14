import telebot
import sqlite3
import datetime
import time

import CONFIG

from RUSSIAN_BUTTONS import Russian_Buttons
from UZBEK_BUTTONS import Uzbek_Buttons

from INLINE_BUTTONS import Inline_Buttons
from RUSSIAN_INLINE_BUTTONS import Russian_Inline_Buttons
from UZBEK_INLINE_BUTTONS import Uzbek_Inline_Buttons


bot = telebot.TeleBot(CONFIG.TOKEN)

db = sqlite3.connect("DATABASE.db", check_same_thread=False)
sql = db.cursor()

DateTime = datetime.datetime.now()

sql.execute('''CREATE TABLE IF NOT EXISTS user_data (ID INTEGER, USERNAME TEXT, FIRST_NAME TEXT, LAST_NAME TEXT, DATE_TIME TIMESWAP)''')
db.commit()

user_dict = {}

class User:
    def __init__(self, name):
        self.name=name
        self.surname = None
        self.mail = None
        self.number = None



@bot.message_handler(commands=['start'])
def start(message):

    sql.execute(f'''SELECT ID FROM user_data WHERE ID = {message.chat.id}''')
    user_id = sql.fetchone()

    if user_id is None:

        sql.execute('''INSERT INTO user_data (ID, USERNAME, FIRST_NAME, LAST_NAME, DATE_TIME) VALUES (?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), DateTime))
        db.commit()

        with open("PHOTOS/Bot Picture.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, '<b> 👋  Xush kelibsiz  /  Добро пожаловать  👋\n\n🇺🇿  Tilni tanlang  /  Выберите язык  🇷🇺 </b>', parse_mode='html', reply_markup=Inline_Buttons.reg_language_inline)

    else:

        with open("PHOTOS/Bot Picture.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, '<b> 👋  Xush kelibsiz  /  Добро пожаловать  👋\n\n🇺🇿  Tilni tanlang  /  Выберите язык  🇷🇺 </b>', parse_mode='html', reply_markup=Inline_Buttons.language_inline)







@bot.message_handler(content_types=["text"])
def text(message):



                                                                                #  RUSSIAN BUTTONS  #

    if message.text == "🛒  Товары":
        bot.send_message(message.chat.id, "<b> Выберите товар: </b>", parse_mode='html', reply_markup=Russian_Buttons.CatalogButton)

    if message.text == "📃  О нас":
        bot.send_message(message.chat.id,   "<b>"
                                            'Адрес:  г. Ташкент, Учтепа тумани 22-мавзе, 23-уй, 44-хонадон. '
                                            '\nТел:   +99890 7043434'
                                            '\nР/с: 20208000000735476001'
                                            '\nТОШКЕНТ Ш., "ТУРКИСТОН" ХАТ БАНКИНИНГ БОШ ОФИСИ'
                                            '\nМФО: 01104  '
                                            '\nИНН: 304681582 '
                                            '\nОКЭД: 32990'
                                            "</b>", parse_mode='html')

    if message.text == "🆘  Связаться":
        user_name = bot.send_message(message.chat.id, '<b> Введите своё имя: </b>', parse_mode='html', reply_markup=None)
        bot.register_next_step_handler(user_name, ru_request_surname)

    if message.text == "🌐  Поменять язык":
        bot.send_message(message.chat.id, "<b> Выберите язык:  </b>", parse_mode='html', reply_markup=Inline_Buttons.language_inline)

    if message.text == "🏠  Главное меню":
        bot.send_message(message.chat.id, "<b> Главное меню: </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButton)





                                                                                #  UZBEK BUTTONS  #

    if message.text == "🛒  Tovarlar":
        bot.send_message(message.chat.id, "<b> Tovarni tanlang: </b>", parse_mode='html', reply_markup=Uzbek_Buttons.CatalogButton)

    if message.text == "📃  Biz haqimizda":
        bot.send_message(message.chat.id,   "<b>"
                                            'Адрес:  г. Ташкент, Учтепа тумани 22-мавзе, 23-уй, 44-хонадон. '
                                            '\nТел:   +99890 7043434'
                                            '\nР/с: 20208000000735476001'
                                            '\nТОШКЕНТ Ш., "ТУРКИСТОН" ХАТ БАНКИНИНГ БОШ ОФИСИ'
                                            '\nМФО: 01104  '
                                            '\nИНН: 304681582 '
                                            '\nОКЭД: 32990'
                                            "</b>", parse_mode='html')

    if message.text == "🆘  Tezkor aloqa":
        user_name = bot.send_message(message.chat.id, '<b> Ismingizni kiriting: </b>', parse_mode='html', reply_markup=None)
        bot.register_next_step_handler(user_name, uz_request_surname)

    if message.text == "🌐  Tilni o'zgartirish":
        bot.send_message(message.chat.id, "<b> Tilni tanlang:  </b>", parse_mode='html', reply_markup=Inline_Buttons.language_inline)

    if message.text == "🏠  Asosiy menu":
        bot.send_message(message.chat.id, "<b> Asosiy menu: </b>", parse_mode='html', reply_markup=Uzbek_Buttons.MenuButton)













    if message.text == "Бандаж для пупочной грыжи":
        with open("PHOTOS/Products/Product 1.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b> Бандаж – ортопедическое приспособление в виде пояса или корсета, которое поддерживает органы брюшной полости в нормальном анатомическом положении. "
                                                   "\nВ зависимости от назначения, фиксатор имеет разные степени жесткости. "
                                                   "\nБандаж для грыжи используется как средство вспомогательной терапии перед операцией по удалению выпячиваний, а также после нее. "
                                                   "\nПриспособление рекомендуют пациентам, которым по состоянию здоровья невозможно провести операцию по удалению грыжи. </b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_1_inline)

    if message.text == "Бинт эластичный ленточный с текстильным покрытием":
        with open("PHOTOS/Products/Product 2.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b> Бинт эластичный медицинский, размером, высокой степени растяжимости применяется для профилактики и лечения хронических венозных воспалительных процессов в до- и послеоперационный периоды, для профилактики образования гематом и удержания эндопротезов в стабильном состоянии при пластических операциях, а также для профилактики и лечения травм, связанных со спортом. </b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_2_inline)

    if message.text == "Воротник для шеи ортопедический (взрослый)":
        with open("PHOTOS/Products/Product 3.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Обеспечивает фиксацию шейного отдела людям разного роста и телосложения благодаря возможности подбора подходящей высоты основы;"
                                                   "\nМинимизирует осевую нагрузку на шейный отдел позвоночника;"
                                                   "\nПрепятствует перенапряжению и травматизации мышц шеи при физических нагрузках;"
                                                   "\nОказывает стабилизирующее и разгружающее действие, восстанавливает шейный лордоз, устраняет патологическое давление позвоночника на кровеносные сосуды и нормализует кровоснабжение головного мозга;"
                                                   "\nОказывает умеренное согревающее и стабилизирующее действие на «мышечный корсет» шеи за счет свойств основного материала;"
                                                   "\nХорошо отводит влагу и пропускает воздух благодаря использованию материала;"
                                                   "\nУдобен и комфортен при длительном ношении."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_3_inline)

    if message.text == "Воротник для шеи ортопедический (детский)":
        with open("PHOTOS/Products/Product 4.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                    "Подходит для круглосуточного использования;"
                                                    "\nМинимизирует осевую нагрузку на шейный отдел позвоночника;"
                                                    "\nПрепятствует перенапряжению и травматизации мышц шеи при физических нагрузках;"
                                                    "\nОказывает стабилизирующее и разгружающее действие, восстанавливает шейный лордоз;"
                                                    "\nУстраняет патологическое давление позвоночника на кровеносные сосуды и нормализует кровоснабжение головного мозга;"
                                                    "\nОказывает умеренное согревающее и стабилизирующее действие на «мышечный корсет» шеи за счет свойств основного материала."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_4_inline)

    if message.text == "Гольфы от варикоза":
        with open("PHOTOS/Products/Product 5.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Компрессионные гольфы представляют собой чулочно-носочные изделия для профилактики и лечения варикоза у женщин и мужчин. "
                                                   "\nВрачи рекомендуют ношение изделий при варикозном расширении вен и частых нагрузках на ноги. Регулярное ношение снимает боль, устраняет отечность, лечит трофические язвы и тромбозы. "
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_5_inline)

    if message.text == "Гетры компрессионные при варикозе (летние)":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Компрессионные гольфы для спорта  разработаны специально для людей, которые занимаются активными видами спорта."
                                                   "\nОсновная цель использования - нормализация венозного кровотока, сужение венозного расширения вен."
                                                   "\nМедицинские гольфы уменьшат нагрузку на сердечно-сосудистую и опорно-двигательную системы, а также обезопасят от неприятных болезней."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_6_inline)


    if message.text == "Гетры компрессионные при варикозе":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Компрессионные гольфы для спорта  разработаны специально для людей, которые занимаются активными видами спорта."
                                                   "\nОсновная цель использования - нормализация венозного кровотока, сужение венозного расширения вен."
                                                   "\nМедицинские гольфы уменьшат нагрузку на сердечно-сосудистую и опорно-двигательную системы, а также обезопасят от неприятных болезней."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_6_inline)


    if message.text == "Корректор осанки ортопедический (детский)":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Корректор осанки для детей оказывает формирование правильной осанки у детей. Индивидуальная коррекция осанки на протяжении дня. Разведение пояса верхних конечностей. Умеренная реклинация и разгрузка тел позвонков средне- и нижнегрудного и верхнепоясничного отделов с сохранением и восстановлением нормального тонуса мышц."
                                                   "\n\nПолужесткая фиксация позвоночника. Распрямляя плечи, корсет добавляет несколько сантиметров роста и поднимает грудь."
                                                   "\nНазначение: Формирование правильной осанки у детей, кифозы, кифосколиозы, крыловидные лопатки. Период реабилитации после травм и операций грудного и верхнепоясничного отделов позвоночника, ключицы. Профилактика прогрессирования искривления позвоночника и уменьшения декомпенсации сколиотической болезни."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_8_inline)


    if message.text == "Корректор осанки ортопедический (взрослый)":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Такой корсет назначается не только в лечебных, но и в профилактических целях. Он подходит как детям, так и взрослым, прекрасно помогая устранить проблемы с позвоночником и провести профилактику нарушений. К преимуществам подобного изделия следует отнести то, что оно: Позволяет предупредить различные искривления позвоночного столба. Предотвращает развитие заболеваний позвоночника, которые могут возникнуть в результате постоянной статической нагрузки. "
                                                   "\nКомпенсирует дефицит опорности. Способствует нормализации тонуса мышц проблемных участков спины. Сводит к минимиму нагрузки на межпозвоночные диски. Фиксирует и нормализует работу проблемных участков позвоночного столба. Разгружает позвонки, не позволяя им смещаться."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_18_inline)

    if message.text == "Повязка для руки (взрослая)":
        with open("PHOTOS/Products/Product 8.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Применение ортеза позволяет предотвратить развитие посттравматических осложнений:"
                                                   "\n\nСмешения сломанной кости."
                                                   "\nОтека."
                                                   "\nРазвития воспалительного процесса."
                                                   "\nОстрой боли при деформирующем артрозе."
                                                   "\nОртез обеспечивает правильное срастание сломанной кости. При сложных переломах бандаж используется для фиксации руки после установки эндопротеза."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_9_inline)

    if message.text == "Повязка для руки (детская)":
        with open("PHOTOS/Products/Product 9.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b> "
                                                   "• Комплексная реабилитация после ушибов, подвывихов, вывихов и переломов костей верхней конечности."
                                                   "\n• Фиксация верхней конечности при острых и хронических воспалительных заболеваниях суставов."
                                                   "\n• Повреждения локтевого сустава и предплечья."
                                                   "\n\nДействие:"
                                                   "\n• Обеспечивает разгрузку плеча и фиксацию локтевого сустава и предплечья."
                                                   "\n• Удерживает верхнюю конечность в функционально-выгодном положении."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_10_inline)

    if message.text == "Пояс до родовой для беременных":
        with open("PHOTOS/Products/Product 10.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo,  "<b>"
                                                    "Женщины, переживающие первую беременность, справедливо задаются вопросом, какую роль выполняет ношение бандажа. Перечислим основные «поддерживающие» достоинства дородового бандажа:"
                                                    "\n\nПредотвращает чрезмерное растяжение кожи во второй половине беременности;"
                                                    "\nСнимает нагрузку с поясничного отдела и с позвоночника;"
                                                    "\nПоддерживает живот, помогая плоду удерживать правильное положение;"
                                                    "\nУменьшает нагрузку на ноги, предотвращает варикозное расширение вен;"
                                                    "\nСнижает риск преждевременных родов при некоторых патологиях во время беременности."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_11_inline)

    if message.text == "Пояс после родовой и после кесарева сечения":
        with open("PHOTOS/Products/Product 11.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo,  "<b>"
                                                    "Поддержке передней стенке живота и внутренних органов в правильном положении;"
                                                    "\nЗащите послеоперационного шва: предотвращает растяжение и расхождение;"
                                                    "\nСозданию равномерного давления на послеоперационную область;"
                                                    "\nСокращению матки;"
                                                    "\nСнижению болезненных ощущений при движении;"
                                                    "\nУменьшению нагрузки на мышцы спины и позвоночник;"
                                                    "\nВрачи рекомендуют носить специальный бандаж, чтобы;"
                                                    "\nУскорить процесс заживление места разреза;"
                                                    "\nСнять напряжение и скорректировать брюшные мышцы;"
                                                    "\nПредотвратить опущение внутренних органов;"
                                                    "\nСнять нагрузку с мышц спинного отдела;"
                                                    "\nСократить боль при движении."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_12_inline)

    if message.text == "Пояс эластичный":
        with open("PHOTOS/Products/Product 12.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Пояс медицинский эластичный, для фиксации поясничного отдела позвоночника, c жесткими вставками и лентами-усилителями."
                                                    "\n\nНадежная фиксация и защита суставов и мышц;"
                                                    "\nИзделия хорошо облегают тело и моделируют его контуры благодаря эластичному полотну и специальному крою;"
                                                    "\nОбеспечивают максимальный комфорт."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_13_inline)

    if message.text == "Пояс послеоперационный":
        with open("PHOTOS/Products/Product 13.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo,  "<b>"
                                                    "Профилактирует внесение бактериальных агентов в рану;"
                                                    "\nВыполняет защиту послеоперационного участка от наружных механических повреждений;"
                                                    "\nПредотвращает появление гематом и кровоподтеков;"
                                                    "\nПомогает сохранить полный размер активных движений;"
                                                    "\nУменьшает неприятные ощущения во время движений;"
                                                    "\nСохраняет и поддерживает мышечный тонус."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_14_inline)

    if message.text == "Корсет для позвоночника при грыже":
        with open("PHOTOS/Products/Product 16.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Грыжа позвоночника"
                                                   "\nБолевой синдром в области поясницы(люмбалгия)."
                                                   "\nРадикулит (воспаление спиномозгового нерва)."
                                                   "\nМышечная слабость. Дегенеративно-дистрофические изменения."
                                                   "\nПред и послеоперационная реабилитация."
                                                   "\nПрофилактика заболеваний поясничного отдела позвоночника при бытовых и профессиональных нагрузках."
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_15_inline)

    if message.text == "Наколенник эластичный":
        with open("PHOTOS/Products/Product 17.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Фиксатор на коленный сустав изготовлен из современной  эластичной ткани, в состав которой входит полушерсть."
                                                   "\nМатериал обеспечивает согревающий эффект."
                                                   "\nПрактичен и очень прост в применении. "
                                                   "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_16_inline)

    if message.text == "Наколенник эластичный (летний)":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo,  "<b>"
                                                    "Остеоартроз (деформирующий артроз) I степени;"
                                                    "\nРевматоидный артрит;"
                                                    "\nРастяжения и перенапряжение капсульно-связочного аппарата;"
                                                    "\nУшибы мягких тканей;"
                                                    "\nОтдаленный период реабилитации после операций в области коленного сустава;"
                                                    "\nПрофилактика травм и заболеваний коленного сустава."
                                                    "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.product_17_inline)


    #  UZB PRODUCTS  #

    if message.text == "Kindik churrasi uchun bandaj":
        with open("PHOTOS/Products/Product 1.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Bandaj - qorin bo'shlig'i a'zolarini normal anatomik holatda qo'llab-quvvatlaydigan kamar yoki korset ko'rinishidagi ortopedik qurilma."
                                                   "\nMaqsadga qarab, mandal turli darajadagi qattiqlikka ega."
                                                   "\nHerniya bandaji protrusionni olib tashlash uchun operatsiyadan oldin va keyin yordamchi terapiya sifatida ishlatiladi."
                                                   "\nQurilma sog'lig'i sababli churrani olib tashlash uchun operatsiya qila olmaydigan bemorlarga tavsiya etiladi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_1_inline)

    if message.text == "To'qimachilik qoplamali elastik bandaj":
        with open("PHOTOS/Products/Product 2.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Elastik tibbiy bandaj, o'lchamdagi, cho'zilish darajasi yuqori, operatsiyadan oldingi va keyingi davrlarda surunkali venoz yallig'lanish jarayonlarining oldini olish va davolash uchun ishlatiladi,"
                                                   "gematomalarning paydo bo'lishining oldini olish va plastik jarrohlik paytida endoprotezlarni barqaror holatda saqlash,"
                                                   "sport bilan bog'liq jarohatlarning oldini olish va davolash uchun."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_2_inline)

    if message.text == "Ortopedik bo'yinbog' (kattalar uchun)":
        with open("PHOTOS/Products/Product 3.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Bazaning mos balandligini tanlash imkoniyati tufayli turli balandlikdagi va quriladigan odamlar uchun servikal mintaqani mahkamlashni ta'minlaydi;"
                                                   "\nServikal umurtqa pog'onasidagi eksenel yukni kamaytiradi;"
                                                   "\nJismoniy mashqlar paytida bo'yin muskullarining haddan tashqari kuchlanishini va travmatizatsiyasini oldini oladi;"
                                                   "\nBu barqarorlashtiruvchi va tushirish ta'siriga ega, servikal lordozni tiklaydi, umurtqa pog'onasining qon tomirlariga patologik bosimini yo'q qiladi va miyaning qon ta'minotini normallantiradi;"
                                                   "\nAsosiy materialning xususiyatlari tufayli bo'yinning <mushak korseti> ga motadil isinish va barqarorlashtiruvchi ta'sir ko'rsatadi;"
                                                   "\nU namlikni yaxshi olib tashlaydi va materialdan foydalanish orqali havo o'tkazadi;"
                                                   "\nUzoq vaqt davomida kiyish uchun qulay va qulay."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_3_inline)

    if message.text == "Ortopedik bo'yinbog' (bolalar uchun)":
        with open("PHOTOS/Products/Product 4.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "24/7 foydalanish uchun javob beradi;"
                                                   "\nServikal umurtqa pog'onasidagi eksenel yukni kamaytiradi;"
                                                   "\nJismoniy mashqlar paytida bo'yin muskullarining haddan tashqari kuchlanishini va travmatizatsiyasini oldini oladi;"
                                                   "\nBu barqarorlashtiruvchi va tushirish ta'siriga ega, servikal lordozni tiklaydi;"
                                                   "\nQon tomirlariga umurtqa pog'onasining patologik bosimini yo'q qiladi va miyaning qon ta'minotini normallantiradi;"
                                                   "\nAsosiy materialning xususiyatlari tufayli bo'yinning <mushak korseti> ga mo''tadil isinish va barqarorlashtiruvchi ta'sir ko'rsatadi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_4_inline)

    if message.text == "Varikoz tomirlaridan golflar":
        with open("PHOTOS/Products/Product 5.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Siqish paypoqlari ayollar va erkaklarda varikoz tomirlarining oldini olish va davolash uchun paypoqdir."
                                                   "\nShifokorlar varikoz tomirlari va oyoqlarda tez-tez yuklanadigan mahsulotlarni kiyishni tavsiya qiladi."
                                                   "\nMuntazam kiyish og'riqni engillashtiradi, shishishni yo'q qiladi, trofik yaralar va trombozni davolaydi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_5_inline)

    if message.text == "Varikoz tomirlari uchun kompressli leggings (yozgi)":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Sport uchun kompressor paypoqlari faol sport bilan shug'ullanadigan odamlar uchun maxsus mo'ljallangan."
                                                   "\nFoydalanishning asosiy maqsadi venoz qon oqimini normallashtirish, tomirlarning venoz kengayishini toraytirishdir."
                                                   "\nTibbiy paypoqlar yurak-qon tomir va mushak-skelet tizimiga yukni kamaytiradi, shuningdek, yoqimsiz kasalliklardan himoya qiladi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_6_inline)

    if message.text == "Varikoz tomirlari uchun kompressli leggings":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Sport uchun kompressor paypoqlari faol sport bilan shug'ullanadigan odamlar uchun maxsus mo'ljallangan."
                                                   "\nFoydalanishning asosiy maqsadi venoz qon oqimini normallashtirish, tomirlarning venoz kengayishini toraytirishdir."
                                                   "\nTibbiy paypoqlar yurak-qon tomir va mushak-skelet tizimiga yukni kamaytiradi, shuningdek, yoqimsiz kasalliklardan himoya qiladi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_6_inline)

    if message.text == "Ortopedik holatni tuzatuvchi (bolalar uchun)":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Bolalar uchun duruş tuzatuvchisi bolalarda to'g'ri holatni shakllantirishni ta'minlaydi. Kun davomida individual holatni tuzatish."
                                                   "\nYuqori oyoq-qo'llarning kamarini ko'paytirish. Oddiy mushak ohangini saqlab qolish va tiklash bilan o'rta va pastki ko'krak va yuqori lomber mintaqalarning umurtqali tanalarini o'rtacha egilish va tushirish."
                                                   "\n\nOrqa miyaning yarim qattiq fiksatsiyasi. Elkalarni to'g'rilab, korset bir necha santimetr balandlikni qo'shib, ko'krak qafasini ko'taradi."
                                                   "\nMaqsad: Bolalarda to'g'ri holatni shakllantirish, kifoz, kifoskolioz, skapula pterygoid. Ko'krak va yuqori bel umurtqalari, bo'yinbog'ning jarohatlari va operatsiyalaridan keyin reabilitatsiya davri."
                                                   "\nOrqa miya egriligining rivojlanishining oldini olish va skoliotik kasallikning dekompensatsiyasini kamaytirish."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_8_inline)

    if message.text == "Ortopedik holatni tuzatuvchi (kattalar uchun)":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Bunday korset nafaqat terapevtik, balki profilaktika maqsadida ham buyuriladi. Bu bolalar va kattalar uchun mos keladi, umurtqa pog'onasi bilan bog'liq muammolarni bartaraf etishga va buzilishlarning oldini olishga mukammal yordam beradi. "
                                                   "\nBunday mahsulotning afzalliklari quyidagilardan iborat: Orqa miyaning turli egriliklarini oldini olishga imkon beradi. Doimiy statik yukdan kelib chiqishi mumkin bo'lgan umurtqa pog'onasi kasalliklarining rivojlanishiga to'sqinlik qiladi."
                                                   "\nQo'llab-quvvatlashning etishmasligini qoplaydi. Orqaning muammoli joylarida mushaklarning ohangini normallashtirishga yordam beradi. Intervertebral disklardagi yukni kamaytiradi. Orqa miya muammoli joylarini tuzatadi va normalizatsiya qiladi. Umurtqalarni bo'shatadi, ularning harakatlanishiga yo'l qo'ymaydi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_18_inline)

    if message.text == "Qo'l bandi (kattalar uchun)":
        with open("PHOTOS/Products/Product 8.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Ortezdan foydalanish shikastlanishdan keyingi asoratlarni rivojlanishining oldini olishga yordam beradi:"
                                                   "\n\nSingan suyaklar aralashmasi."
                                                   "\nShish."
                                                   "\nyallig'lanish jarayonining rivojlanishi."
                                                   "\nDeformatsiya qiluvchi artrozda o'tkir og'riq."
                                                   "\nOrtez singan suyakning to'g'ri davolanishini ta'minlaydi. Murakkab yoriqlar bo'lsa, bint endoprotezni o'rnatgandan so'ng qo'lni tuzatish uchun ishlatiladi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_9_inline)

    if message.text == "Qo'l bandi (bolalar uchun)":
        with open("PHOTOS/Products/Product 9.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b> "
                                                   "• Ko'karishlar, subluksatsiyalar, dislokatsiyalar va yuqori oyoq-qo'l suyaklarining sinishidan keyin kompleks reabilitatsiya."
                                                   "\n• Bo'g'imlarning o'tkir va surunkali yallig'lanish kasalliklarida yuqori oyoq-qo'llarni mahkamlash."
                                                   "\n• Tirsak bo'g'imi va bilakning shikastlanishi."
                                                   "\n\nHarakat:"
                                                   "\n• Yelkaning tushirilishini va tirsak bo'g'imi va bilakning mahkamlanishini ta'minlaydi."
                                                   "\n• Yuqori oyoq-qo'lni funktsional jihatdan qulay holatda ushlab turadi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_10_inline)

    if message.text == "Homilador ayollar uchun tug'ilishdan oldin kamar":
        with open("PHOTOS/Products/Product 10.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Birinchi homiladorligini boshdan kechirayotgan ayollar bint qanday rol o'ynashini haqli ravishda hayratda qoldiradilar. Biz prenatal bandajning asosiy <qo'llab-quvvatlovchi> afzalliklarini sanab o'tamiz:"
                                                   "\n\nHomiladorlikning ikkinchi yarmida terining haddan tashqari cho'zilishining oldini oladi;"
                                                   "\nLomber va umurtqa pog'onasidagi stressni engillashtiradi;"
                                                   "\nQorin bo'shlig'ini qo'llab-quvvatlaydi, homilaning to'g'ri pozitsiyasini saqlashga yordam beradi;"
                                                   "\nOyoqlardagi yukni kamaytiradi, varikoz tomirlarini oldini oladi;"
                                                   "\nHomiladorlik davrida ma'lum patologiyalarda erta tug'ilish xavfini kamaytiradi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_11_inline)

    if message.text == "Tug'ilgandan keyin va sezaryen keyin kamar":
        with open("PHOTOS/Products/Product 11.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Qorinning old devorini va ichki organlarni to'g'ri holatda qo'llab-quvvatlash;"
                                                   "\nOperatsiyadan keyingi tikuvni himoya qilish: cho'zish va divergensiyani oldini oladi;"
                                                   "\nOperatsiyadan keyingi hududda bir xil bosim yaratish;"
                                                   "\nbachadonning qisqarishi;"
                                                   "\nHarakat paytida og'riqni kamaytirish;"
                                                   "\nOrqa va orqa miya mushaklariga yukni kamaytirish;"
                                                   "\nShifokorlar maxsus bandaj kiyishni tavsiya qiladilar;"
                                                   "\nKesilgan joyning shifo jarayonini tezlashtirish;"
                                                   "\nTaranglikni engillashtiring va qorin bo'shlig'i mushaklarini sozlang;"
                                                   "\nIchki organlarning prolapsasini oldini olish;"
                                                   "\nOrqa miya mintaqasining mushaklaridan stressni yo'qotish;"
                                                   "\nHarakat paytida og'riqni kamaytiring."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_12_inline)

    if message.text == "Elastik kamar":
        with open("PHOTOS/Products/Product 12.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Qattiq qo'shimchalar va mustahkamlovchi bantlar bilan bel umurtqasini mahkamlash uchun elastik tibbiy kamar."
                                                   "\n\nQo'shimchalar va mushaklarni ishonchli mahkamlash va himoya qilish;"
                                                   "\nMahsulotlar elastik mato va maxsus kesim tufayli tanaga yaxshi mos keladi va uning konturlarini modellashtiradi;"
                                                   "\nMaksimal qulaylikni ta'minlang."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_13_inline)

    if message.text == "Operatsiyadan keyingi kamar":
        with open("PHOTOS/Products/Product 13.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Yaraga bakterial vositalarning kiritilishini oldini oladi;"
                                                   "\nOperatsiyadan keyingi hududni tashqi mexanik shikastlanishdan himoya qilishni amalga oshiradi;"
                                                   "\nGematomalar va ko'karishlar paydo bo'lishining oldini oladi;"
                                                   "\nFaol harakatlarning to'liq hajmini saqlashga yordam beradi;"
                                                   "\nHarakatlar paytida noqulaylikni kamaytiradi;"
                                                   "\nMushaklar ohangini saqlaydi va saqlaydi."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_14_inline)

    if message.text == "Hernisi bilan umurtqa pog'onasi uchun korset":
        with open("PHOTOS/Products/Product 16.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Orqa miya churrasi"
                                                   "\nLomber mintaqada og'riq (lumbalgiya)."
                                                   "\nSiyatik (orqa miya nervining yallig'lanishi)."
                                                   "\nMushaklar kuchsizligi. Degenerativ-distrofik o'zgarishlar."
                                                   "\nOperatsiyadan oldingi va keyingi reabilitatsiya."
                                                   "\nMaishiy va professional stressda lomber umurtqa pog'onasi kasalliklarining oldini olish."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_15_inline)

    if message.text == "Elastik tizza yostig'i":
        with open("PHOTOS/Products/Product 17.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Tizza qo'shimchasidagi fiksator zamonaviy elastik matodan tayyorlangan bo'lib, u jun aralashmasini o'z ichiga oladi."
                                                   "\nMateriallar issiqlik ta'sirini ta'minlaydi."
                                                   "\nAmaliy va foydalanish juda oson."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_16_inline)

    if message.text == "Elastik tizza yostig'i (yozgi)":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, "<b>"
                                                   "Osteoartrit (deformatsiya qiluvchi artroz) I daraja;"
                                                   "\nRomatoid artrit;"
                                                   "\nKapsulyar-ligamentli apparatlarning burilishlari va haddan tashqari kuchlanishi;"
                                                   "\nYumshoq to'qimalarda ko'karishlar;"
                                                   "\ntizza bo'g'imlari sohasidagi operatsiyalardan keyin uzoq muddatli reabilitatsiya davri;"
                                                   "\nTizza bo'g'imlarining shikastlanishlari va kasalliklarining oldini olish."
                                                   "</b>", parse_mode='html', reply_markup=Uzbek_Inline_Buttons.product_17_inline)







def ru_request_surname(message):

    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user

    user_surname = bot.send_message(message.chat.id, '<b> Введите вашу фамилию: </b>', parse_mode='html')
    bot.register_next_step_handler(user_surname, ru_request_mail)

def ru_request_mail(message):

    chat_id = message.chat.id
    surname = message.text
    user = user_dict[chat_id]
    user.surname = surname

    user_mail = bot.send_message(message.chat.id, '<b> Введите вашу электронную почту: </b>', parse_mode='html')
    bot.register_next_step_handler(user_mail, ru_request_number)

def ru_request_number(message):

    chat_id = message.chat.id
    mail = message.text
    user = user_dict[chat_id]
    user.mail = mail

    user_number = bot.send_message(message.chat.id, '<b> Введите ваш номер телефона: </b>', parse_mode='html')
    bot.register_next_step_handler(user_number, ru_request_send)

def ru_request_send(message):

    chat_id = message.chat.id
    number = message.text
    user = user_dict[chat_id]
    user.number = number

    bot.send_message('@GhoerNEc15', f"<b>"
                                     f"Новая заявка  ⚠"
                                     f"\n\nUser ID:  {str(message.chat.id)}"
                                     f"\nUsername:  @{str(message.from_user.username)}"
                                     f"\nFirst Name:  {str(message.from_user.first_name)}"
                                     f"\nLast Name:  {str(message.from_user.last_name)}"
                                     f"\n\nИмя:  {str(user.name)}"
                                     f"\nФамилия:  {str(user.surname)}"
                                     f"\nЭлектронная почта:  {str(user.mail)}"
                                     f"\nНомер телефона:  {str(message.text)}"
                                     f"</b>", parse_mode="html")

    bot.send_message(message.chat.id, '<b>'
                                      'Ваша заявка принята  ✅'
                                      '\n\nПожалуйста подождите, как только освободятся наши специалисты, сразу же с вами свяжутся  ✅'
                                      '</b>', parse_mode='html')



def uz_request_surname(message):

    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user

    user_surname = bot.send_message(message.chat.id, '<b> Familiyangizni kiriting: </b>', parse_mode='html')
    bot.register_next_step_handler(user_surname, uz_request_mail)

def uz_request_mail(message):

    chat_id = message.chat.id
    surname = message.text
    user = user_dict[chat_id]
    user.surname = surname

    user_mail = bot.send_message(message.chat.id, '<b> Elektron pochtangizni kiriting: </b>', parse_mode='html')
    bot.register_next_step_handler(user_mail, uz_request_number)

def uz_request_number(message):

    chat_id = message.chat.id
    mail = message.text
    user = user_dict[chat_id]
    user.mail = mail

    user_number = bot.send_message(message.chat.id, '<b> Telefon raqamingizni kiriting: </b>', parse_mode='html')
    bot.register_next_step_handler(user_number, uz_request_send)

def uz_request_send(message):

    chat_id = message.chat.id
    number = message.text
    user = user_dict[chat_id]
    user.number = number

    bot.send_message('@GhoerNEc15', f"<b>"
                                     f"Новая заявка  ⚠"
                                     f"\n\nUser ID:  {str(message.chat.id)}"
                                     f"\nUsername:  @{str(message.from_user.username)}"
                                     f"\nFirst Name:  {str(message.from_user.first_name)}"
                                     f"\nLast Name:  {str(message.from_user.last_name)}"
                                     f"\n\nИмя:  {str(user.name)}"
                                     f"\nФамилия:  {str(user.surname)}"
                                     f"\nЭлектронная почта:  {str(user.mail)}"
                                     f"\nНомер телефона:  {str(message.text)}"
                                     f"</b>", parse_mode="html")

    bot.send_message(message.chat.id, '<b>'
                                      'Sizning arizangiz qabul qilindi ✅'
                                      "\n\nIltimos, kuting, mutaxassislarimiz bo'sh bo'lishi bilanoq siz bilan darhol bog'lanishadi✅"
                                      '</b>', parse_mode='html')




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



    #  RU PRODUCTS CALLBACK  #

    if call.data == "ru_product_1":
        with open("PHOTOS/Products/Product 1.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  68,770  UZS"
                                                        "\nРазмер (44 - 46)  -  68,770  UZS"
                                                        "\nРазмер (48 - 50)  -  68,770  UZS"
                                                        "\nРазмер (52 - 54)  -  68,770  UZS"
                                                        "\nРазмер (56 - 58)  -  68,770  UZS"
                                                        "\nРазмер (60 - 62)  -  68,770  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_2":
        with open("PHOTOS/Products/Product 2.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "(8 см - 1,5 м)  -  14,170  UZS"
                                                        "\n(8 см - 3 м)  -  20,670  UZS"
                                                        "\n(8 см - 4 м)  -  21,970  UZS"
                                                        "\n(8 см - 5 м)  -  25,870  UZS"
                                                        "\n(10 см - 1,5 м)  -  16,770  UZS"
                                                        "\n(10 см - 3 м)  -  20,670  UZS"
                                                        "\n(10 см - 4 м)  -  28,870  UZS"
                                                        "\n(10 см - 5 м)  -  31,070  UZS"
                                                        "\n(12 см - 1,5 м)  -  15,470  UZS"
                                                        "\n(12 см - 3 м)  -  27,170  UZS"
                                                        "\n(12 см - 4 м)  -  29,770  UZS"
                                                        "\n(12 см - 5 м)  -  32,370  UZS"
                                                        "\n(14 см - 1,5 м)  -  15,470  UZS"
                                                        "\n(14 см - 3 м)  -  27,170  UZS"
                                                        "\n(14 см - 4 м)  -  32,370  UZS"
                                                        "\n(14 см - 5 м)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_3":
        with open("PHOTOS/Products/Product 3.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  34,450  UZS"
                                                        "\nРазмер (44 - 46)  -  34,450  UZS"
                                                        "\nРазмер (48 - 50)  -  34,450  UZS"
                                                        "\nРазмер (52 - 54)  -  34,450  UZS"
                                                        "\nРазмер (56 - 58)  -  34,450  UZS"
                                                        "\nРазмер (60 - 62)  -  34,450  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_4":
        with open("PHOTOS/Products/Product 4.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Лет (6 - 8)  -  31,850  UZS"
                                                        "\nЛет (9 - 11)  -  31,850  UZS"
                                                        "\nЛет (12 - 15)  -  31,850  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_5":
        with open("PHOTOS/Products/Product 5.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (37 - 40)  -  33,670  UZS"
                                                        "\nРазмер (41 - 44)  -  33,670  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_6":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42) (летние)  -  34,970  UZS"
                                                        "\nРазмер (44 - 46) (летние)  -  34,970  UZS"
                                                        "\nРазмер (48 - 50) (летние)  -  34,970  UZS"
                                                        "\nРазмер (52 - 54) (летние)  -  34,970  UZS"
                                                        "\nРазмер (56 - 58) (летние)  -  34,970  UZS"
                                                        "\nРазмер (60 - 62) (летние)  -  34,970  UZS"
                                                        "\nРазмер (40 - 42)  -  34,970  UZS"
                                                        "\nРазмер (44 - 46)  -  34,970  UZS"
                                                        "\nРазмер (48 - 50)  -  34,970  UZS"
                                                        "\nРазмер (52 - 54)  -  34,970  UZS"
                                                        "\nРазмер (56 - 58)  -  34,970  UZS"
                                                        "\nРазмер (60 - 62)  -  34,970  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_7":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  34,970  UZS"
                                                        "\nРазмер (44 - 46)  -  34,970  UZS"
                                                        "\nРазмер (48 - 50)  -  34,970  UZS"
                                                        "\nРазмер (52 - 54)  -  34,970  UZS"
                                                        "\nРазмер (56 - 58)  -  34,970  UZS"
                                                        "\nРазмер (60 - 62)  -  34,970  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_8":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (6 - 8 лет) (детские)  -  75,270  UZS"
                                                        "\nРазмер (9 - 11 лет) (детские)  -  75,270  UZS"
                                                        "\nРазмер (12 - 15 лет) (детские)  -  75,270  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_18":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "\nРазмер (40 - 42) (для взрослых)  -  94,770  UZS"
                                                        "\nРазмер (44 - 46) (для взрослых)  -  94,770  UZS"
                                                        "\nРазмер (48 - 50) (для взрослых)  -  94,770  UZS"
                                                        "\nРазмер (52 - 54) (для взрослых)  -  94,770  UZS"
                                                        "\nРазмер (56 - 58) (для взрослых)  -  94,770  UZS"
                                                        "\nРазмер (60 - 62) (для взрослых)  -  94,770  UZS"
                                                        "</b>", parse_mode = 'html', reply_markup = Russian_Inline_Buttons.order_product_inline)


    if call.data == "ru_product_9":
        with open("PHOTOS/Products/Product 8.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  44,070  UZS"
                                                        "\nРазмер (44 - 46)  -  44,070  UZS"
                                                        "\nРазмер (48 - 50)  -  44,070  UZS"
                                                        "\nРазмер (52 - 54)  -  44,070  UZS"
                                                        "\nРазмер (56 - 58)  -  44,070  UZS"
                                                        "\nРазмер (60 - 62)  -  44,070  UZS"
                                                        "\nРазмер (40 - 42) (летние)  -  37,570  UZS"
                                                        "\nРазмер (44 - 46) (летние)  -  37,570  UZS"
                                                        "\nРазмер (48 - 50) (летние)  -  37,570  UZS"
                                                        "\nРазмер (52 - 54) (летние)  -  37,570  UZS"
                                                        "\nРазмер (56 - 58) (летние)  -  37,570  UZS"
                                                        "\nРазмер (60 - 62) (летние)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_10":
        with open("PHOTOS/Products/Product 9.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Лет (6 - 8)  -  42,900  UZS"
                                                        "\nЛет (9 - 11)  -  42,900  UZS"
                                                        "\nЛет (12 - 15)  -  42,900  UZS"
                                                        "\nЛет (6 - 8) (летняя)  -  36,400  UZS"
                                                        "\nЛет (9 - 11) (летняя)  -  36,400  UZS"
                                                        "\nЛет (12 - 15) (летняя)  -  36,400  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_11":
        with open("PHOTOS/Products/Product 10.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  59,150  UZS"
                                                        "\nРазмер (44 - 46)  -  59,150  UZS"
                                                        "\nРазмер (48 - 50)  -  59,150  UZS"
                                                        "\nРазмер (52 - 54)  -  59,150  UZS"
                                                        "\nРазмер (56 - 58)  -  59,150  UZS"
                                                        "\nРазмер (60 - 62)  -  59,150  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_12":
        with open("PHOTOS/Products/Product 11.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  66,170  UZS"
                                                        "\nРазмер (44 - 46)  -  66,170  UZS"
                                                        "\nРазмер (48 - 50)  -  66,170  UZS"
                                                        "\nРазмер (52 - 54)  -  66,170  UZS"
                                                        "\nРазмер (56 - 58)  -  66,170  UZS"
                                                        "\nРазмер (60 - 62)  -  66,170  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_13":
        with open("PHOTOS/Products/Product 12.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  37,570  UZS"
                                                        "\nРазмер (44 - 46)  -  37,570  UZS"
                                                        "\nРазмер (48 - 50)  -  37,570  UZS"
                                                        "\nРазмер (52 - 54)  -  37,570  UZS"
                                                        "\nРазмер (56 - 58)  -  37,570  UZS"
                                                        "\nРазмер (60 - 62)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_14":
        with open("PHOTOS/Products/Product 13.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  71,370  UZS"
                                                        "\nРазмер (44 - 46)  -  71,370  UZS"
                                                        "\nРазмер (48 - 50)  -  71,370  UZS"
                                                        "\nРазмер (52 - 54)  -  71,370  UZS"
                                                        "\nРазмер (56 - 58)  -  71,370  UZS"
                                                        "\nРазмер (60 - 62)  -  71,370  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_15":
        with open("PHOTOS/Products/Product 16.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  71,370  UZS"
                                                        "\nРазмер (44 - 46)  -  71,370  UZS"
                                                        "\nРазмер (48 - 50)  -  71,370  UZS"
                                                        "\nРазмер (52 - 54)  -  71,370  UZS"
                                                        "\nРазмер (56 - 58)  -  71,370  UZS"
                                                        "\nРазмер (60 - 62)  -  71,370  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_16":
        with open("PHOTOS/Products/Product 17.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42)  -  27,170  UZS"
                                                        "\nРазмер (44 - 46)  -  27,170  UZS"
                                                        "\nРазмер (48 - 50)  -  27,170  UZS"
                                                        "\nРазмер (52 - 54)  -  27,170  UZS"
                                                        "\nРазмер (56 - 58)  -  27,170  UZS"
                                                        "\nРазмер (60 - 62)  -  27,170  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_17":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Размер (40 - 42) (летний)  -  20,670  UZS"
                                                        "\nРазмер (44 - 46) (летний)  -  20,670  UZS"
                                                        "\nРазмер (48 - 50) (летний)  -  20,670  UZS"
                                                        "\nРазмер (52 - 54) (летний)  -  20,670  UZS"
                                                        "\nРазмер (56 - 58) (летний)  -  20,670  UZS"
                                                        "\nРазмер (60 - 62) (летний)  -  20,670  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "ru_product_18":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
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
                                               "\nКонтакт:  +998997719888"
                                               "</b>", parse_mode="html")




    #  UZ PRODUCTS CALLBACK  #

    if call.data == "uz_product_1":
        with open("PHOTOS/Products/Product 1.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  68,770  UZS"
                                                        "\nHajmi (44 - 46)  -  68,770  UZS"
                                                        "\nHajmi (48 - 50)  -  68,770  UZS"
                                                        "\nHajmi (52 - 54)  -  68,770  UZS"
                                                        "\nHajmi (56 - 58)  -  68,770  UZS"
                                                        "\nHajmi (60 - 62)  -  68,770  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_2":
        with open("PHOTOS/Products/Product 2.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "(8 sm - 1,5 m)  -  14,170  UZS"
                                                        "\n(8 sm - 3 m)  -  20,670  UZS"
                                                        "\n(8 sm - 4 m)  -  21,970  UZS"
                                                        "\n(8 sm - 5 m)  -  25,870  UZS"
                                                        "\n(10 sm - 1,5 m)  -  16,770  UZS"
                                                        "\n(10 sm - 3 m)  -  20,670  UZS"
                                                        "\n(10 sm - 4 m)  -  28,870  UZS"
                                                        "\n(10 sm - 5 m)  -  31,070  UZS"
                                                        "\n(12 sm - 1,5 m)  -  15,470  UZS"
                                                        "\n(12 sm - 3 m)  -  27,170  UZS"
                                                        "\n(12 sm - 4 m)  -  29,770  UZS"
                                                        "\n(12 sm - 5 m)  -  32,370  UZS"
                                                        "\n(14 sm - 1,5 m)  -  15,470  UZS"
                                                        "\n(14 sm - 3 m)  -  27,170  UZS"
                                                        "\n(14 sm - 4 m)  -  32,370  UZS"
                                                        "\n(14 sm - 5 m)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_3":
        with open("PHOTOS/Products/Product 3.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  34,450  UZS"
                                                        "\nHajmi (44 - 46)  -  34,450  UZS"
                                                        "\nHajmi (48 - 50)  -  34,450  UZS"
                                                        "\nHajmi (52 - 54)  -  34,450  UZS"
                                                        "\nHajmi (56 - 58)  -  34,450  UZS"
                                                        "\nHajmi (60 - 62)  -  34,450  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_4":
        with open("PHOTOS/Products/Product 4.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Yosh (6 - 8)  -  31,850  UZS"
                                                        "\nYosh (9 - 11)  -  31,850  UZS"
                                                        "\nYosh (12 - 15)  -  31,850  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_5":
        with open("PHOTOS/Products/Product 5.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (37 - 40)  -  33,670  UZS"
                                                        "\nHajmi (41 - 44)  -  33,670  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_6":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (44 - 46) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (48 - 50) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (52 - 54) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (56 - 58) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (60 - 62) (yozgi)  -  34,970  UZS"
                                                        "\nHajmi (40 - 42)  -  34,970  UZS"
                                                        "\nHajmi (44 - 46)  -  34,970  UZS"
                                                        "\nHajmi (48 - 50)  -  34,970  UZS"
                                                        "\nHajmi (52 - 54)  -  34,970  UZS"
                                                        "\nHajmi (56 - 58)  -  34,970  UZS"
                                                        "\nHajmi (60 - 62)  -  34,970  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_7":
        with open("PHOTOS/Products/Product 6.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  34,970  UZS"
                                                        "\nHajmi (44 - 46)  -  34,970  UZS"
                                                        "\nHajmi (48 - 50)  -  34,970  UZS"
                                                        "\nHajmi (52 - 54)  -  34,970  UZS"
                                                        "\nHajmi (56 - 58)  -  34,970  UZS"
                                                        "\nHajmi (60 - 62)  -  34,970  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_8":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (6 - 8 yosh) (bolalar uchun)  -  75,270  UZS"
                                                        "\nHajmi (9 - 11 yosh) (bolalar uchun)  -  75,270  UZS"
                                                        "\nHajmi (12 - 15 yosh) (bolalar uchun)  -  75,270  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_18":
        with open("PHOTOS/Products/Product 7.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "\nHajmi (40 - 42) (kattalar uchun)  -  94,770  UZS"
                                                        "\nHajmi (44 - 46) (kattalar uchun)  -  94,770  UZS"
                                                        "\nHajmi (48 - 50) (kattalar uchun)  -  94,770  UZS"
                                                        "\nHajmi (52 - 54) (kattalar uchun)  -  94,770  UZS"
                                                        "\nHajmi (56 - 58) (kattalar uchun)  -  94,770  UZS"
                                                        "\nHajmi (60 - 62) (kattalar uchun)  -  94,770  UZS"
                                                        "</b>", parse_mode = 'html', reply_markup = Russian_Inline_Buttons.order_product_inline)


    if call.data == "uz_product_9":
        with open("PHOTOS/Products/Product 8.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  44,070  UZS"
                                                        "\nHajmi (44 - 46)  -  44,070  UZS"
                                                        "\nHajmi (48 - 50)  -  44,070  UZS"
                                                        "\nHajmi (52 - 54)  -  44,070  UZS"
                                                        "\nHajmi (56 - 58)  -  44,070  UZS"
                                                        "\nHajmi (60 - 62)  -  44,070  UZS"
                                                        "\nHajmi (40 - 42) (yozgi)  -  37,570  UZS"
                                                        "\nHajmi (44 - 46) (yozgi)  -  37,570  UZS"
                                                        "\nHajmi (48 - 50) (yozgi)  -  37,570  UZS"
                                                        "\nHajmi (52 - 54) (yozgi)  -  37,570  UZS"
                                                        "\nHajmi (56 - 58) (yozgi)  -  37,570  UZS"
                                                        "\nHajmi (60 - 62) (yozgi)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_10":
        with open("PHOTOS/Products/Product 9.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Yosh (6 - 8)  -  42,900  UZS"
                                                        "\nYosh (9 - 11)  -  42,900  UZS"
                                                        "\nYosh (12 - 15)  -  42,900  UZS"
                                                        "\nYosh (6 - 8) (yozgi)  -  36,400  UZS"
                                                        "\nYosh (9 - 11) (yozgi)  -  36,400  UZS"
                                                        "\nYosh (12 - 15) (yozgi)  -  36,400  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_11":
        with open("PHOTOS/Products/Product 10.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  59,150  UZS"
                                                        "\nHajmi (44 - 46)  -  59,150  UZS"
                                                        "\nHajmi (48 - 50)  -  59,150  UZS"
                                                        "\nHajmi (52 - 54)  -  59,150  UZS"
                                                        "\nHajmi (56 - 58)  -  59,150  UZS"
                                                        "\nHajmi (60 - 62)  -  59,150  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_12":
        with open("PHOTOS/Products/Product 11.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  66,170  UZS"
                                                        "\nHajmi (44 - 46)  -  66,170  UZS"
                                                        "\nHajmi (48 - 50)  -  66,170  UZS"
                                                        "\nHajmi (52 - 54)  -  66,170  UZS"
                                                        "\nHajmi (56 - 58)  -  66,170  UZS"
                                                        "\nHajmi (60 - 62)  -  66,170  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_13":
        with open("PHOTOS/Products/Product 12.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  37,570  UZS"
                                                        "\nHajmi (44 - 46)  -  37,570  UZS"
                                                        "\nHajmi (48 - 50)  -  37,570  UZS"
                                                        "\nHajmi (52 - 54)  -  37,570  UZS"
                                                        "\nHajmi (56 - 58)  -  37,570  UZS"
                                                        "\nHajmi (60 - 62)  -  37,570  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_14":
        with open("PHOTOS/Products/Product 13.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  71,370  UZS"
                                                        "\nHajmi (44 - 46)  -  71,370  UZS"
                                                        "\nHajmi (48 - 50)  -  71,370  UZS"
                                                        "\nHajmi (52 - 54)  -  71,370  UZS"
                                                        "\nHajmi (56 - 58)  -  71,370  UZS"
                                                        "\nHajmi (60 - 62)  -  71,370  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_15":
        with open("PHOTOS/Products/Product 16.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  71,370  UZS"
                                                        "\nHajmi (44 - 46)  -  71,370  UZS"
                                                        "\nHajmi (48 - 50)  -  71,370  UZS"
                                                        "\nHajmi (52 - 54)  -  71,370  UZS"
                                                        "\nHajmi (56 - 58)  -  71,370  UZS"
                                                        "\nHajmi (60 - 62)  -  71,370  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_16":
        with open("PHOTOS/Products/Product 17.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  27,170  UZS"
                                                        "\nHajmi (44 - 46)  -  27,170  UZS"
                                                        "\nHajmi (48 - 50)  -  27,170  UZS"
                                                        "\nHajmi (52 - 54)  -  27,170  UZS"
                                                        "\nHajmi (56 - 58)  -  27,170  UZS"
                                                        "\nHajmi (60 - 62)  -  27,170  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_17":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42) (yozgi)  -  20,670  UZS"
                                                        "\nHajmi (44 - 46) (yozgi)  -  20,670  UZS"
                                                        "\nHajmi (48 - 50) (yozgi)  -  20,670  UZS"
                                                        "\nHajmi (52 - 54) (yozgi)  -  20,670  UZS"
                                                        "\nHajmi (56 - 58) (yozgi)  -  20,670  UZS"
                                                        "\nHajmi (60 - 62) (yozgi)  -  20,670  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_product_18":
        with open("PHOTOS/Products/Product 18.png", "rb") as photo:
            bot.send_photo(call.message.chat.id, photo, "<b>"
                                                        "Hajmi (40 - 42)  -  26,900  UZS"
                                                        "\nHajmi (44 - 46)  -  26,900  UZS"
                                                        "\nHajmi (48 - 50)  -  26,900  UZS"
                                                        "\nHajmi (52 - 54)  -  26,900  UZS"
                                                        "\nHajmi (56 - 58)  -  26,900  UZS"
                                                        "\nHajmi (60 - 62)  -  26,900  UZS"
                                                        "</b>", parse_mode='html', reply_markup=Russian_Inline_Buttons.order_product_inline)

    if call.data == "uz_order_product":
        bot.send_message(call.message.chat.id, "<b>"
                                               "Kontakt:  +998907043434"
                                               "\nKontakt:  +998997719888"
                                               "</b>", parse_mode="html")







if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            print(e)
            time.sleep(5)
            continue



