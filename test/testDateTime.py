__author__ = 'Tails'

import time
import datetime

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

today = datetime.datetime.now()
date = today + datetime.timedelta(days=2)

print date - today