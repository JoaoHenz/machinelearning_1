import csv
import numpy
from random import *
import random

class Node:

    def __init__(self):
        self.info = ""
        self.children_list = []

    def add_child(self, child):
        self.children.append(child)
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
    #   print(dataset.attlist[i].possib_number)
    #   print(dataset.attlist[i].element_list)  # pra debug

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

def create_tree(dataset, att_list):

    new_node = Node()
    if len(numpy.unique(numpy.asarray(dataset[:,-1]))) == 1: # saida so tem uma classe
        new_node.info = dataset[1:-1]
        return new_node

    elif len(att_list) == 0: # nao tem mais nenhum atributo no dataset
        class_array = numpy.asarray(dataset[:,-1])
        class_array = numpy.delete(class_array, 0) # pra tirar o header da lista

        unique, counts = numpy.unique(class_array),  return_counts = True) # counts possui a frenquencia de cada classe
        max_index, = numpy.where(counts == max(counts)) # pega o index das classe mais frenquente
        new_node.info = max_index[0] # contem a classe mais frequente no dataset

    else:
        best_att, att_index = id3(dataset, att_list) # TODO
        new_node.info = best_att
        att_list.remove(best_att)

        att_values = numpy.unique(numpy.asarray(dataset[:,att_index]))
        att_values = numpy.delete(att_values,0) # pra tirar o header da lista

        for value in att_values:
            dataset_v = create_sub_dataset(dataset)

            if len(dataset_v) == 1: # subset ta vazio
                new_node1 = Node()

                class_array = numpy.asarray(dataset[:,-1])
                class_array = numpy.delete(class_array, 0)
                unique, counts = numpy.unique(class_array),  return_counts = True)
                max_index, = numpy.where(counts == max(counts))
                new_node.info1 = max_index[0] # contem a classe mais frequente no dataset

                new_node.children_list.append(new_node1) # adiciona folha

            else:
                new_node.children_list.append(create_tree(dataset_v, att_list))

    return new_node


def id3(dataset, att_list):
    pass

def create_sub_dataset(dataset):
    pass




