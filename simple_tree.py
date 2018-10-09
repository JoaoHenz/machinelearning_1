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
    def __init__(self, y_column, dataset, attribute_list, random_att):
        self.y_column = -1
        self.dataset = dataset
        self.attribute_list = attribute_list
        self.root = None
        self.features_vector = None
        self.random_att = random_att

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
            #            print(attribute + ": " + str(classes_gain[i]))
            i+=1
            #        print("InfoD: " + str(infoD))
        argmax = np.argmax(classes_gain)
        return argmax, classes_gain[argmax]

    def fit(self):
        self.root = self.create_tree(self.dataset, self.attribute_list)
        self.dataset = None

    def create_tree(self, dataset, att_list):
        new_node = Node()

        if len(np.unique(dataset.iloc[:, self.y_column])) == 1:
            new_node.info = dataset.iloc[0, self.y_column]
            new_node.set_leaf()
            return new_node

        elif att_list.shape[0] == 0: # nao tem mais nenhum atributo no dataset
            att_values, counts = np.unique(dataset.iloc[:, self.y_column], return_counts = True)
            index_max = np.argmax(counts)
            new_node.info = att_values[index_max]
            new_node.set_leaf()
            return new_node

        else:
            if self.random_att:
                num_pick = att_list.shape[0] ** (1/2) # raiz quadrada
            else:
                num_pick = att_list.shape[0] # qtd normal, sem subsampling

            num_pick = round(num_pick)
            if num_pick == 0:
                num_pick = 1

            random_att_list = np.random.choice(att_list, num_pick, replace = False)
            best_att_index, best_att_gain = self.id3(dataset, random_att_list)
            att = random_att_list[best_att_index]
            att_index_original = np.argwhere(att_list == att)[0][0]

            new_node.info = att
            new_node.set_gain(best_att_gain)

            att_values = np.unique(self.dataset.loc[:, att])
            att_list = np.delete(att_list, att_index_original)

            for value in att_values:
                dataset_v = dataset[dataset.loc[:, att] == value]

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

    def printree(self):
        print("######## PRINTANDO ARVORE ########\n\n")
        self.print_tree(self.root, "", True)
        print("A = Atributo")
        print("F = Folha")

    def classify(self, dataset):
        num_rows = dataset.shape[0]
        y_pred = []

        for i in range(num_rows):
            y_pred.append(self.classify_single(dataset.iloc[i:i+1, :]))

        return np.array(y_pred)

    def classify_single(self, features_vector):
        features_vector = features_vector.reset_index(drop = True)
        self.features_vector = features_vector

        resultado = self.classify_core(self.root)

        self.features_vector = None
        return resultado

    def classify_core(self, node):
        if node.leaf:
            return node.info
        else:
            children = node.children_list
            flag = 0
            for child in children:
                if child[0] == self.features_vector.loc[0, node.info]:
                    x = self.classify_core(child[1])
                    flag = 1

            if flag == 0:
                return -1
            return x
