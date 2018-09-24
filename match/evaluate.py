#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""doc matching evaluation
input:
"""
from match.doc import Doc
from match.matcher import DocMatcher
from match.w2v.w2v_match import W2vMatcher
from conf import w2v_model_pt
from data_loader import load_titles
from typing import List


def eval(docs: List[Doc], matcher: DocMatcher, topN: int) -> float:
  """
  compute the accuracy of a match
  :param docs: evaluate corpus
  :param matcher: doc match
  :param topN: topN candidates
  :return: accuracy
  """
  n_all = len(docs)
  n_right = 0

  for doc in docs:
    matched_docs, _ = matcher.match(doc.raw, topN)
    for matched_doc in matched_docs:
      if matched_doc.standard == doc.standard and matched_doc.raw != doc.raw:
        n_right += 1
        break

  accuracy = n_right / (n_all + 1e-10)
  print("top%d accuracy = %d/%d = %f" % (topN, n_right, n_all, accuracy))
  return accuracy


if __name__ == '__main__':
  topN = 1
  corpus = load_titles()
  matcher = W2vMatcher.init(w2v_model_pt, corpus)
  test_corpus = corpus[:1000]
  eval(test_corpus, matcher, 1)
