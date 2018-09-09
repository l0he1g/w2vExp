#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from gensim.models import Word2Vec
from conf import titles_pt, w2v_model_pt as model_pt
from util import tokenize
import sys
from nltk.util import ngrams
"""Module documentation 
"""

def load_titles():
  rows = csv.reader(open(titles_pt, encoding="utf8"))
  docs = []
  for row in rows:
    doc = row[2]
    chars = tokenize(doc)
    bigrams = ngrams(chars, 2, pad_left=True, left_pad_symbol="^",
                     pad_right=True, right_pad_symbol="$")
    bigrams = ["%s%s" % (c1, c2) for c1, c2 in bigrams]
    docs.append(bigrams)
  return docs

def train(docs):
  model = Word2Vec(docs, size=100, window=5, min_count=2, workers=4)
  #model.save(model_pt)
  print("save model:" + model_pt)
  return model

def inspect(word):
  kvs = model.wv.similar_by_word(word)
  print("\n------" + word + "----------")
  for k, v in kvs:
    print("%s\t%f" % (k, v))

if __name__ == '__main__':
  docs = load_titles()
  model = train(docs)
  print("input word:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    word = line.strip()
    inspect(word)
    print("input word:", end="", flush=True)
    line = sys.stdin.readline()
