TOKEN = '7818791643:AAHa-jxUuwv_09sxVyjREQ18SEl_TGOBkMk'

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

# Замените на ID администратора (можно узнать через @userinfobot)
ADMIN_ID = 1888279425

# Словарь для хранения состояния пользователей
user_states = {}
