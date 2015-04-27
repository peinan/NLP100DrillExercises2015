#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-14

def countLine(filePath):
  return sum([ 1 for line in open(filePath) ])


if __name__ == '__main__':
  print countLine('../data/hightemp.txt')
