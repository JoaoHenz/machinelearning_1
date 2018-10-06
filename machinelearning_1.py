import sys
from generallib import *
import random

numberofargs = 4+1
if len(sys.argv) < numberofargs:
    print('arguments are: 1.randomseed 2.ntreeparameter 3.datasetpath 4.outputpath')
    callexit()
if (sys.argv[3]=='-'):
    datasetpath = 'dadosBenchmark_validacaoAlgoritmoAD.csv'
else:
    datasetpath = sys.argv[3]
random.seed(sys.argv[1])
ntreeparameter = sys.argv[2]
try:
    dataset = readdataset(datasetpath)
    print('this is the dataset:\n',dataset)
    '''
    att_list = numpy.asarray(dataset[0]).ravel().tolist()
    att_list.pop()
    tree = create_tree(dataset, att_list)
    '''
    
except Exception as e:
    print('Error!\n',e)
    callexit()



callexit()
