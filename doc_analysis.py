# -*- coding: utf-8 -*-
"""基于w2v结果算doc相似度"""

import sys

from gensim.models import Word2Vec
import numpy as np
from conf import w2v_model_pt as model_pt
from util import tokenize


def doc_analysis(doc):
  words = tokenize(doc)
  for w in words:
    vec = model.wv.get_vector(w)
    print("%s\t%f\t%s" % (w, np.linalg.norm(vec), str(vec)))

if __name__ == '__main__':
  topN = 10
  model = Word2Vec.load(model_pt)
  print("input doc:", end="", flush=True)
  doc = sys.stdin.readline().strip()
  while doc:
    print("doc=" + doc)
    doc_analysis(doc)
    print("input doc:", end="", flush=True)
    doc = sys.stdin.readline().strip()
    if doc:
      print("input doc:", end="", flush=True)
      doc = sys.stdin.readline().strip()

