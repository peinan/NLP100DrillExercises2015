#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

def headN(filePath, n):
  return open(filePath).readlines()[:n]


if __name__ == '__main__':
  import sys
  print ''.join(headN('../data/hightemp.txt', int(sys.argv[1])))
