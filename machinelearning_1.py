import sys
import traceback
import random
import pandas as pd
import bootstrap as bs
from generallib import *

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
# Usando árvore simples
# =============================================================================
from simple_tree import Tree

# Coluna a ser predita (-1 == ultima, na minha opiniao pode ser variavel global)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)


print(dataset_original,'\n\n',attribute_list)

arvore = Tree(y_column, dataset_original, attribute_list)
arvore.fit()
arvore.print()

stratifiedkcrossvalidation(dataset_original,3,'Joga')
