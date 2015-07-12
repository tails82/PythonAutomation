#coding=utf-8

__author__ = 'Tails'

import urllib
import urllib2
import httplib
import os
import gzip
import StringIO

#########################urllib##################################
#如果你不传参数，urllib/urllib2使用get请求
#如果你传参数，urllib/urllib2使用post请求

# send get request use urllib
#url = "http://www.englishtown.com/login.aspx"
url = "http://www.baidu.com/"
host = "www.englishtown.com"
param = {"username":"tails", "password":"aaa"}
queryString = urllib.urlencode(param)
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

def getWithoutParam():
    result = urllib.urlopen(url)
    html = result.read()
    #乱码问题
    #返回的内容经过压缩
    gzipped = result.headers.get('Content-Encoding')
    if gzipped:
        html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode='r')
    #html = html.decode("gb2312").encode('utf-8')  如果需要编码转换  eg.返回的是gb2312编码，转换成utf-8编码
    result.close()
    print html

def getWithParam():
    result = urllib.urlopen(url + "?" + queryString)
    print result.read()
    result.close()

# send post request use urllib
def postWithParam():
    result = urllib.urlopen(url, queryString)
    print result.read()
    result.close()

#########################urllib2##################################

# send get request use urllib2
def getWithoutParam2():
    result = urllib2.urlopen(url)
    print result.read()

def getWithParam2():
    opener = urllib2.build_opener()  #urllib2 can use build_opener() function
    result = opener.open(url)
    print result.read()
    result.close()

#urllib2 can user Request object to send request
def getWithoutParamByRequest():
    request = urllib2.Request(url=url)
    result = urllib2.urlopen(request)
    print result.read()
    result.close()

def getWithParamByRequest():
    request = urllib2.Request(url=url + '?' + queryString)
    result = urllib2.urlopen(request)
    print result.read()
    result.close()

def postWithParamByRequest():
    request = urllib2.Request(url=url, data=queryString)
    result = urllib2.urlopen(request)
    print result.read()

##################httplib###############################
def getWithoutParam3():
    httpClient = httplib.HTTPConnection(host=host, port=80, timeout=30)
    httpClient.request('GET', '/')
    response = httpClient.getresponse()
    print response.read()
    print response.status
    response.close()

def getWithParam3():
    httpClient = httplib.HTTPConnection(host=host, port=80, timeout=30)
    httpClient.request('GET', '/login.aspx' + queryString)
    response = httpClient.getresponse()
    print response.read()
    print response.status
    response.close()

def postWithoutParam3():
    httpClient = httplib.HTTPConnection(host=host, port=80, timeout=30)
    httpClient.request('POST', '/login.aspx', queryString, header)
    response = httpClient.getresponse()
    print response.read()
    print response.status
    response.close()

if __name__ == "__main__":
    getWithoutParam()
    # getWithParam()
    # postWithParam()
    # getWithoutParam2()
    # getWithParam2()
    # getWithoutParamByRequest()
    # getWithParamByRequest()
    # postWithParam()
    # getWithoutParam3()
    # getWithParam3()
    # postWithoutParam3()