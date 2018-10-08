#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 03:22:52 2018

@author: jcdazeredo
"""

import numpy as np
import math

class Node(object):
    def __init__(self):
        self.info = ""
        self.children_list = []
        self.root = False
        self.leaf = False
        self.gain = None
        
    def add_child(self, child):
        self.children.append(child)
    
    def set_leaf(self):
        self.leaf = True
        
    def set_gain(self, gain):
        self.gain = gain

class Tree(object):
    def __init__(self, y_column, dataset, attribute_list):
        self.y_column = -1
        self.dataset = dataset
        self.attribute_list = attribute_list
        self.root = None
    
    # =============================================================================
    # Parâmetros:
    #   attribute_list: lista de atributos existentes no dataframe, para calcular
    #   o ganho. Exemplo: [age, income, student]
    #   
    #   y: tipo Series (pandas), coluna y a ser predita
    #
    # Retorno: índice do vetor attribute_list cujo ganho é o maior, e valor ganho
    # =============================================================================
    def id3(self, dataset, attribute_list):
        num_rows = dataset.shape[0]
        y = dataset.iloc[:,self.y_column]
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
    #        print(attribute + ": " + str(classes_gain[i]))
            i+=1
    #    print("InfoD: " + str(infoD))     
        argmax = np.argmax(classes_gain)
        return argmax, classes_gain[argmax]
    
    def fit(self):
        self.root = self.create_tree(self.dataset, self.attribute_list)
    
    def create_tree(self, dataset, att_list):
        new_node = Node()
        
        if len(np.unique(dataset.iloc[:, self.y_column])) == 1:
            new_node.info = dataset.iloc[0, self.y_column]
            new_node.set_leaf()
            return new_node
    
        elif len(att_list) == 0: # nao tem mais nenhum atributo no dataset
            att_values, counts = np.unique(dataset.iloc[:, self.y_column], return_counts = True)
            index_max = np.argmax(counts)
            new_node.info = att_values[index_max]
            new_node.set_leaf()
            return new_node
    
        else:
            best_att_index, best_att_gain = self.id3(dataset, att_list)
            best_att = att_list[best_att_index]
            new_node.info = best_att
            new_node.set_gain(best_att_gain)
            
            att_values = np.unique(self.dataset.loc[:, best_att])
            att_list = np.delete(att_list, best_att_index)
            
            for value in att_values:
                dataset_v = dataset[dataset.loc[:, best_att] == value]
    
                if dataset_v.shape[0] == 0: # subset ta vazio
                    new_node1 = Node()
    
                    att_values, counts = np.unique(dataset.iloc[:, self.y_column], return_counts = True)
                    index_max = np.argmax(counts)
                    new_node1.info = att_values[index_max]
                    new_node1.set_leaf()
                    
                    pair = (value, new_node1)
                    new_node.children_list.append(pair)
    
                else:
                    pair = (value, self.create_tree(dataset_v, att_list))
                    new_node.children_list.append(pair)
    
        return new_node
    
    def print_tree(self, tree, tab, inicial):
        if not(inicial):
            tab += "\t"
        if(tree.leaf):
            print(tab + tree.info + "(F)\n")
        else:
            print(tab + tree.info + "(A) - Ganho: " + "%.4f" % tree.gain)
        tab += "\t"
        
        for filho in tree.children_list:
            print(tab + "-> " + str(filho[0]))
            self.print_tree(filho[1], tab, False)
    
    def print(self):
        print("######## PRINTANDO ARVORE ########\n\n")
        self.print_tree(self.root, "", True)
        print("A = Atributo")
        print("F = Folha")
    
    
            