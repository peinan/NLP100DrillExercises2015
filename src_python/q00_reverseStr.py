#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

def reverseStr(s='stressed'):
  return ''.join([ aChar for aChar in s[::-1] ])


if __name__ == '__main__':
  print 'stressed ->', reverseStr()
