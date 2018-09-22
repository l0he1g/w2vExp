#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""文档匹配基类
"""
from abc import ABC, abstractmethod
from basic.doc import Doc

class DocMatcher(ABC):

  @abstractmethod
  def match(self, doc: str, topN:int = 10) -> list[Doc]:
    pass

