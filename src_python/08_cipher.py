#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-14

import re, sys
alphabet = re.compile(ur'[a-z]')

def cipherEncode(s):
  encoded = ''
  for aChar in s:
    if alphabet.match(aChar):
      encoded += chr(219 - ord(aChar))
    else:
      encoded += aChar

  return encoded


if __name__ == '__main__':
  print cipherEncode(sys.argv[1])
