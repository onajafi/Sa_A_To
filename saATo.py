import datetime,time
import pytz
from prettyTime import isTimePretty
import telebot,inits

bot = telebot.TeleBot(inits.tel_token)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print message
    bot.reply_to(message, "Howdy, how are you doing?")


while(True):
    bot.polling()
    d_aware = pytz.timezone("Etc/GMT").localize(datetime.datetime.now())
    print d_aware.astimezone(pytz.timezone("Asia/Tehran")).time()
    print isTimePretty(d_aware.astimezone(pytz.timezone("Asia/Tehran")).time())
    time.sleep(1)
