# -*- coding: utf-8 -*-
"""基于w2v结果算doc相似度"""

import sys

import numpy as np
from numpy import ndarray
from gensim.models import Word2Vec
from data_loader import load_titles
from conf import w2v_model_pt as model_pt
from common.util import tokenize
from match.matcher import DocMatcher
from match.doc import Doc
from typing import List

"""
word2vec based doc match
"""


class W2vMatcher(DocMatcher):

  def __init__(self, model: Word2Vec, corpus: List[Doc]):
    self.model = model
    self.corpus = corpus
    docs = [d.raw for d in corpus]
    self.corpus_mat = self.corpus2mat(docs)
    print("corpus_mat.shape=" + str(self.corpus_mat.shape))

  @staticmethod
  def init(model_pt: str, corpus: List[Doc]):
    model = Word2Vec.load(model_pt)
    wv = model.wv
    print("w2v model, voca size=%d, vector size=%d" % (len(wv.vocab), wv.vector_size))
    return W2vMatcher(model, corpus)

  def doc2vec(self, doc: str) -> ndarray:
    words = tokenize(doc)
    wv = self.model.wv
    sum_vec = np.sum(np.array([wv.get_vector(w) for w in words if w in wv]), axis=0)
    vec = sum_vec / np.linalg.norm(sum_vec, 2)
    return vec

  def corpus2mat(self, docs: List[str]) -> ndarray:
    return np.stack([self.doc2vec(d) for d in docs], axis=0)

  def match(self, doc: str, topN: int) -> (List[Doc], List[float]):
    doc_vec = self.doc2vec(doc)
    sims = np.dot(self.corpus_mat, doc_vec)
    dids = np.argsort(-sims)[:topN]
    return map(lambda did: self.corpus[did], dids), sims


if __name__ == '__main__':
  topN = 10
  corpus = load_titles()
  matcher = W2vMatcher.init(model_pt, corpus)

  print("input doc:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    doc = line.strip()
    print("query=" + doc)
    matched_docs, sims = matcher.match(doc, topN)
    for i, matched_doc in enumerate(matched_docs):
      print(str(matched_doc) + ", sim=%f" % sims[i])

    print("input doc:", end="", flush=True)
    line = sys.stdin.readline()
