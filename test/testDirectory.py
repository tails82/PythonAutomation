__author__ = 'tails.zhang'

import sys
import os

print os.getcwd()
print sys.path[0]
print __file__
print os.path
print os.path.realpath(__file__)
# the real current file directory
print os.path.split(os.path.realpath(__file__))[0]