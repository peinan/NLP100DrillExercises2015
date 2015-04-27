#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

def cutCol(filePath):
  list_col1 = []
  list_col2 = []
  for line in open(filePath):
    col1, col2, _, _ = line.split('\t')
    list_col1.append(col1)
    list_col2.append(col2)
  
  return ('\n'.join(list_col1), '\n'.join(list_col2))


if __name__ == '__main__':
  import sys
  col1, col2 = cutCol('../data/hightemp.txt') 
  with open('col1.txt', 'w') as file_col1:
    file_col1.write(col1)
  with open('col2.txt', 'w') as file_col2:
    file_col2.write(col2)
