#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import datetime,time
import pytz
from prettyTime import isTimePretty
import telebot,inits

bot = telebot.TeleBot(inits.tel_token)


@bot.message_handler()
def send_welcome(message):
    print message
    bot.forward_message(inits.my_id,message.chat.id,message.message_id)


while(True):
    try:
        bot.polling()

        d_aware = pytz.timezone("Etc/GMT").localize(datetime.datetime.now())
        print d_aware.astimezone(pytz.timezone("Asia/Tehran")).time()
        timeIsPretty = isTimePretty(d_aware.astimezone(pytz.timezone("Asia/Tehran")).time())
        print timeIsPretty
        if(timeIsPretty):
            time.sleep(1)
            bot.send_message(inits.chat_id,"ساعتو")
    except KeyboardInterrupt:
        break
    except:
        pass
    time.sleep(5)
