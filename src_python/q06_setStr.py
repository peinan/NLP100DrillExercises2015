#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

from q05_ngram import ngram

if __name__ == '__main__':
  x = 'paraparaparadise'
  y = 'paragraph'
  X = [ ''.join(aTuple) for aTuple in ngram(x, mode='s') ]
  Y = [ ''.join(aTuple) for aTuple in ngram(y, mode='s') ]

  print 'X:', X
  print 'Y:', Y

  union = list(set(X) | set(Y))
  intersection = list(set(X) ^ set(Y))
  difference = list(set(X) & set(Y))

  print 'union       =', union
  print 'itersection =', intersection
  print 'difference  =', difference

  print '"se" in X? ->', 'se' in X
  print '"se" in Y? ->', 'se' in Y
