#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

def joinStr01(s=u'パタトクカシーー', n=[1, 3, 5, 7]):
  return u''.join([ s[i-1] for i in n ])


if __name__ == '__main__':
  print u'パタトクカシーー ->', joinStr01()
