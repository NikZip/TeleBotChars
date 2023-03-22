import private_config
"""
Вставьте свои значения токенов
"""
BOT_TOKEN = private_config.BOT_TOKEN

API_TOKEN = private_config.API_TOKEN

API_URL = "https://api.apilayer.com/fixer/convert?to={to_curr}&from={from_curr}&amount={amount}"

currency_base = {
    'BTC': "base-BTC",
    'EUR': "base-EUR",
    'GBP': "base-GBP",
    'KZT': "base-KZT",
    'RUB': "base-RUB",
    'USD': "base-USD",
}

currency_to = {
    'BTC': "to-BTC",
    'EUR': "to-EUR",
    'GBP': "to-GBP",
    'KZT': "to-KZT",
    'RUB': "to-RUB",
    'USD': "to-USD",
}
welcome_sticker = open('static/sticker.webp', 'rb')
