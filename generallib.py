# =============================================================================
# Usando create_bootstrap_list
# =============================================================================
'''
import bootstrap as bs
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
boot = bs.create_bootstrap_list(dataset_original, 3, 0.6)

for b in boot:
    print("Train")
    print(b.training_set)
    print("Test")
    print(b.test_set)

# =============================================================================
# Usando árvore simples
# =============================================================================

from simple_tree import Tree

# Coluna a ser predita (-1 == ultima, na minha opiniao pode ser variavel global)
y_column = -1
# Carregando CSV
dataset_original = pd.read_csv("dadosBenchmark_validacaoAlgoritmoAD.csv", sep = ";")
# Lista de atributos do dataset
attribute_list = np.array(dataset_original.iloc[:,:-1].columns.values)

arvore = Tree(y_column, dataset_original, attribute_list)
arvore.fit()
arvore.print()
'''
