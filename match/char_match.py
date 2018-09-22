#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""基于字的匹配
"""
from match.matcher import DocMatcher


class CharMatcher(DocMatcher):

  def __init__(self, stop_words):
    pass

  def match(self, doc: str, topN: int):
    pass

  def doc_sim(self):
    pass
