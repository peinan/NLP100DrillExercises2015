#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-17

import sys

def replaceTab2Space(filePath='../data/hightemp.txt'):
  for line in open(filePath):
    sys.stdout.write(line.replace('\t', ' '))


if __name__ == '__main__':
  replaceTab2Space()
