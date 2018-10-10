import pandas as pd
import numpy as np
from simple_tree import Tree
import generallib as gl


# =============================================================================
# Usando floresta
# =============================================================================

from sklearn.metrics import confusion_matrix
from random_forest import Random_Forest



# =============================================================================
# Pre - Processing
# =============================================================================
# Coluna a ser predita
y_column = 0

header = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

# Carregando CSV
dataset_original = pd.read_csv("wine.csv", sep = ",", header = None)
dataset_original.columns = header

header = dataset_original.columns.values
x = gl.stratified_kcross_validation(dataset_original,3, header[0])

# Lista de atributos do dataset
attribute_list = np.array(dataset_original.columns.values)
attribute_list = np.delete(attribute_list, y_column)




# =============================================================================
# Random Forest
# =============================================================================
floresta = Random_Forest(y_column, dataset_original.iloc[0:100, :], attribute_list, 10)
floresta.fit()

y_pred, mode = floresta.classify(dataset_original.iloc[100:, :])

y_actual = dataset_original.iloc[:, y_column]
y_pred = np.reshape(y_pred, (y_actual.shape))

# Resultado do classificador
classifier_result = y_pred == y_actual
accuracy = np.sum(classifier_result) / dataset_original.shape[0]
cm = confusion_matrix(y_actual, y_pred)










# =============================================================================
# Pre - Processing
# =============================================================================
# Coluna a ser predita
y_column = 0

# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")

header = dataset_original.columns.values
x = gl.stratified_kcross_validation(dataset_original,3, header[4])

# Lista de atributos do dataset
attribute_list = np.array(dataset_original.columns.values)
attribute_list = np.delete(attribute_list, y_column)
































