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
try:
    dataset = pd.read_csv(dataset_path, sep = ";")
    print('this is the dataset:\n',dataset)
    bootstrap_list = bs.create_bootstrap_list(dataset, 3, 0.3)
    print('this is the bootstrap list:\n')
    for i in range(0,len(bootstrap_list)):
        print('\nBootstrap ',i,':\nTraining set:\n',bootstrap_list[i].training_set,'\nTest set:\n',bootstrap_list[i].test_set)
    '''
    att_list = numpy.asarray(dataset[0]).ravel().tolist()
    att_list.pop()
    tree = create_tree(dataset, att_list)
    '''

except Exception as e:
    print('\n',traceback.format_exc())
    #print('\nError on line {}:'.format(sys.exc_info()[-1].tb_lineno),'\n', type(e).__name__, e)
    callexit()

callexit()




# =============================================================================
# Utilizando Arvore
# =============================================================================

# Coluna a ser predita (-1 == ultima, na minha opiniao pode ser variavel global)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)

# Cria arvore
arvore = Tree(y_column, dataset_original, attribute_list)
arvore.fit() # Após fit ele remove o dataset guardado
# Printa Tree
arvore.printree()

# Classifica dataset
vector = dataset_original.iloc[:, 0:-1]
x = arvore.classify(vector)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(x, dataset_original.iloc[:, -1])