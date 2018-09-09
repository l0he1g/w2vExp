#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""读取DuReader数据
"""

import json
import csv
from conf import titles_pt

raw_pt = "/Users/yxh/data/duReader/raw/trainset/zhidao.train.json"


def read_file(pt, res_pt):
  wf = csv.writer(open(res_pt, "w", newline=""))
  for line in open(pt, encoding="utf8"):
    entry = json.loads(line.strip())
    qid = entry["question_id"]
    question = entry["question"].replace(",", " ").strip()
    for d in entry["documents"]:
      title = d["title"].replace(",", " ").strip()
      wf.writerow((qid, question, title))


if __name__ == '__main__':
  read_file(raw_pt, titles_pt)
