#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-27

import gzip, json, sys
import pickle as pk

if __name__ == '__main__':
  # load gzipped json file: '../data/jawiki-country.json.gz'
  lines_json = [ json.loads(line) for line in gzip.open(sys.argv[1]) ]
  pk.dump(lines_json, open(sys.argv[2], 'w'))
