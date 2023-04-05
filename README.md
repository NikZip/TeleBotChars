<p align="center">
      <img src="https://telegramas.ru/wp-content/uploads/2022/01/Logo-Telegram.jpg" width="250">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Bot%20Version-v1.0-green" alt="Bot Version">
   <img src="https://img.shields.io/badge/License-MIT-brightgreen" alt="License">
</p>

# About

This is a telegram bot that uses api to receive real-time currency exchange

# Install

0. Before doing all of this you need:

+ Get bot api key from Father telegram bot [here](https://t.me/botfather) 
+ Get some currency api key. I used [Fixer API](https://fixer.io/)

1. Clone the repository or download the zip file
```
git clone https://github.com/NikZip/TeleBotChars
```
2. Rename file **`private_config_template.py`** to **`private_config.py`** and full **`BOT_TOKEN`**, **`API_TOKEN`** tokens with yours

3. Docker:

      To run bot in docker:
```
docker-compose up --build
```
4. Without Docker
```
pip install -r requirements.txt
```

# Documentation

## Config:

**`BOT_TOKEN`** - your telegram bot token

**`API_TOKEN`** - your custom API token

**`API_URL`** - custom API url

**`currency_base`** - dict of currency choicen as base

**`currency_to`** - dict of currency that your base will convert to

## Classes:

### Class **`CharsBot`** - main bot

**`CharsBot.welcome_command`** - /start command for welcome message

**`CharsBot.help_command`** - /help command for help

**`CharsBot.exchange_command`** - /exchange command to start exchange

### Handler methods

**`CharsBot.base_cur_callback`** - sets base currency on user choice 

**`CharsBot.to_curr_callback`** - deletes markup and executes functions _get_exchange_callback _send_exchange_result

### Private methods 

**`CharsBot._get_exchange_callback`** - executes function _send_exchange_result and sends currency to value

**`CharsBot._send_exchange_result`** - calling API for exchange and sending result to user

### Class **`CurrencyAPI`** - class for API handler

**`CurrencyAPI.get_exchange`** - accepts currency_from, currency_to as str and amount as int, sending request to get data, return json

## Other methods:

**`keyboard_from_dict`** - makes Telegram inline keyboard from dict

**`keyboard_delete_selected`** - makes deepcopy of dict and delete selected element, needs for deleting option that user selected

# Developers

- [NikZip](https://github.com/NikZip)

# License
The TeleBotChars is distributed under the MIT license.
