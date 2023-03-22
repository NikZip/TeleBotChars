import telebot
import config
from utils import CurrencyAPI, keyboard_delete_selected, keyboard_from_dict


class CharsBot:
    def __init__(self):

        self.bot = telebot.TeleBot(config.BOT_TOKEN)
        self._base_curr = None

        @self.bot.message_handler(commands=['start'])
        def welcome_command(message):

            self.bot.send_sticker(message.chat.id, config.welcome_sticker)

            self.bot.send_message(message.chat.id, f"""
            Welcome {message.from_user.first_name}! I'm Chars.
            I can convert currency for lazy you :)
            Available commands:\n
            /exchange - Press it to get started.
            /help - Press if you need help.
            """)

        @self.bot.message_handler(commands=['help'])
        def help_command(message):
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton(
                'Message the developer',
                url='telegram.me/TheNikZip'))

            self.bot.send_message(message.chat.id, """
            1)To receive a list of available currencies press /exchange.
            2)Click on the currency you wanna convert from.
            3)Click on the currency you wanna convert to.
            """, reply_markup=keyboard)

        @self.bot.message_handler(commands=['exchange'])
        def exchange_command(message):

            keyboard = keyboard_from_dict(config.currency_base)
            self.bot.send_message(message.chat.id, 'Choice currency that you wanna convert from', reply_markup=keyboard)

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith('base-'))
        def base_cur_callback(query):

            self._set_base_currency(query.data[5:])

            d = keyboard_delete_selected(config.currency_to, self._base_curr)
            keyboard = keyboard_from_dict(d)

            self.bot.edit_message_text(chat_id=query.message.chat.id,
                                       text='Choice currency that you wanna convert to',
                                       message_id=query.message.message_id,
                                       reply_markup=keyboard)

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith('to-'))
        def to_curr_callback(query):
            self.bot.edit_message_reply_markup(chat_id=query.message.chat.id,
                                               message_id=query.message.message_id,
                                               reply_markup=[])
            self._get_exchange_callback(query)

    def _set_base_currency(self, currency):
        self._base_curr = currency

    def start(self):
        self.bot.polling(none_stop=True)

    def _get_exchange_callback(self, query):
        self.bot.answer_callback_query(query.id)
        self._send_exchange_result(query.message, query.data[3:])

    def _send_exchange_result(self, message, exc_curr):
        self.bot.send_chat_action(message.chat.id, 'typing')
        try:
            curr = CurrencyAPI.get_exchange(self._base_curr, exc_curr, 1)

            self.bot.send_message(
                message.chat.id, """
                From: {}
                To: {}
                Exchange rate: {}
                """.format(self._base_curr, exc_curr, curr.get('result'))
            )
        except Exception as e:
            self.bot.send_message(
                message.chat.id, "Oops Error: {}".format(e)
            )

