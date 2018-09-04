import datetime,time
import pytz
from prettyTime import isTimePretty
utc_now = pytz.utc.localize(datetime.datetime.utcnow())

# print utc_now
# print utc_now.astimezone(pytz.timezone("Asia/Tehran"))
d_aware = pytz.timezone("Etc/GMT").localize(datetime.datetime.now())

while(True):
    print d_aware.astimezone(pytz.timezone("Asia/Tehran")).time()
    print isTimePretty(d_aware.astimezone(pytz.timezone("Asia/Tehran")).time())
    time.sleep(30)
