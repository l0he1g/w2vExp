#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""文档匹配基类
"""
from abc import ABC, abstractmethod
from match.doc import Doc
from typing import List

class DocMatcher(ABC):

  @abstractmethod
  def match(self, doc: str, topN: int) -> List[Doc]:
    pass

