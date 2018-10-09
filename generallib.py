import csv
import numpy as np
import random
import math
import pandas as pd


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
