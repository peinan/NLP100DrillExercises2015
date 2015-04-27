#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

import sys, pprint

def splitFile(filePath, n):
  fileLines = open(filePath).readlines()
  line_num = len(fileLines)
  if n > line_num:
    print 'N is larger than file lines'
    sys.exit(-1)
  block_size = line_num / n
  returnList = [ 
          [ fileLines.pop(0) for j in range(block_size) ] for i in range(n-1)
      ]
  returnList.append(fileLines)
  
  return returnList


if __name__ == '__main__':
  import sys
  splitedFile = splitFile('../data/hightemp.txt', int(sys.argv[1]))
  count = 0
  for sentList in splitedFile:
    count += 1
    for sent in sentList:
      print count, sent,
