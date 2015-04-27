#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

def sortCol(filePath, colNo=3, delimiter='\t', reverse=True):
  lines = [ line.split(delimiter) for line in open(filePath) ]
  return sorted(lines, key=lambda x: x[colNo-1], reverse=reverse)


if __name__ == '__main__':
  import sys
  for line in sortCol('../data/hightemp.txt'):
    sys.stdout.write('\t'.join(line))
