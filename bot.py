import keralabot

from config import token
from sql.sql import *
import heroku3

bot = keralabot.bot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi I am Heroku Bot. I can help in managing your Heroku Account. \n\nFirst of all press /auth\n\n@KeralasBots")


@bot.message_handler(commands=['auth'])
def auth(message):
    bot.reply_to(message, "Now send me your Heroku API key in the format <b>#herokuapikey</b>\nExample: <code>#1583hw2728gkbdyuwo629</code>", parse_mode="HTML")

@bot.message_handler(regexp=r"^#[^\s]+")
def apikey(message):
    key = message.text[1:]
    heroku(message.from_user.id, key)
    bot.reply_to(message, "Successfully got the API key {}".format(key))

@bot.message_handler(commands=['apps'])
def apps(message):
    key = get_key(message.from_user.id)
    cloud = heroku3.from_key(key)
    app = cloud.apps()
    bot.reply_to(message, str(app))
bot.polling()
