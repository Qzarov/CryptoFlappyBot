import telebot
from flask import Flask, request
import requests

import config

bot = telebot.TeleBot(config.TOKEN_FLAPPY)
app = Flask(__name__)

user_chat_id = 726356323


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/auth', methods=['GET'])
def get_auth_token():
    # print(request.json)
    bot.send_message(user_chat_id, text=f"{request.json}")
    print(request.json)


@bot.message_handler(commands=['start'])
def c_start(message):
    bot.send_message(message.chat.id, text=f"Слушаю, кожаный")


@bot.message_handler(commands=['account'])
def c_account(message):
    url = "https://tonapi.io/v1/blockchain/getAccount?"  # + "account=" + config.WALLET

    headers = {
        "Authorization": "Bearer " + config.CLIENT_KEY
    }

    params = {
        "account": config.WALLET
    }

    response = requests.request("GET", url, headers=headers, params=params).json()
    balance = response["balance"] / 1000000000
    status: str = response["status"]
    bot.send_message(message.chat.id, text=f"Твой баланс, нищеброд: {balance} TON")
    bot.send_message(message.chat.id, text=f"Твой акк, бомжара: {status}")


@bot.message_handler(commands=['help'])
def c_help(message):
    pass


@bot.message_handler(commands=['auth'])
def c_auth(message):
    url = "https://tonapi.io/login?"

    headers = {
        'Authorization': 'Bearer ' + config.CLIENT_KEY
    }

    params = {
        "return_url": "http://" + config.MY_IP + ":" + str(config.PORT) + "/auth"
        # "return_url": "http://" + "127.0.0.1" + ":5000/auth"
    }

    # bot.send_message(message.chat.id, text=f'Перейди по ссылке: {auth_url}')
    # response = requests.request("GET", url, headers=headers, params=params)
    response = requests.get(url, params=params)
    bot.send_message(message.chat.id, text=f'Мой ответ тебе: {response.url}')
    # print(response.text)


bot.polling(none_stop=True)
if __name__ == '__main__':
    app.run(port=config.PORT, debug=True)
