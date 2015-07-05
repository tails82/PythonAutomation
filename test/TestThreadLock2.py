#coding=utf-8

from time import sleep

__author__ = 'Tails'

import threading

lock = threading.Lock()

def fun1():
    lock.acquire()
    print u'我在用，你等会儿'
    sleep(2)
    lock.release()

threads = []

t1 = threading.Thread(target=fun1)
threads.append(t1)
t2 = threading.Thread(target=fun1)
threads.append(t2)

for t in threads:
    t.start()