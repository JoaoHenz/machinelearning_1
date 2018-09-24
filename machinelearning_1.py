import sys
from generallib import *


numberofargs = 4+1
if len(sys.argv) < numberofargs:
    print('arguments are: 1.randomseed 2.ntreeparameter 3.datasetpath 4.outputpath')
    callexit()
print('thats correct')
random.seed(sys.argv[1])
ntreeparameter = sys.argv[2]
try:
    dataset = readdataset(sys.argv[2])
except:
    print('something wrong with the dataset path!')
    callexit()



callexit()
