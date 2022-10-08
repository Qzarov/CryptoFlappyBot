import telebot
from flask import request
import requests

import config

bot = telebot.TeleBot(config.TOKEN_FLAPPY)


@bot.message_handler(commands=['start'])
def c_start(message):
    url = "https://tonapi.io/v1/blockchain/getAccount?" + "account=" + config.WALLET

    response = requests.request("GET", url).json()
    balance = response["balance"] / 1000000000
    status: str = response["status"]
    bot.send_message(message.chat.id, text=f"Твой баланс, нищеброд: {balance} TON")
    bot.send_message(message.chat.id, text=f"Твой акк, бомжара: {status}")


@bot.message_handler(commands=['help'])
def c_help(message):
    pass


    # account = 'account=' + config.WALLET
    # auth_url = "https://tonapi.io/v1/blockchain/getAccount?" + account
    # redir_url = "localhost:5000/auth"

@bot.message_handler(commands=['auth'])
def c_auth(message):

    redir_url = "return_url=" + "176.59.15.120:5000/auth"

    auth_url = "https://tonapi.io/login?" + redir_url
    header = {
        'Authorization': 'Bearer ' + config.CLIENT_KEY
    }

    bot.send_message(message.chat.id, text=f'Перейди по ссылке: {auth_url}')
    # response = requests.request("GET", auth_url, headers=header)
    # bot.send_message(message.chat.id, text=f'Мой ответ тебе: {response.text}')
    # bot.send_message(message.chat.id, text=f"Твой баланс, нищеброд: {balance}")


bot.polling(none_stop=True)
