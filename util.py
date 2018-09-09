#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""Module documentation 
"""
def tokenize(text):
  regex = r"[\u4e00-\ufaff]|[0-9_a-zA-Z\-]+\'*[a-z]*"
  matches = re.findall(regex, text, re.UNICODE)
  return matches
