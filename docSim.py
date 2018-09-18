# -*- coding: utf-8 -*-
"""基于w2v结果算doc相似度"""

import sys

import numpy as np
from gensim.models import Word2Vec
from data_loader import titles
from conf import w2v_model_pt as model_pt
from util import tokenize

def doc2vec(doc):
  words = tokenize(doc)
  sum_vec= np.sum(np.array([model.wv.get_vector(w) for w in words if w in model.wv]), axis=0)
  vec = sum_vec / np.linalg.norm(sum_vec, 2)
  return vec

def doc_sim(dv1, dv2):
  return np.dot(dv1, dv2)

if __name__ == '__main__':
  topN = 10
  model = Word2Vec.load(model_pt)
  print("input doc1:", end="", flush=True)
  doc1 = sys.stdin.readline().strip()
  if doc1:
    print("input doc2:", end="", flush=True)
    doc2 = sys.stdin.readline().strip()
  while doc1 and doc2:
    print("doc1=" + doc1)
    print("doc2=" + doc2)
    dv1 = doc2vec(doc1)
    dv2 = doc2vec(doc2)
    sim = doc_sim(dv1, dv2)
    print("sim=%f" % sim)

    print("input doc1:", end="", flush=True)
    doc1 = sys.stdin.readline().strip()
    if doc1:
      print("input doc2:", end="", flush=True)
      doc2 = sys.stdin.readline().strip()

