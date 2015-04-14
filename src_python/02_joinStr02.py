#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-13

def joinStr02(s1=u'パトカー', s2=u'タクシー'):
  return u''.join([ u''.join(s) for s in zip(s1, s2) ])


if __name__ == '__main__':
  print u'パトカー + タクシー ->', joinStr02()
