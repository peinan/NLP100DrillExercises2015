#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

from collections import defaultdict, OrderedDict

def freqWord(filePath, colNo=1, delimiter='\t', reverse=True):
  word_count = defaultdict(int)
  for line in open(filePath):
    word_count[ line.split('\t')[colNo-1] ] += 1
  return OrderedDict(
           sorted(word_count.items(), key=lambda x: x[1], reverse=reverse)
         )


if __name__ == '__main__':
  word_count = freqWord('../data/hightemp.txt')
  for word, count in word_count.items():
    print '%s\t%d' % (word, count)
