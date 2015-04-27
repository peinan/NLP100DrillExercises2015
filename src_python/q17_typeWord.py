#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

from collections import defaultdict

def typeWord(filePath, colNo=1, delimiter='\t'):
  word_count = defaultdict(int)
  for line in open(filePath):
    word_count[ line.strip().split(delimiter)[colNo - 1] ] += 1
  return len(word_count)


if __name__ == '__main__':
  print typeWord('../data/hightemp.txt')
