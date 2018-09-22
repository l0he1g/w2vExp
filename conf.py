#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

"""Module documentation 
"""

project_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
data_dir = project_dir + "data/"
titles_pt = data_dir + "titles.csv"

model_dir = project_dir + "model/"
d2v_model_pt = model_dir + "d2v.model"
w2v_model_pt = model_dir + "w2v.model"