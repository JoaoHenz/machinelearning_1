#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:26:27 2018

@author: jcdazeredo
"""
import numpy as np

class Bootstrap(object):
    def __init__(self):
        self.training_set = None
        self.test_set = None

def create_bootstrap_list(dataset, num_bootstrap, max_ratio):
    index_dataset = np.array(dataset.index)
    bootstrap_list = []

    for i in range(num_bootstrap):
        bs = Bootstrap()

        test_ratio = np.random.uniform(0, max_ratio)
        num_pick = round(test_ratio*index_dataset.shape[0])

        if num_pick == 0:
            num_pick = 1

        index_test_list = np.random.choice(index_dataset, num_pick, replace = False)

        index_train_list = np.array([e for e in index_dataset if e not in index_test_list])
        dummy_list = np.random.choice(index_train_list, index_dataset.shape[0]-index_train_list.shape[0])
        index_train_list = np.append(index_train_list, dummy_list)

        bs.training_set = dataset.iloc[index_train_list]
        bs.training_set = bs.training_set.reset_index(drop=True)
        bs.test_set = dataset.iloc[index_test_list]
        bs.test_set = bs.test_set.reset_index(drop=True)

        bootstrap_list.append(bs)

    return bootstrap_list
