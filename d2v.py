#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from conf import titles_pt, d2v_model_pt
from util import tokenize
import sys

"""Module documentation 
"""


def load_docs():
  return [l.strip() for l in open(titles_pt)]

def load_titles():
  rows = csv.reader(open(titles_pt, encoding="utf8"))
  docs = []
  for row in rows:
    doc = row[2]
    docs.append(tokenize(doc))
  print("n(doc)=", len(docs))
  return docs


def train(docs, model_pt):
  docs = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs)]
  model = Doc2Vec(docs, vector_size=100, window=5, min_count=2, workers=4)
  #model.save(model_pt)
  print("save model:" + model_pt)
  return model


def inspect(doc_id):
  dv = model.docvecs
  kvs = dv.most_similar(positive=[doc_id])
  print("\n------" + docs[doc_id] + "----------")
  for k, v in kvs:
    print("%s\t%f" % (docs[k].strip(), v))

if __name__ == '__main__':
  docs = load_docs()
  titles = load_titles()
  model = train(titles, d2v_model_pt)
  print("input doc_id:", end="", flush=True)
  line = sys.stdin.readline()
  while line:
    doc_id = int(line.strip())
    inspect(doc_id)
    print("input doc_id:", end="", flush=True)
    line = sys.stdin.readline()
