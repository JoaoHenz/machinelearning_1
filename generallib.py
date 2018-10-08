import csv
import numpy as np
import random
import math
import pandas as pd

class Node(object):
    def __init__(self):
        self.info = ""
        self.children_list = []
        self.root = False
        self.leaf = False
        self.gain = None
        
    def add_child(self, child):
        self.children.append(child)
    
    def set_leaf(self):
        self.leaf = True
        
    def set_gain(self, gain):
        self.gain = gain



class Bootstrap:
    def __init__(self):
        self.training_set = None
        self.test_set = None
        

# sorteia 
        


def callexit():
    print('')
    exit()


def create_bootstrap_list(dataset, num_bootstrap, test_ratio):
    bootstrap_list = []

    test_set_size = int(dataset.shape[0] * test_ratio)

    for i in range(0, num_bootstrap):
        bootstrap = Bootstrap()
        test_index_list = []
        begin_test_set = random.randint(0, dataset.shape[0] - test_set_size)
        
        for j in range(begin_test_set, begin_test_set + test_set_size):
            bootstrap.test_set.append(dataset[j])
            test_index_list.append(j)
        bootstrap.test_set = np.matrix(bootstrap.test_set)
        
        for j in range(0,len(dataset)): 
            random_index = random.randint(0,len(dataset)-1)
            while random_index in test_index_list:
                random_index = random.randint(0,len(dataset)-1)
            bootstrap.training_set.append(dataset[random_index])
        bootstrap.training_set = np.matrix(bootstrap.training_set)
        bootstrap_list.append(bootstrap)


    return bootstrap_list



# =============================================================================
# Usando árvore simples
# =============================================================================
from simple_tree import Tree

# Coluna a ser predita (-1 == ultima, na minha opiniao pode ser variavel global)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)

arvore = Tree(y_column, dataset_original, attribute_list)
arvore.fit()
arvore.print()
    
    