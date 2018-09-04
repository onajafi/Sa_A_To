import datetime,time
import pytz
from prettyTime import isTimePretty
import telebot,inits

bot = telebot.TeleBot(inits.tel_token)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print message
    bot.send_message(inits.chat_id, "Salam")


while(True):
    bot.polling()
    d_aware = pytz.timezone("Etc/GMT").localize(datetime.datetime.now())
    print d_aware.astimezone(pytz.timezone("Asia/Tehran")).time()
    print isTimePretty(d_aware.astimezone(pytz.timezone("Asia/Tehran")).time())
    time.sleep(1)
