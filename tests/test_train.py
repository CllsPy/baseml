from baseml.train_models import split_data
import pytest


def test_split_data():
    X_train, X_test, y_train, y_test = split_data("sample", "target")
   
    assert X_train.shape[0] == y_train.shape[0], f'X_train e y_train possuem diferentes números de linhas'
    assert X_test.shape[0] == y_test.shape[0], f'X_test e y_test possuem diferentes números de colunas'
    assert X_train.shape[1] == X_test.shape[1], f'X_test e X_test possuem diferentes números de colunas'

    

    
