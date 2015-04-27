#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

import sys
import pickle as pkl

def extractCategoryLines(string):
  return [ line for line in string.splitlines() if 'Category' in line ]


if __name__ == '__main__':
  for article in pkl.load(open('../data/jawiki-country.pkl')):
    for catgLine in extractCategoryLines(article['text']):
      print catgLine
