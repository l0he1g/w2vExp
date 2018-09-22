#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from nltk.util import ngrams


def tokenize(text):
  """
  :return list of tokens
  """
  regex = r"[\u4e00-\ufaff]|[0-9_a-zA-Z\-]+\'*[a-z]*"
  matches = re.findall(regex, text, re.UNICODE)
  return matches


def ngram_tokenize(text, N):
  """
  :return list of tokens
  """
  chars = tokenize(text)
  tokens = ngrams(chars, N, pad_left=True, left_pad_symbol="^",
                  pad_right=True, right_pad_symbol="$")
  tokens = [",".join(t) for t in tokens]
  return tokens
