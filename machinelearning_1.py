import sys
import traceback
from generallib import *

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
    dataset = read_dataset(dataset_path)
    print('this is the dataset:\n',dataset)
    bootstrap_list = create_bootstrap_list(dataset, 3, 0.3)
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
