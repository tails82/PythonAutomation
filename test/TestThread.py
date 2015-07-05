#coding=utf-8
__author__ = 'Tails'

import threading
from time import ctime, sleep

def music(musicName):
    for i in range(2):
        print "I was listening to %s. %s" %(musicName, ctime())
        sleep(4)

def movie(movieName):
    for i in range(2):
        print "I was at the %s! %s" %(movieName, ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=movie, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        # 设置为守护线程。线程分为用户线程和守护线程。守护线程在所有用户线程执行结束后会自动结束
        t.setDaemon(True)
        t.start()

    #由于t1, t2为守护线程，而主线程是唯一的用户线程。如果主线程在t1, t2前结束，则t1, t2会自动结束。因此这里使用join，通知主线程等待t1, t2执行结束后，再往下执行
    t.join()
    print "all over %s" %ctime()