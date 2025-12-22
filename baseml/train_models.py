from baseml.data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn import linear_model
from sklearn import svm

import yaml
import json

with open("config/model.yaml", "r") as f:
    params_yaml = yaml.safe_load(f)

def split_data(dataset_name: str, target: str):
    data_frame = load_data(dataset_name)

    X = data_frame.drop(target, axis=1)
    y = data_frame.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


def setup_models():
    models = {
        "LinearRegression":  linear_model.LinearRegression(),
        "SVR": svm.SVR()

    }

    return models

def setup_grid():
    models = setup_models()
    grid_search = []

    for key, value in models.items():
        model_parameters = params_yaml[key]
        estimator = GridSearchCV(value, model_parameters)
        grid_search.append(estimator)
    
    return grid_search

def collect_best_params():
    pass

def jsonfy_predictions():
    pass

def make_prediction():
    grid = setup_grid()
    X_train, X_test, y_train, y_test = split_data("sample", "target")

    models_and_predictions = {}

    for estimator in grid:
        estimator.fit(X_train, y_train)

        predictions = estimator.predict(X_test)
        models_and_predictions[estimator] = predictions
    

    return models_and_predictions



if __name__=='__main__':
    X = [[0, 0], [2, 2], [2, 2], [2, 2], [2, 2]]
    y = [0.5, 2.5, 2.5, 2.5, 2.5]

    # grid = setup_grid()
    # for x in grid:
    #     print(x)
    #     x.fit(X, y)
    #     print(x.predict([[1, 1]]))
    
    print(make_prediction())