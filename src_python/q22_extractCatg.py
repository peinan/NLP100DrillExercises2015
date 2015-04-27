#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

import sys, re
import pickle as pkl
from collections import defaultdict
from q21_extractCatgLines import extractCategoryLines

def extractCategories(string):
  reCatg1 = re.compile(ur'.*Category:([^\|\]\}]+)')
  reCatg2 = re.compile(ur'([^\*\]\} ]+)[\]\}\n]?')
  catgs = []
  splited = string.split('|')
  # print '#', len(splited), splited
  flag = False
  for aSplited in splited:
    # print '# aSplited:', aSplited
    matched = reCatg1.match(aSplited)
    if matched:
      # print '# matched catg1:', matched.group(1)
      catgs.append(matched.group(1))
      flag = True
    elif flag == True:
      matched = reCatg2.match(aSplited)
      if matched:
        # print '# matched catg2:', matched.group(1)
        catgs.append(matched.group(1))

  return catgs


def main(pklFilePath='../data/jawiki-country.pkl'):
  catgs = defaultdict(int)
  for article in pkl.load(open(pklFilePath)):
    for catgLine in extractCategoryLines(article['text']):
      # print catgLine
      for catg in extractCategories(catgLine):
        # print '#', catg
        catgs[catg] += 1

  return catgs


if __name__ == '__main__':
  for catg, count in sorted(main().items(), key=lambda x:x[1], reverse=True):
    print count, catg
