import csv
import numpy as np
import random
import math
import pandas as pd
import numbers as nb

def search_next(class_list,dataset,k,classcolumn):
    i=0
    while i<len(dataset):
        if dataset['JaAdicionado'][i] == 'nao' and dataset[classcolumn][i] == class_list[k]:
            dataset['JaAdicionado'][i] = 'sim'
            next_i = dataset.iloc[[i]]
            next_i = next_i.iloc[:,:]
            return next_i
        i+=1
    return []

def stratified_kcross_validation(dataset, num_divisions, classcolumn):
    kcross_list = []
    dataset['JaAdicionado'] = 'nao'
    for i in range(0,num_divisions):
        kcross_list.append([])
    class_list = []
    for i in range(0,len(dataset[classcolumn])):
        if not(dataset[classcolumn][i] in class_list):
            class_list.append(dataset[classcolumn][i])
    #print('numero de classes é:',len(class_list))
    k = 0
    next_i = []
    for i in range(0,len(dataset)):
        j= 0
        while j < num_divisions and i < len(dataset):
            if k>=len(class_list):
                k = 0
            if len(next_i)!=0:
                next_i = []
            while len(next_i)==0 and len(class_list)>0:
                next_i = search_next(class_list, dataset ,k,classcolumn)
                if len(next_i)==0:
                    del class_list[k]
                    k -= 1
            if len(next_i)>0:
#                print(next)
                kcross_list[j].append(next_i)
            k+=1
            j+=1
    for i in range(0,num_divisions):
        kcross_list[i] = pd.concat(kcross_list[i])
        kcross_list[i] = kcross_list[i].iloc[:, :-1]
#        print('\n\nesta é a kcross list:\n',kcross_list[i],'\n')

    return kcross_list



















#def searchnext(class_list, dataset, k, classcolumn):
#    i = 0
#    while i < dataset.shape[0]:
##        print("i: " + str(i))
##        print("classcolumn: " + str(classcolumn))
##        print("k = " + str(k))
##        print("class_list[k] tamanho = " + str(len(class_list)))
##        print("class_list[k]" + str(class_list[k]))
##        print("dataset[jaAdicionado][i]\n")
##        print(dataset['JaAdicionado'][i])
##        print("dataset.iloc[i, classcolum]\n\n")
##        print(dataset.iloc[i, classcolumn])
##        print("class_list")
##        print(class_list)
##        print()
##        print()
#        if dataset['JaAdicionado'][i] == 'nao' and dataset.iloc[i, classcolumn] == class_list[k]:
#            dataset['JaAdicionado'][i] = 'sim'
#            next_i = dataset.iloc[[i]]
#            return next_i
#        i+=1
#    return []
#    
#def stratifiedkcrossvalidation(dataset, num_divisions,classcolumn):
#    kcross_list = []
#    control_dataset = dataset
#    control_dataset['JaAdicionado'] = 'nao'
#    
#    for i in range(0, num_divisions):
#        kcross_list.append([])
#    
#    class_list = np.unique(dataset.iloc[:, classcolumn])
#    k = 0
#    next_i = []
#    
#    for i in range(0, dataset.shape[0]):
#        j= 0
#        while j < num_divisions and i < dataset.shape[0]:
#            print("inicio while, k = " + str(k))
#            if k >= len(class_list):
#                k = 0
#                
#            if len(next_i) != 0:
#                next_i = []
#                
#            while len(next_i) == 0 and len(class_list) > 0:
#                next_i = searchnext(class_list, dataset, k, classcolumn)
#                
#                if len(next_i)==0:
#                    class_list = np.delete(class_list, k)
#                    k -= 1
#                    
#            if len(next_i) > 0:
##                print(next_i)
#                kcross_list[j].append(next_i)
#            
#            k+=1
#            j+=1
#            
#    for i in range(0, num_divisions):
#        kcross_list[i] = pd.concat(kcross_list[i])
##        print('\n\nesta é a kcross list:\n',kcross_list[i],'\n')

    return kcross_list