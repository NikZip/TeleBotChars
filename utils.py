import requests
import config

import telebot
from copy import deepcopy
from telebot import types


def keyboard_from_dict(d):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for key, value in d.items():
        keyboard.row(types.InlineKeyboardButton(text=key, callback_data=value))
    return keyboard


def keyboard_delete_selected(d, selected):
    _d = deepcopy(d)
    _d.pop(selected)
    return _d


class CurrencyAPI:

    @staticmethod
    def get_exchange(convert_from, convert_to, amount):
        try:
            response = requests.request("GET", config.API_URL.format(
                from_curr=convert_from,
                to_curr=convert_to,
                amount=amount
            ), headers=config.API_TOKEN)
            response.raise_for_status()

            if response.json().get('success') is True:
                return response.json()
            else:
                raise CurrencyApiError(response.json().get('error'))

        except requests.exceptions.HTTPError as e:
            return e


class CurrencyApiError(Exception):

    def __init__(self, error):
        self.code = error.get('code')
        self.type = error.get('type')

    def __str__(self):
        return """
        Error code: {}
        Error Message: {}
        """.format(self.code, self.type)
