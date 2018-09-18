# -*- coding: utf-8 -*-
import csv

from conf import titles_pt

def load_titles():
  rows = csv.reader(open(titles_pt, encoding="utf8"))
  docs = []
  for row in rows:
    doc = row[2]
    docs.append(doc)
  return docs

titles = load_titles()

if __name__ == '__main__':
    print("n(title)=%d" % len(titles))