import csv
import numpy as np
import random
import math
import pandas as pd

class Node:

    def __init__(self):
        self.info = ""
        self.children_list = []

    def add_child(self, child):
        self.children.append(child)
testratio = 0.3



# O método gain_info necessita das variáveis abaixo para funcionar.
#
# Coluna a ser predita (-1 == ultima, na minha opiniao pode ser variavel global)
y_column = -1
# Carregando CSV
data_set = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(data_set.iloc[:,:-1].columns.values)

# =============================================================================
# Parâmetros:
#   attribute_list: lista de atributos existentes no dataframe, para calcular
#   o ganho. Exemplo: [age, income, student]
#   
#   y: tipo Series (pandas), coluna y a ser predita
#
# Retorno: índice do vetor attribute_list cujo ganho é o maior
# =============================================================================
def gain_info(attribute_list, dataset):
    num_rows = dataset.shape[0]
    y = dataset.iloc[:,y_column]
    # Verifica as classes possíveis de serem preditas
    classes = np.unique(y)
    # Calcula o INFO(D) que está nos slides. Cálculo da Entropia.
    infoD = 0
    for cl in classes:
        prob = len(y[y==cl]) / num_rows
        infoD = infoD -(prob*math.log2(prob)) 
    
    classes_gain = np.empty_like(attribute_list)
    i = 0
    # Para cada atributo:
    for attribute in attribute_list:
        # Valores possíveis da classe
        values = np.unique(dataset[attribute])
        # Pega, do dataset original, somente a coluna respectiva a classe atual do for 
        dummy_df = dataset[attribute]
        infoD_class = 0
        # Para cada valor possível do atributo:
        for vl in values:
            infoDj = 0
            # Probabilidade de dar o valor vl para o atributo
            prob = len(dummy_df[dummy_df==vl]) / num_rows
            # Índices do dataframe cujo atributo tem valor vl
            indexes = dummy_df[dummy_df==vl].index
            # Número de linhas para esse valor de atributo
            num_rows_vl = y[indexes].shape[0]
            
            # Pra cada classe possível de ser predita, calcula o InfoDj (somatório)
            for cl in classes:
                prob_cl = len((y[indexes])[y==cl]) / num_rows_vl
                if prob_cl != 0:
                    infoDj = infoDj -(prob_cl*math.log2(prob_cl))
            infoD_class = infoD_class + prob*infoDj
    
        classes_gain[i] = infoD - infoD_class
        print(attribute + ": " + str(classes_gain[i]))
        i+=1
    print("InfoD: " + str(infoD))        
    return np.argmax(classes_gain)

#Exemplo de uso da função.
x = gain_info(attribute_list, data_set)
print("Atributo de maior ganho: " + str(attribute_list[x]))
    

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

## da pra substituir isso por pd.read_csv("dataset.csv", sep = ";")
def readdataset(datasetpath):
    dataset = []

    with open(datasetpath, 'rt') as csvfile:
        csvline = csv.reader(csvfile, delimiter=';')
        for row in csvline:
            datasetrow = []
            for i in range(0,len(row)):
                datasetrow.append(row[i])
            dataset.append(datasetrow)


    dataset = np.matrix(dataset)

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
        begintestset = random.randint(0,len(dataset)-testsetsize-1)
        for j in range(begintestset,begintestset+testsetsize):
            bootstrap.testset.append(dataset[j])
            testindexlist.append(j)
        bootstrap.testset = np.matrix(bootstrap.testset)
        for j in range(0,len(dataset)): #every instance
            randomindex = random.randint(0,len(dataset)-1)
            while randomindex in testindexlist:
                randomindex = random.randint(0,len(dataset)-1)
            bootstrap.trainingset.append(dataset[randomindex])
        bootstrap.trainingset = np.matrix(bootstrap.trainingset)
        bootstraplist.append(bootstrap)


    return bootstraplist

def create_tree(dataset, att_list):

    new_node = Node()
    if len(np.unique(np.asarray(dataset[:,-1]))) == 1: # saida so tem uma classe
        new_node.info = dataset[1:-1]
        return new_node

    elif len(att_list) == 0: # nao tem mais nenhum atributo no dataset
        class_array = np.asarray(dataset[:,-1])
        class_array = np.delete(class_array, 0) # pra tirar o header da lista

        unique, counts = np.unique((class_array),  return_counts = True) # counts possui a frenquencia de cada classe
        max_index, = np.where(counts == max(counts)) # pega o index das classe mais frenquente
        new_node.info = max_index[0] # contem a classe mais frequente no dataset

    else:
        best_att, att_index = id3(dataset, att_list) # TODO
        new_node.info = best_att
        att_list.remove(best_att)

        att_values = np.unique(np.asarray(dataset[:,att_index]))
        att_values = np.delete(att_values,0) # pra tirar o header da lista

        for value in att_values:
            dataset_v = create_sub_dataset(dataset)

            if len(dataset_v) == 1: # subset ta vazio
                new_node1 = Node()

                class_array = np.asarray(dataset[:,-1])
                class_array = np.delete(class_array, 0)
                unique, counts = np.unique((class_array),  return_counts = True)
                max_index, = np.where(counts == max(counts))
                new_node.info1 = max_index[0] # contem a classe mais frequente no dataset

                new_node.children_list.append(new_node1) # adiciona folha

            else:
                new_node.children_list.append(create_tree(dataset_v, att_list))

    return new_node


def id3(dataset, att_list):
    pass

def create_sub_dataset(dataset):
    pass




