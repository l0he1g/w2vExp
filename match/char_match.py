#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""基于字的匹配
"""
import os
import sys
from typing import Set, List

from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh.analysis import RegexAnalyzer
from whoosh import scoring

from data_loader import load_titles
from match.doc import Doc
from match.matcher import DocMatcher
from tqdm import tqdm


class CharMatcher(DocMatcher):

  def __init__(self, corpus: List[Doc], stop_words: Set[str] = set(), rebuild=False):
    self.corpus = corpus
    self.stop_words = stop_words
    self.index_dir = "whoosh_index"
    self.index = self._build_index(rebuild)

  def _build_index(self, rebuild: bool):
    if not rebuild and os.path.exists(self.index_dir):
      print("read existing index:" + self.index_dir)
      return open_dir(self.index_dir)

    if not os.path.exists(self.index_dir):
      os.mkdir(self.index_dir)
    print("build index：" + self.index_dir)
    ana = RegexAnalyzer(r"[\u4e00-\ufaff]|[0-9_a-zA-Z\-]+\'*[a-z]*")
    schema = Schema(standard=TEXT(stored=True, analyzer=ana),
                    raw=TEXT(stored=True, analyzer=ana))

    index = create_in(self.index_dir, schema)
    writer = index.writer(procs=4, limitmb=512, multisegment=True)
    for doc in tqdm(self.corpus):
      writer.add_document(standard=doc.standard, raw=doc.raw)

    writer.commit()
    print("index build succeeded")
    return index

  def match(self, doc: str, topN: int) -> List[Doc]:
    searcher = self.index.searcher(weighting=scoring.TF_IDF())
    query = QueryParser("raw", self.index.schema).parse(doc)
    results = searcher.search(query, limit=topN)
    docs = []
    sims = []
    for result in results:
      docs.append(Doc(result["standard"], result["raw"]))
      sims.append(result.score)
    return docs, sims

  def doc_sim(self):
    pass


if __name__ == '__main__':
  topN = 10
  corpus = load_titles()
  matcher = CharMatcher(corpus, rebuild=False)

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
