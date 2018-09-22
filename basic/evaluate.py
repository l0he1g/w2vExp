#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""doc matching evaluation
input:
"""
from basic.doc import Doc
from basic.matcher import DocMatcher


def eval(docs: list[Doc], matcher: DocMatcher, topN: Int) -> float:
  """
  compute the accuracy of a matcher
  :param docs: evaluate corpus
  :param matcher: doc matcher
  :param topN: topN candidates
  :return: accuracy
  """
  n_all = len(docs)
  n_right = 0

  for doc in docs:
    matched_docs = matcher.match(doc, topN)
    for matched_doc in matched_docs:
      if matched_doc.standard == doc.standard:
        n_right += 1
        break

  accuracy = n_right / (n_all + 1e-10)
  print("top%d accuracy = %d/%d = %f" % (topN, n_right, n_all, accuracy))
  return accuracy
