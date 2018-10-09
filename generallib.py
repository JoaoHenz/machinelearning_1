import csv
import numpy as np
import random
import math
import pandas as pd


def searchnext(class_list,dataset,k,classcolumn):
    i=0
    while i<len(dataset):
        if dataset['JaAdicionado'][i] == 'nao' and dataset[classcolumn][i] == class_list[k]:
            dataset['JaAdicionado'][i] = 'sim'
            next = dataset.iloc[[i]]
            next = next.loc[:,:classcolumn]
            return next
        i+=1
    return []

def stratifiedkcrossvalidation(dataset, num_divisions,classcloumn):
    kcross_list = []
    control_dataset = dataset
    control_dataset['JaAdicionado'] = 'nao'
    for i in range(0,num_divisions):
        kcross_list.append([])
    class_list = []
    for i in range(0,len(dataset[classcolumn])):
        if not(dataset[classcolumn][i] in class_list):
            class_list.append(dataset[classcolumn][i])
    #print('numero de classes é:',len(class_list))
    k=0
    next = []
    for i in range(0,len(dataset)):
        j= 0
        while j < num_divisions and i < len(dataset):
            if k>=len(class_list):
                k = 0
            if len(next)!=0:
                next = []
            while len(next)==0 and len(class_list)>0:
                next = searchnext(class_list,dataset,k,classcolumn)
                if len(next)==0:
                    del class_list[k]
            if len(next)>0:
                print(next)
                kcross_list[j].append(next)
            k+=1
            j+=1
    for i in range(0,num_divisions):
        kcross_list[i] = pd.concat(kcross_list[i])
        print('\n\nesta é a kcross list:\n',kcross_list[i],'\n')
