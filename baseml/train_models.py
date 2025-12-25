from baseml.data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error

from sklearn import svm

import yaml

with open("config/model.yaml", "r") as f:
    params_yaml = yaml.safe_load(f)


def split_data(dataset_name: str, tmp: str):
    data_frame = load_data(dataset_name, tmp)

    X = data_frame.drop("target", axis=1)
    y = data_frame.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=params_yaml["GRIDSEARCH"]["test_size"],
        random_state=params_yaml["GRIDSEARCH"]["random_state"],
    )

    return X_train, X_test, y_train, y_test


def setup_models():
    model = svm.SVR()
    return model


def setup_grid():
    model = setup_models()

    model_parameters = params_yaml["SVR"]
    grid = GridSearchCV(model, model_parameters)

    return grid


def collect_best_params():
    pass


def jsonfy_predictions():
    pass


def make_prediction(dataset_name, tmp):
    grid = setup_grid()
    X_train, X_test, y_train, y_test = split_data(dataset_name, tmp)

    estimator = grid.fit(X_train, y_train)

    return estimator, estimator.best_params_

def evaluate(dataset_name: str, tmp: str):
    """
    Docstring for evaluate
    """ 

    _, X_test, _, y_test = split_data(dataset_name, tmp)

    estimator, _ = make_prediction(dataset_name, tmp)
    y_hat = estimator.predict(X_test)

    metrics = mean_absolute_error(y_test, y_hat)
    return metrics


if __name__ == "__main__":
    X = [[0, 0], [2, 2], [2, 2], [2, 2], [2, 2]]
    y = [0.5, 2.5, 2.5, 2.5, 2.5]

    #grid = setup_grid()
    #model = setup_models()
    #print(grid)
    #print(model)
    # for x in grid:
    #     print(x)
    #     x.fit(X, y)
    #     print(x.predict([[1, 1]]))

    #estimator, _ = (make_prediction("sample", "data/"))
    print(evaluate("sample", "data/"))
    # for x in setup_grid():
