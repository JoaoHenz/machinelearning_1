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

def searchnext(class_list,dataset,k):
    i=0
    while i<len(dataset):
        if dataset['JaAdicionado'][i] == 'nao' and dataset['Joga'][i] == class_list[k]:
            return dataset[i]
    return None

def stratifiedkcrossvalidation(dataset,num_divisions):
    kcross_list = []
    control_dataset = dataset
    control_dataset['JaAdicionado'] = 'nao'
    print('control\n',control_dataset)

    for i in range(0,num_divisions):
        kcross_list.append([])


    class_list = []
    for i in range(0,len(dataset['Joga'])):
        if not(dataset['Joga'][i] in class_list):
            class_list.append(dataset['Joga'][i])

    #print('numero de classes é:',len(class_list))
    k=0
    next = None
    for i in range(0,len(dataset)):
        j= 0
        while j < num_divisions and i < len(dataset):
            if k>len(class_list):
                k = 0
            if next!= None:
                del next
            while next == None:
                next = searchnext(class_list,dataset,k)
                if next == None:
                    del class_list[k]
            kcross_list[j].append(searchnext(class_list,dataset,k))
            k+=1
            j+=1
