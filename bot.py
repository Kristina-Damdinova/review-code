import telebot
from telebot import types

from pars import Parser


class MyBot:
    pars = Parser()
    def __init__(self):
        self.bot = telebot.TeleBot('token')
        menu = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)

        # Create callback buttons
        item1 = types.KeyboardButton(text='Показать ссылку')
        item2 = types.KeyboardButton(text='Хочу переиграть')

        # Add buttons to the inline keyboard
        menu.add(item1, item2)

        @self.bot.message_handler(commands=['start'])
        def start(message):
            msg = self.bot.send_message(message.from_user.id,
                                   "Привет! Я чат-бот, который поможет тебе подобрать выкройку платья судьбы!"
                                   "Для начала введи любое целое число")
            self.bot.register_next_step_handler(msg, choice)


        def choice(message):
            try:
                number = int(message.text) % 12 #чтобы работало с 44 страницами использовать %170
                self.bot.send_message(message.chat.id,self.pars.data_dresses.get_information_by_model(number))
                self.bot.send_message(message.chat.id, "Выберите действие:", reply_markup=menu)

                self.bot.register_next_step_handler(message, get_url, number)
            except ValueError:
                self.bot.send_message(message.chat.id, 'Введи ЦЕЛОЕ число!')
                self.bot.register_next_step_handler(message, choice)

        @self.bot.message_handler(content_types=['text'])
        def get_url(message, number):
            if message.text == 'Показать ссылку':
                self.bot.send_message(message.chat.id, self.pars.data_dresses.get_models_url(number))
            else:
                self.bot.send_message(message.chat.id, 'Хорошо) введи целое число')
                self.bot.register_next_step_handler(message, choice)

        self.bot.polling(none_stop=True, interval=0)

hw_bot = MyBot()
