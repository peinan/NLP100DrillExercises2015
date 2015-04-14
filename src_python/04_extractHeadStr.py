#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

def extractHeadStr(s='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.', s1=[1, 5, 6, 7, 8, 9, 15, 16, 19]):
  words = s.split(' ')
  s2 = list(set(range(len(words)+1)) ^ set(s1))[1:]
  returnStr = {}
  for i in range(len(words)):
    if i+1 in s1: returnStr[words[i][0]] = i+1
    if i+1 in s2: returnStr[words[i][:2]] = i+1
  return returnStr


if __name__ == '__main__':
  print sorted(extractHeadStr().items(), key=lambda x: x[1])
