__author__ = 'Tails'

import Cookie
import datetime
import random

"""
available attributes in cookie (only part of)
expires
domain
path
"""
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie['session'] = random.randint(1, 1000000000)
cookie['session']['domain'] = '.baidu.com'
cookie['session']['path'] = '/'
cookie['session']['expires'] = expiration.strftime('%a, %d-%b-%Y %H:%M:%S PST')

print "Content-type:text/plain"
print cookie.output()
print cookie
print
print "Cookie set with: " + cookie.output()
