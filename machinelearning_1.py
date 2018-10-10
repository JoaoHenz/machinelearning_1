import pandas as pd
import numpy as np
import generallib as gl
import click


@click.command()
@click.option('--input_file', prompt = 'Input CSV', help = 'Input CSV.')
@click.option('--no_header', is_flag = True, help = 'If CSV have no header.')
@click.option('--separator', default = ',', help = 'CSV Separator. Inside commas.')
@click.option('--k', default = 10, help='K for K-Fold.')
@click.option('--pred_col', default = 0, prompt = 'Column for Prediction', help = 'Column for Prediction, starting from zero.')
@click.option('--n_trees', default = 10, help = 'Number of Trees on each Forest')

def am1(input_file, no_header, separator, k, pred_col, n_trees):
    # =============================================================================
    # Pre - Processing
    # =============================================================================
    try:
        if k < 2:
            k = 2
        y_column = pred_col
        if no_header:
            dataset_original = pd.read_csv(input_file, sep = separator, header = None)
            header = gl.create_stringlist(dataset_original.shape[1])
            dataset_original.columns = header
        else:
            dataset_original = pd.read_csv(input_file, sep = separator)
        
        header = dataset_original.columns.values
        y_column_name = header[y_column]
        
        # Lista de atributos do dataset
        attribute_list = np.array(dataset_original.columns.values)
        attribute_list = np.delete(attribute_list, y_column)
        
        acc, cm = gl.train_kfold(k, y_column_name, y_column, dataset_original, attribute_list, n_trees)
        
        f1_measure = gl.f1measure_emlista(np.array(cm), 1)
        print("F1 Measure: %.3f" % f1_measure)
        mean_acc = gl.mean_acc(acc)
        print("Accuracy: " + str("%.3f" % mean_acc))
        
    except:
        print("ERROR")

if __name__ == '__main__':
    am1()


    
    

















