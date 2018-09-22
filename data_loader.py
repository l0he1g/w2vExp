# -*- coding: utf-8 -*-
import csv

from conf import titles_pt
from match.doc import Doc
from typing import List

def load_titles() -> List[Doc]:
  rows = csv.reader(open(titles_pt, encoding="utf8"))
  docs = []
  for row in rows:
    doc = Doc(row[1], row[2])
    docs.append(doc)
  return docs

if __name__ == '__main__':
  titles = load_titles()
  print("n(title)=%d" % len(titles))
