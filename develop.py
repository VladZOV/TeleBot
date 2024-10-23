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
        "options": ["Мясо", "Фрукты", "Рыба"]
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
        "image_url": "lick"
    },
    "Панда": {
        "description": "Милый и неуклюжий любитель бамбука",
        "image_url": "lick"
    },
    "Орел": {
        "description": "Величественная птица, символ свободы",
        "image_url": "lick"
    },
    "Амурский тигр": {
        "description": "Властелин тайги, грациозный и могучий хищник Дальнего Востока",
        "image_url": "lick"
    },
    "Белый медведь": {
        "description": "Хозяин Арктики, символ могущества и выносливости северной природы",
        "image_url": "lick"
    },
    "Снежный барс": {
        "description": "Хранитель заснеженных вершин, легендарный дух горных хребтов",
        "image_url": "lick"
    },
    "Суррикат": {
        "description": "Часовой саванны, мастер командной работы и взаимовыручки",
        "image_url": "lick"
    },
    "Морской конек": {
        "description": "Рыцарь коралловых рифов, символ верности и отцовской заботы",
        "image_url": "lick"
    },
    "Леопард": {
        "description": "Пятнистый охотник, символ ловкости и скрытности",
        "image_url": "lick"
    }

    # Добавьте больше животных здесь
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Начать викторину")
    markup.add(item)
    bot.reply_to(message, "Добро пожаловать! Готовы узнать свое тотемное животное?", reply_markup=markup)

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
    # Простая логика выбора животного (можно усложнить)
    animal = random.choice(list(animals.keys()))
    result = f"Ваше тотемное животное: {animal}\n{animals[animal]['description']}\n\nХотите узнать больше о программе опеки?"
    try:
        image = requests.get(animals[animal]["image_url"])
        if image.status_code == 200:
            bot.send_photo(chat_id, image.content, caption=result)
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
    bot.send_message(message.chat.id, "Контакты сотрудника: @zoo_employee")
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

# Функция для запуска бота
def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()