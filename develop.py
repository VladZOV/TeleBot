import telebot
import random
from telebot import types
import requests

# Инициализация бота
TOKEN = '7818791643:AAHa-jxUuwv_09sxVyjREQ18SEl_TGOBkMk'
bot = telebot.TeleBot(TOKEN)

# Структура данных для хранения вопросов и ответов
questions = [

    {
        "question": "Какая у вас любимая еда?",
        "options": ["Мясо", "Фрукты/овощи", "Рыба"]
    },
    {
        "question": "Какую среду обитания вы предпочитаете?",
        "options": ["Тропические леса", "Саванны и степи", "Горы", "Водная среда"]
    },
    {
        "question": "Какой размер животного вам больше нравится?",
        "options": ["Маленький", "Средний", "Крупный", "Очень крупный"]
    },
    {
        "question": "Какой тип питания вы считаете наиболее интересным?",
        "options": ["Травоядные", "Хищники", "Всеядные", "Насекомоядные"]
    },
    {
        "question": "Какое качество вы больше всего цените в животных?",
        "options": ["Ловкость и скорость", "Силу и выносливость", "Интеллект", "Необычную внешность"]
    },
    {
        "question": "Какой образ жизни вам ближе?",
        "options": ["Дневной", "Ночной", "Сумеречный", "Смешанный"]
    },
    {
        "question": "Какой тип социального поведения вам нравится?",
        "options": ["Одиночки", "Семейные группы", "Большие стаи или стада", "Колонии"]
    },
    {
        "question": "Какая особенность животного вам кажется наиболее привлекательной?",
        "options": ["Яркая окраска", "Необычная форма тела", "Способность к маскировке", "Впечатляющие размеры"]
    }
    # Добавьте больше вопросов здесь
]

# Словарь для хранения ответов пользователей
user_answers = {}

# Животные и их характеристики
animals = {
    "Лев": {
        "description": "Царь зверей, символ силы и мужества",
        "image_url": "https://media.istockphoto.com/id/494856046/ru/фото/лев-в-высокой-траве.jpg?s=612x612&w=0&k=20&c=JI25SmQsrObTy7sZRuFJ-_ZTPZJXoPm8Sutg71BSgII="
    },
    "Панда": {
        "description": "Милый и неуклюжий любитель бамбука",
        "image_url": "https://media.istockphoto.com/id/175009379/ru/фото/большая-панда-медведь-ест-бамбук.jpg?s=612x612&w=0&k=20&c=E9TwK9lJKdhOr3ht8Tpbb5OAWua69NIyNoY6JYDHX6I="
    },
    "Орел": {
        "description": "Величественная птица, символ свободы",
        "image_url": "https://media.istockphoto.com/id/681388560/ru/фото/лысый-орел-пролетел-над-ледяными-водами.jpg?s=612x612&w=0&k=20&c=aViz7GADxq_-ByGQFg9Y-pH8cRVxPHsMhiomX4gEihQ="
    },
    "Амурский тигр": {
        "description": "Властелин тайги, грациозный и могучий хищник Дальнего Востока",
        "image_url": "https://media.istockphoto.com/id/638671828/ru/фото/медленно-гуляет-сибирский-тигр-в-снегу.jpg?s=612x612&w=0&k=20&c=4k2e0p6ry-Rt-pKAW7oDTgOwcLrlM7yBmhkuofs1vuA="
    },
    "Белый медведь": {
        "description": "Хозяин Арктики, символ могущества и выносливости северной природы",
        "image_url": "https://media.istockphoto.com/id/627066956/ru/фото/полярный-медведь.jpg?s=612x612&w=0&k=20&c=mNtkIXThVoqaYmqI70d2avw6mommkjSk4sgEW-TswXM="
    },
    "Снежный барс": {
        "description": "Хранитель заснеженных вершин, легендарный дух горных хребтов",
        "image_url": "https://media.istockphoto.com/id/186723473/ru/фото/снежный-барс-в-зимний-пейзаж.jpg?s=612x612&w=0&k=20&c=QoQyZA0Jsd76JYM05-zx1PoBtAmZgiFcPaOggNesKNw="
    },
    "Суррикат": {
        "description": "Часовой саванны, мастер командной работы и взаимовыручки",
        "image_url": "https://media.istockphoto.com/id/664727638/photo/meerkat-on-hind-legs.webp?a=1&b=1&s=612x612&w=0&k=20&c=p6w-wQAvzshWKGtii0I3wujJbnkR_00sIko72ZrryPo="
    },
    "Морской конек": {
        "description": "Рыцарь коралловых рифов, символ верности и отцовской заботы",
        "image_url": "https://media.istockphoto.com/id/94323951/photo/horse-sea.webp?a=1&b=1&s=612x612&w=0&k=20&c=XnTwJSAd9XpewEYiz4-pvNhbm44H7iYZVRocJchUyUI="
    },
    "Леопард": {
        "description": "Пятнистый охотник, символ ловкости и скрытности",
        "image_url": "https://media.istockphoto.com/id/1856545232/photo/low-angle-view-of-majestic-leopard-sleeping-on-huge-tree-branch-at-serengeti-national-park-in.webp?a=1&b=1&s=612x612&w=0&k=20&c=_GXwqtaod9F7LN3mg-H9PrAgjIxTKRib2GUQP0W_woI="
    }

    # Добавьте больше животных здесь
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Начать викторину")
    markup.add(item)
    bot.reply_to(message, "Добро пожаловать на викторину от Московского зоопарка!"
                          "\nГотовы узнать свое тотемное животное?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Начать викторину")
def start_quiz(message):
    user_answers[message.chat.id] = []
    send_question(message.chat.id, 0)

def send_question(chat_id, question_index):
    if question_index < len(questions):
        question = questions[question_index]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for option in question['options']:
            markup.add(types.KeyboardButton(option))
        bot.send_message(chat_id, question['question'], reply_markup=markup)
    else:
        send_result(chat_id)

@bot.message_handler(func=lambda message: message.chat.id in user_answers)
def handle_answer(message):
    chat_id = message.chat.id
    user_answers[chat_id].append(message.text)
    send_question(chat_id, len(user_answers[chat_id]))

def send_result(chat_id):
    # Логика выбора животного 
    def calculate_animal_score(user_answers):
        scores = {animal: 0 for animal in animals.keys()}

        # Логика подсчета баллов на основе ответов
        # Еда [0]
        if user_answers[0] == "Мясо":
            scores["Лев"] += 2
            scores["Амурский тигр"] += 2
            scores["Леопард"] += 2
            scores["Орел"] += 2
        elif user_answers[0] == "Фрукты/овощи":
            scores["Панда"] += 2
        elif user_answers[0] == "Рыба":
            scores["Белый медведь"] += 2
            scores["Морской конек"] += 2

        # Среда обитания [1]
        if user_answers[1] == "Тропические леса":
            scores["Панда"] += 2
            scores["Леопард"] += 2
        elif user_answers[1] == "Саванны и степи":
            scores["Лев"] += 2
            scores["Суррикат"] += 2
        elif user_answers[1] == "Горы":
            scores["Снежный барс"] += 2
            scores["Орел"] += 2
        elif user_answers[1] == "Водная среда":
            scores["Морской конек"] += 2
            scores["Белый медведь"] += 1

        # Размер [2]
        if user_answers[2] == "Маленький":
            scores["Суррикат"] += 2
            scores["Морской конек"] += 2
        elif user_answers[2] == "Средний":
            scores["Орел"] += 1
            scores["Леопард"] += 2
        elif user_answers[2] == "Крупный":
            scores["Амурский тигр"] += 2
            scores["Снежный барс"] += 2
        elif user_answers[2] == "Очень крупный":
            scores["Белый медведь"] += 2

        # Тип питания [3]
        if user_answers[3] == "Хищники":
            scores["Лев"] += 2
            scores["Амурский тигр"] += 2
            scores["Леопард"] += 2
            scores["Орел"] += 2
        elif user_answers[3] == "Травоядные":
            scores["Панда"] += 2

        # Качества [4]
        if user_answers[4] == "Ловкость и скорость":
            scores["Леопард"] += 2
            scores["Снежный барс"] += 2
        elif user_answers[4] == "Силу и выносливость":
            scores["Лев"] += 2
            scores["Белый медведь"] += 2
        elif user_answers[4] == "Интеллект":
            scores["Суррикат"] += 2

        # Образ жизни [5]
        if user_answers[5] == "Ночной":
            scores["Леопард"] += 1
            scores["Снежный барс"] += 1
        elif user_answers[5] == "Дневной":
            scores["Суррикат"] += 2
            scores["Панда"] += 1
            scores["Орел"] += 2

        # Социальное поведение [6]
        if user_answers[6] == "Семейные группы":
            scores["Лев"] += 2
            scores["Суррикат"] += 2
        elif user_answers[6] == "Одиночки":
            scores["Леопард"] += 2
            scores["Снежный барс"] += 2
            scores["Орел"] += 1

            # Особенности [7]
        if user_answers[7] == "Способность к маскировке":
            scores["Леопард"] += 2
            scores["Снежный барс"] += 2
        elif user_answers[7] == "Необычная форма тела":
            scores["Морской конек"] += 2
        elif user_answers[7] == "Сила и мощь":
            scores["Белый медведь"] += 2
            scores["Амурский тигр"] += 2
        elif user_answers[7] == "Социальное поведение":
            scores["Суррикат"] += 2
            scores["Лев"] += 2
        elif user_answers[7] == "Уникальный окрас":
            scores["Панда"] += 2

            # Выбираем животное с максимальным количеством баллов
        max_score = max(scores.values())
        winners = [animal for animal, score in scores.items() if score == max_score]

        # Если есть несколько победителей, выбираем случайного
        return random.choice(winners)

    animal = calculate_animal_score(user_answers[chat_id])
    result = (f"Ваше тотемное животное: {animal}\n{animals[animal]['description']}"
              f"\nПоделитесь ссылкой на викторину от нашего зоопарка с друзьями, и узнайте про их тотемное"
              f" животное: t.me/CapitalRusZooBot"
              f"\nНаш зоопарк предоставляет всем желающим, поучаствовать в программе 'Лучший друг' по опеке над вашим"
              f" 'тотемным' или любым другим животным."
              f"\n\nХотите узнать больше о программе опеки?")
    try:
        image = requests.get(animals[animal]["image_url"])
        if image.status_code == 200:
            bot.send_photo(chat_id, image.content)
        else:
            bot.send_message(chat_id, result)
            bot.send_message(chat_id, "К сожалению, не удалось загрузить изображение животного.")
    except Exception as e:
        bot.send_message(chat_id, result)
        bot.send_message(chat_id, "Произошла ошибка при загрузке изображения животного.")
        print(f"Error sending image: {e}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Узнать о программе опеки"))
    markup.add(types.KeyboardButton("Попробовать еще раз"))
    bot.send_message(chat_id, result, reply_markup=markup)
    del user_answers[chat_id]

@bot.message_handler(func=lambda message: message.text == "Узнать о программе опеки")
def about_guardianship(message):
    bot.reply_to(message, "Программа опеки позволяет вам стать опекуном животного в нашем зоопарке."
                          "Вы можете помочь в уходе за животным, обеспечении его кормом и поддержании условий обитания."
                          " Хотите узнать больше или стать опекуном?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Стать опекуном"))
    markup.add(types.KeyboardButton("Вернуться в главное меню"))
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Стать опекуном")
def become_guardian(message):
    bot.reply_to(message, "Отлично! Для того чтобы стать опекуном, пожалуйста, свяжитесь с нашим сотрудником. "
                          "Он предоставит вам всю необходимую информацию.")
    bot.send_message(message.chat.id, "Контакты сотрудника: @zoo_employee")   # Можно добавить контакты
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Вернуться в главное меню"))
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Попробовать еще раз")
def retry_quiz(message):
    start_quiz(message)

@bot.message_handler(func=lambda message: message.text == "Вернуться в главное меню")
def return_to_main_menu(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Пожалуйста, используйте кнопки меню.")


bot.polling(none_stop=True)
