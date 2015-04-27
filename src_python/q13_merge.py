#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

def mergeCols(col1FilePath, col2FilePath):
  col1 = open(col1FilePath).readlines()
  col2 = open(col2FilePath).readlines()
  return ''.join([ '\t'.join([c1.strip(), c2]) for c1, c2 in zip(col1, col2) ])


if __name__ == '__main__':
  import sys
  sys.stdout.write(mergeCols('col1.txt', 'col2.txt'))
