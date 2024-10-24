import telebot
import random
from telebot import types
import requests
from config import TOKEN, questions, animals, user_answers, ADMIN_ID, user_states

bot = telebot.TeleBot(TOKEN)


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
    markup.add(types.KeyboardButton("Написать отзыв о боте"))
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


@bot.message_handler(func=lambda message: message.text == "Написать отзыв о боте")
def start_feedback(message):
    user_states[message.from_user.id] = 'waiting_for_feedback'
    bot.reply_to(message, "Пожалуйста, напишите ваш отзыв о боте:")


@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'waiting_for_feedback')
def process_feedback(message):
    feedback = message.text
    user_id = message.from_user.id
    username = message.from_user.username

    # Отправка отзыва администратору
    bot.send_message(ADMIN_ID, f"Новый отзыв от @{username} (ID: {user_id}):\n\n{feedback}")

    bot.reply_to(message, "Спасибо за ваш отзыв! Мы ценим ваше мнение.")

    # Сбрасываем состояние пользователя
    user_states.pop(message.from_user.id, None)

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
