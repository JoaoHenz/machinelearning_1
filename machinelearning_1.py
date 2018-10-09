import sys
import traceback
import random
import pandas as pd
import numpy as np
import bootstrap as bs
from simple_tree import Tree

def callexit():
    print('')
    exit()

numberofargs = 4+1
if len(sys.argv) < numberofargs:
    print('arguments are: 1.randomseed 2.ntreeparameter 3.datasetpath 4.outputpath')
    callexit()
if (sys.argv[3]=='-'):
    dataset_path = 'dadosBenchmark_validacaoAlgoritmoAD.csv'
else:
    dataset_path = sys.argv[3]
random.seed(sys.argv[1])
ntreeparameter = sys.argv[2]






# =============================================================================
# Usando floresta
# =============================================================================

from sklearn.metrics import confusion_matrix
from random_forest import Random_Forest

# Coluna a ser predita (-1 == ultima)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)

# Cria floresta
floresta = Random_Forest(y_column, dataset_original, attribute_list, 13)
floresta.fit()
y_pred = floresta.classify(dataset_original)

cm = confusion_matrix(y_pred, dataset_original.iloc[:, -1])




# =============================================================================
# Usando árvore simples
# =============================================================================

# Coluna a ser predita (-1 == ultima)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)

# Cria arvore
arvore = Tree(y_column, dataset_original, attribute_list, False)
arvore.fit() # Após fit ele remove o dataset guardado
# Printa Tree
arvore.printree()

# Classifica dataset
vector = dataset_original.iloc[:, 0:-1]
x = arvore.classify(vector)



#stratifiedkcrossvalidation(dataset_original,3)
