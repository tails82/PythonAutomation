__author__ = 'Tails'

import os
import urllib2
import cookielib

# save cookies in memory
def saveCookieInMemory(url):
    cookieJar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(handler)
    opener.open(url)

    return cookieJar

# save cookie in file
def saveCookieToLWPCompatableFile(url, fileName):
    fileCookieJar = cookielib.LWPCookieJar(fileName)
    #fileCookieJar.save()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(fileCookieJar))
    opener.open(url)
    fileCookieJar.save()

def saveCookieToMozillarCompatableFile(url, fileName):
    fileCookieJar = cookielib.MozillaCookieJar(fileName)
    #fileCookieJar.save()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(fileCookieJar))
    opener.open(url)
    fileCookieJar.save()

# read cookie from file as libwww-perl Set-Cookie3 compatale cookie
def readLWPCookieFromFile(fileName):
    fileCookieJar = cookielib.LWPCookieJar()
    fileCookieJar.load(fileName)
    return fileCookieJar

# read cookie from file as Mozilla compatable cookie
def readMozillaCookieFromFile(fileName):
    mozillaFileCookieJar = cookielib.MozillaCookieJar()
    mozillaFileCookieJar.load(fileName)
    return mozillaFileCookieJar


if __name__ == '__main__':
    url = 'http://www.englishtown.com/login.aspx'
    cookieJar = saveCookieInMemory(url)
    print cookieJar
    print 'Totally ' + str(len(cookieJar)) + ' cookies'
    for cookie in cookieJar:
        print cookie.name + '=' + cookie.value

    LWPCookieFileName = os.getcwd() + os.path.sep + "LWPCookieFile.txt"
    mozillarCookieFileName = os.getcwd() + os.path.sep + "MozillarCookieFile.txt"

    print LWPCookieFileName
    saveCookieToLWPCompatableFile(url, LWPCookieFileName)
    with open(LWPCookieFileName, 'r') as f:
        for line in f:
            print line

    print mozillarCookieFileName
    saveCookieToMozillarCompatableFile(url, mozillarCookieFileName)
    with open(mozillarCookieFileName, 'r') as f:
        for line in f:
            print line

    LWPfileCookieJar = readLWPCookieFromFile(LWPCookieFileName)
    print LWPfileCookieJar
    print 'Totally ' + str(len(LWPfileCookieJar)) + ' cookies'
    for cookie in LWPfileCookieJar:
        print cookie.name + '=' + cookie.value

    mozillaFileCookieJar = readMozillaCookieFromFile(mozillarCookieFileName)
    print mozillaFileCookieJar
    print 'Totally ' + str(len(mozillaFileCookieJar)) + ' cookies'
    for cookie in mozillaFileCookieJar:
        print cookie.name + '=' + cookie.value
