#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

import sys

def ngram(s, n=2, mode='w'):
  """s: the sequence, n: n of n-gram, mode: [w]ord level or [s]tring level"""

  if mode == 'w': iterList = s.strip().split(' ')
  elif mode == 's': iterList = s

  # length checking
  if n > len(s):
    print '[Error] n is larger than the sequence.'
    sys.exit(-1)

  ngrams = []

  # find ngrams
  for i in range(len(iterList)):
    grams = []
    for j in range(n):
      try:
        grams.append(iterList[i+j])
      except IndexError:
        pass
    if len(grams) == n:
      ngrams.append(tuple(grams))

  return ngrams


if __name__ == '__main__':
  s = 'I am an NLPer'
  print s
  print ngram(s)
  print ngram(s, n=3)
  print ngram(s, n=2, mode='s')
