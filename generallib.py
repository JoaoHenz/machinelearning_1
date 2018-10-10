import pandas as pd
import numpy as np
import math
from sklearn.metrics import confusion_matrix
from random_forest import Random_Forest

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
    dataset_copy = dataset.copy()
    dataset_copy['JaAdicionado'] = 'nao'
    for i in range(0,num_divisions):
        kcross_list.append([])
    class_list = []
    for i in range(0,len(dataset_copy[classcolumn])):
        if not(dataset_copy[classcolumn][i] in class_list):
            class_list.append(dataset_copy[classcolumn][i])
    #print('numero de classes é:',len(class_list))
    k = 0
    next_i = []
    for i in range(0,len(dataset_copy)):
        j= 0
        while j < num_divisions and i < len(dataset_copy):
            if k>=len(class_list):
                k = 0
            if len(next_i)!=0:
                next_i = []
            while len(next_i)==0 and len(class_list)>0:
                next_i = search_next(class_list, dataset_copy ,k,classcolumn)
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
        kcross_list[i] = kcross_list[i].iloc[:, :-1].reset_index(drop = True)
        
#        print('\n\nesta é a kcross list:\n',kcross_list[i],'\n')

    return kcross_list


def calcula_f1measure(matrix,beta):
    precision = []
    recall = []
    truepositive = []

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i == j:
                truepositive.append(matrix[i][j])

    for i in range(0,len(truepositive)):
        precision.append(truepositive[i]/sum(matrix[i,:]))
        recall.append(truepositive[i]/sum(matrix[:,i]))

    for i in range(0,len(recall)):
        if math.isnan(recall[i]):
            recall[i]=1

    for i in range(0,len(precision)):
        if math.isnan(precision[i]):
            precision[i]=1

    recall = sum(recall)/len(recall)
    precision = sum(precision)/len(precision)

    f1_measure = 2 * (precision * recall)/(precision + recall)
    if math.isnan(f1_measure):
        f1_measure=1
    return f1_measure

def f1measure_emlista(matrix_list, beta):
    f1measure_mediatotal = []
    for i in range(0,len(matrix_list)):
        f1measure_mediatotal.append(calcula_f1measure(matrix_list[i],beta))
#        print('olha isso: ',calcula_f1measure(matrix_list[i],beta))
    return (sum(f1measure_mediatotal)/len(f1measure_mediatotal))

def mean_acc(acc_list):
    return (sum(acc_list)/len(acc_list))
    
def train_kfold(k, y_column_name, y_column_number, dataset, attribute_list, num_tree):
    folds_original = stratified_kcross_validation(dataset, k, y_column_name)
    cm_list = []
    accuracy_list = []
    print("###### K-FOLD RUNNING ######")
    print()
    for i in range(k):
        folds = folds_original.copy()
        teste = folds.pop(i)
        teste = teste.reset_index(drop = True)
        treino = folds
        treino = pd.concat(treino).reset_index(drop = True)
        floresta = Random_Forest(y_column_number, treino, attribute_list, num_tree)
        print()
        print("###### RANDOM FOREST TRAINING - " + str(i+1) + "/" + str(k) + " folds ######")
        floresta.fit()
        
        print("###### RANDOM FOREST TESTING ######")
        print()
        y_pred, mode = floresta.classify(teste)
        
        y_actual = teste.iloc[:, y_column_number]
        y_pred = np.reshape(y_pred, (y_actual.shape))
        
        # Resultado do classificador
        classifier_result = y_pred == y_actual
        accuracy = np.sum(classifier_result) / y_actual.shape[0]
        print("Parcial Accuracy: " + str("%.3f" % accuracy))
        accuracy_list.append(accuracy)
        cm = confusion_matrix(y_actual, y_pred)
        cm_list.append(cm)
    
    return accuracy_list, cm_list

def create_stringlist(numberofstrings):
    stringlist = []

    for i in range(0, numberofstrings):
        stringlist.append(str(chr(65+i)))

    return stringlist