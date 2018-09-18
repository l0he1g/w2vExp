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


def docs2vecs(docs):
  return np.stack([doc2vec(d) for d in docs], axis=0)

def most_similar(corpus_mat, vec, topN):
  N = corpus_mat.shape[0]
  print(N)
  sim_vec = np.dot(corpus_mat, vec)
  dids = np.argsort(-sim_vec)[:topN]
  for did in dids:
    print("%d\t%s\t%f" % (did, titles[did], sim_vec[did]))

if __name__ == '__main__':
  topN = 10
  model = Word2Vec.load(model_pt)
  mat = docs2vecs(titles)
  print("mat.shape=" + str(mat.shape))
  print("input doc:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    doc = line.strip()
    print("query=" + doc)
    dv = doc2vec(doc)
    most_similar(mat, dv, topN)
    print("input doc:", end="", flush=True)
    line = sys.stdin.readline()
