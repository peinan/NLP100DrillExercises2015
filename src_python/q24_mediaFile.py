#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-28

import re
import pickle as pkl

def extractMediaFile(string):
  reMedia = re.compile(ur'\[\[ファイル:(.+\.(jpg|png|gif|jpeg|mp4|mpeg|mkv))\|.*')
  for line in string.splitlines():
    
