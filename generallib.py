import csv
import numpy
from random import *
import random

testratio = 0.3

'''
class Attribute:
	def __init__(self, name, element_list):
		self.name = name;
		self.element_list = element_list
		self.possib_number = 0  # numero de valores que o atributo pode assumir

class Dataset:
	def __init__(self):
		self.attlist = [] #lista de "Attribute"
		self.attnum = 0
		self.datasize = 0

def readdataset(datapath):

	with open(datapath, 'rb') as csvfile:

		dataset = Dataset()

		csvline = csv.reader(csvfile, delimiter=';')

		i = 0

		for row in csvline:

			if(i==0): # primeira linha

				dataset.attnum = len(row)

				for j in range(dataset.attnum):
					dataset.attlist.append(Attribute(row[j], [])) # instancia cada atributo

				i+=1

			else:
				for j in range(dataset.attnum):
					dataset.attlist[j].element_list.append(row[j]) # enche a lista de atributos

	for i in range(dataset.attnum):
		dataset.attlist[i].possib_number = len(set(dataset.attlist[i].element_list))
	#	print(dataset.attlist[i].possib_number)
	#	print(dataset.attlist[i].element_list)  # pra debug

	return dataset
'''

class Bootstrap:
    def __init__(self):
        self.trainingset = []
        self.testset = []

def readdataset(datasetpath):
    dataset = []

    with open(datasetpath, 'rt') as csvfile:
        csvline = csv.reader(csvfile, delimiter=';')
        for row in csvline:
            datasetrow = []
            for i in range(0,len(row)):
                datasetrow.append(row[i])
            dataset.append(datasetrow)


    dataset = numpy.matrix(dataset)

    return dataset

def callexit():
    print('')
    exit()

def create_bootstraplist(dataset,numberofbootstraps):
    bootstraplist = []
    dataset = dataset.tolist()

    testsetsize = int(len(dataset) * testratio)

    for i in range(0,numberofbootstraps): #every bootstrap
        bootstrap = Bootstrap()
        testindexlist = []
        begintestset = randint(0,len(dataset)-testsetsize-1)
        for j in range(begintestset,begintestset+testsetsize):
            bootstrap.testset.append(dataset[j])
            testindexlist.append(j)
        bootstrap.testset = numpy.matrix(bootstrap.testset)
        for j in range(0,len(dataset)): #every instance
            randomindex = randint(0,len(dataset)-1)
            while randomindex in testindexlist:
                randomindex = randint(0,len(dataset)-1)
            bootstrap.trainingset.append(dataset[randomindex])
        bootstrap.trainingset = numpy.matrix(bootstrap.trainingset)
        bootstraplist.append(bootstrap)


    return bootstraplist

# def create_tree(dataset):
