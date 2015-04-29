#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-28

import re
import pickle as pkl

def extractSectionStructure(string):
  reSection = re.compile(ur'^={1,} (.*) ={1,}')
  structure = []
  for line in string.splitlines():
    matched = reSection.match(line)
    if matched:
      level = len(line.split(' ')[0]) - 1
      content = matched.group(1)
      structure.append((content, level))

  return structure


if __name__ == '__main__':
  for article in pkl.load(open('../data/jawiki-country.pkl')):
    print article['title']
    structure = extractSectionStructure(article['text'])
    for element in structure:
      print '#'*element[1],
      print element[0]
    print
  # jawiki = pkl.load(open('../data/jawiki-country.pkl'))
  # print extractSectionStructure(jawiki[0]['text'])
