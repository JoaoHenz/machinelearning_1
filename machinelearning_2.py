#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 00:34:21 2018

@author: jcdazeredo
"""

# =============================================================================
# Pre - Processing
# =============================================================================

import pandas as pd
import numpy as np
import generallib as gl
pred_col = 4
separator = ";"
k = 2
n_trees = 20
input_file = "dadosBenchmark_validacaoAlgoritmoAD.csv"
no_header = False

y_column = pred_col
if no_header:
    dataset_original = pd.read_csv(input_file, sep = separator, header = None)
    header = gl.create_stringlist(dataset_original.shape[1])
    dataset_original.columns = header
else:
    dataset_original = pd.read_csv(input_file, sep = separator)

header = dataset_original.columns.values
y_column_name = header[y_column]

# Lista de atributos do dataset
attribute_list = np.array(dataset_original.columns.values)
attribute_list = np.delete(attribute_list, y_column)

acc, cm = gl.train_kfold(k, y_column_name, y_column, dataset_original, attribute_list, n_trees)

f1_measure = gl.f1measure_emlista(np.array(cm), 1)
print("F1 Measure: %.3f" % f1_measure)
mean_acc = gl.mean_acc(acc)
print("Accuracy: " + str("%.3f" % mean_acc))
