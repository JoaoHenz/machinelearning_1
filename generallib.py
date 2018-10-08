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



class Bootstrap(object):
    def __init__(self):
        self.training_set = None
        self.test_set = None
        

# sorteia 
        


def callexit():
    print('')
    exit()


def read_dataset(dataset_path):
    return pd.read_csv(dataset_path, sep = ";")


def create_bootstrap_list(dataset, num_bootstrap, test_ratio):
    bootstrap_list = []

    test_set_size = int(dataset.shape[0] * test_ratio)

    for i in range(0, num_bootstrap):
        bootstrap = Bootstrap()
        test_index_list = []
        begin_test_set = random.randint(0, dataset.shape[0] - test_set_size - 1) # gera um comeco de area de testes aleatorio
            
        for j in range(begin_test_set, begin_test_set + test_set_size):
#            bootstrap.test_set.append(dataset[j])
            test_index_list.append(j)

        bootstrap.test_set = dataset.iloc[begin_test_set:(begin_test_set + test_set_size)] # cria um dataframe novo com apenas as linhas de teste
#        bootstrap.test_set = np.matrix(bootstrap.test_set)
        
        for j in range(1,dataset.shape[0]): 
            random_index = random.randint(1,dataset.shape[0]) 
            while random_index in test_index_list:
                random_index = random.randint(1,dataset.shape[0]) # gera um numero aleatorio fora do test_set
            if j == 1:
                bootstrap.training_set = dataset.iloc[(random_index-1):random_index]
            else:
                bootstrap.training_set = bootstrap.training_set.append(dataset.iloc[(random_index-1):random_index])
                
        bootstrap_list.append(bootstrap)

    return bootstrap_list



# =============================================================================
# Usando árvore simples
# =============================================================================
'''
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
'''    
