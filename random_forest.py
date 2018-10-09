#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:18:33 2018

@author: jcdazeredo
"""

from simple_tree import Tree
from scipy import stats
import bootstrap as bs
import numpy as np

class Random_Forest(object):
    def __init__(self, y_column, dataset, attribute_list, num_trees):
        self.num_trees = num_trees
        self.y_column = -1
        self.dataset = dataset
        self.attribute_list = attribute_list
        self.bootstrap_list = None
        self.tree_list = [None]*num_trees
        self.cm = None
        self.accuracy = None
        
    def fit(self):
        self.create_bootstrap()

        for i in range(self.num_trees):
            self.tree_list[i] = Tree(self.y_column, self.bootstrap_list[i].training_set, self.attribute_list, True)
            self.tree_list[i].fit()
#            self.tree_list[i].printree()
        
    def create_bootstrap(self):
        self.bootstrap_list = bs.create_bootstrap_list(self.dataset, self.num_trees, 0.7)
  
    def validation(self):
        pass

            
    def classify(self, dataset):
        predictions = [None]*self.num_trees
        
        # Faz a predição de todas as árvores para o mesmo dataset
        for i in range(self.num_trees):
            predictions[i] = self.tree_list[i].classify(self.dataset)
            
        predictions = np.array(predictions)
        
        # Verifica qual teve mais votação
        mode = stats.mode(predictions)
        y_pred = mode[0].transpose()   
        return y_pred
