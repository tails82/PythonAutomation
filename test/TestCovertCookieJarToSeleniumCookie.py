__author__ = 'Tails'

import urllib2
import cookielib
from selenium import webdriver

seleniumCookieElementMap = {
    'name': 'name',
    'value': 'value',
    'path': 'path',
    'secure': 'secure',
    'expires': 'expiry'
}


def saveCookieInMemory(url):
    cookieJar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(handler)
    opener.open(url)

    return cookieJar


def converCookieJarFormatToSeleniumCookieFormat(cookie):
    dicSeleniumCookie = dict()

    # Based on observation of the WebDriver cookies, I think this is how the
    # cookielib cookie attributes should me mapped for the domain attribute
    # of a cookie.
    if getattr(cookie, 'domain_initial_dot'):
        dicSeleniumCookie['domain'] = '.' + getattr(cookie, 'domain')
    else:
        dicSeleniumCookie['domain'] = getattr(cookie, 'domain')
    for key in seleniumCookieElementMap.keys():
        val = getattr(cookie, key)
        dicSeleniumCookie[seleniumCookieElementMap[key]] = val
    return dicSeleniumCookie


if __name__ == "__main__":
    # driver = webdriver.Firefox()
    # driver.get("http://www.englishtown.com/login.aspx")
    # cookies = driver.get_cookies();
    # for cookie in cookies:
    #     print cookie

    cookieJar = saveCookieInMemory("http://www.englishtown.com/login.aspx")
    for cookie in cookieJar:
        # print cookie
        print converCookieJarFormatToSeleniumCookieFormat(cookie)
