#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-14

import sys

def templateStr(x, y, z):
  return u'%d時の%sは%.1f' % (x, y, z)


if __name__ == '__main__':
  print templateStr(12, u'気温', 22.4)
