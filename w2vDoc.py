# -*- coding: utf-8 -*-
"""基于w2v结果算doc相似度"""

from gensim.models import Word2Vec
from conf import titles_pt, w2v_model_pt as model_pt
from util import ngram_tokenize, tokenize
import numpy as np
import sys


def doc2vec(doc):
  ws = tokenize(doc)
  return np.sum(np.array([model.wv.get_vector(w) for w in ws if w in model.wv]), axis=0)


if __name__ == '__main__':
  model = Word2Vec.load(model_pt)
  print("input doc:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    doc = line.strip()
    dv = doc2vec(doc)
    print(dv)
    print("input doc:", end="", flush=True)
    line = sys.stdin.readline()
