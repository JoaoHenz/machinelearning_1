import sys
import traceback
import random
import pandas as pd
import numpy as np
import bootstrap as bs
from simple_tree import Tree
import generallib as gn


#def callexit():
#    print('')
#    exit()
#
#numberofargs = 4+1
#if len(sys.argv) < numberofargs:
#    print('arguments are: 1.randomseed 2.ntreeparameter 3.datasetpath 4.outputpath')
#    callexit()
#if (sys.argv[3]=='-'):
#    dataset_path = 'dadosBenchmark_validacaoAlgoritmoAD.csv'
#else:
#    dataset_path = sys.argv[3]
#random.seed(sys.argv[1])
#ntreeparameter = sys.argv[2]

# =============================================================================
# Usando floresta
# =============================================================================

from sklearn.metrics import confusion_matrix
from random_forest import Random_Forest

# Coluna a ser predita (-1 == ultima)
y_column = 0

header = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]



# Carregando CSV
dataset_original = pd.read_csv("wine.csv", sep = ",", header = None)
dataset_original.columns = header
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.columns.values)
attribute_list = np.delete(attribute_list, y_column)


#gera os dataframes estratificados da k cross validation
kcross_list = gn.stratifiedkcrossvalidation(dataset_original,3,'Joga')

# Cria floresta
floresta = Random_Forest(y_column, dataset_original.iloc[0:100, :], attribute_list, 10)
floresta.fit()

y_pred, mode = floresta.classify(dataset_original.iloc[100:, :])

y_actual = dataset_original.iloc[:, y_column]
y_pred = np.reshape(y_pred, (y_actual.shape))

# Resultado do classificador
classifier_result = y_pred == y_actual
accuracy = np.sum(classifier_result) / dataset_original.shape[0]
cm = confusion_matrix(y_actual, y_pred)


## Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#
#string_column = 3
#dataset_original.iloc[:, string_column] = sc.fit_transform(dataset_original.iloc[:, string_column:string_column+1])
#dataset_original.iloc[:, string_column], bins = pd.qcut(dataset_original.iloc[:, string_column], 5, labels=False, retbins = True)
#
#dataset2 = pd.read_csv("/home/jcdazeredo/Dropbox/Faculdade/UFRGS/Indo/Aprendizado/dataset2.csv")
#dataset2.iloc[:, string_column] = sc.transform(dataset2.iloc[:, string_column:string_column+1])
#dataset2.iloc[:, string_column] = pd.qcut(dataset2.iloc[:, string_column], 5, labels=False)

# =============================================================================
# Usando árvore simples
# =============================================================================

# Coluna a ser predita (-1 == ultima)
#y_column = -1
## Carregando CSV
#dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
## Lista de atributos do dataset
#attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)
#
## Cria arvore
#arvore = Tree(y_column, dataset_original, attribute_list, False)
#arvore.fit() # Após fit ele remove o dataset guardado
## Printa Tree
#arvore.printree()
#
## Classifica dataset
#vector = dataset_original.iloc[:, 0:-1]
#x = arvore.classify(vector)



#stratifiedkcrossvalidation(dataset_original,3)


#import pandas as pd        
#
## Coluna a ser predita (-1 == ultima)
#y_column = 0
#
#header = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
#
## Carregando CSV
#dataset_original = pd.read_csv("wine.csv", sep = ",", header = None)
#dataset_original.columns = header
## Lista de atributos do dataset
#
#attribute_list = np.array(dataset_original.columns.values)
#attribute_list = np.delete(attribute_list, y_column)
#
## Cria arvore
#arvore = Tree(y_column, dataset_original, attribute_list, False)
#arvore.fit()
#arvore.printree()
#
## Classifica dataset
#vector = dataset_original.iloc[:, 1:]
#x = arvore.classify(vector)
#
#dataset_original.iloc[:, 0]
#
#np.sum(x == dataset_original.iloc[:, 0])

