#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

import collections

def countStr(s='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'):
  return [ len(s.strip(',.')) for s in s.split(' ') ]


if __name__ == '__main__':
  print 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
  print countStr()
