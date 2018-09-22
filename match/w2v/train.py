#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import Word2Vec
from conf import w2v_model_pt as model_pt
from data_loader import titles
import sys

from common.util import tokenize

"""word2vec training
"""

def train(docs):
  docs = [tokenize(doc) for doc in docs]
  model = Word2Vec(docs, size=100, window=5, min_count=2, workers=4)
  model.save(model_pt)
  print("save model:" + model_pt)
  return model

def inspect(word):
  kvs = model.wv.similar_by_word(word)
  print("\n------" + word + "----------")
  for k, v in kvs:
    print("%s\t%f" % (k, v))

if __name__ == '__main__':
  model = train(titles)
  print("input word:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    word = line.strip()
    inspect(word)
    print("input word:", end="", flush=True)
    line = sys.stdin.readline()
