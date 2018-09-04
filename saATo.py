# import datetime
# from datetime import tzinfo,timedelta

# print str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)


import datetime
import pytz
# "Asia/Tehran"
# America/Los_Angeles
utc_now = pytz.utc.localize(datetime.datetime.utcnow())
# print utc_now
# print utc_now.astimezone(pytz.timezone("Asia/Tehran"))
d_aware = pytz.timezone("Etc/GMT").localize(datetime.datetime.now())
print d_aware.astimezone(pytz.timezone("Asia/Tehran")).time()
