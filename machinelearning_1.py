import sys
import traceback
from generallib import *

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
    bootstraplist = create_bootstraplist(dataset,3)
    print('this is the bootstrap list:\n')
    for i in range(0,len(bootstraplist)):
        print('\nBootstrap ',i,':\nTraining set:\n',bootstraplist[i].trainingset,'\nTest set:\n',bootstraplist[i].testset)
    # tree = create_tree(dataset)

except Exception as e:
    print('\n',traceback.format_exc())
    #print('\nError on line {}:'.format(sys.exc_info()[-1].tb_lineno),'\n', type(e).__name__, e)
    callexit()



callexit()
