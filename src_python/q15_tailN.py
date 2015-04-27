#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

def tailN(filePath, n):
  return open(filePath).readlines()[-n:]


if __name__ == '__main__':
  import sys
  print ''.join(tailN('../data/hightemp.txt', int(sys.argv[1])))
