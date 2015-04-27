#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2015-04-14

import numpy as np
import sys

def typoglycemia(s):

  def randSwitch(word):
    chars = list(word)
    randChars = [chars.pop(0)]
    lastChar = chars.pop()
    while len(chars) > 0:
      randChars.append(chars.pop(np.random.randint(len(chars))))
    randChars.append(lastChar)
    return ''.join(randChars)

  words = s.split(' ')
  typos = []
  for word in words:
    if len(word) > 4:
      typos.append(randSwitch(word))
    else:
      typos.append(word)

  return ' '.join(typos)


if __name__ == '__main__':
  print "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
  print typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
