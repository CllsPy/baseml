import mlflow
import yaml
from baseml.train_models import make_prediction, evaluate


with open("config/model.yaml", "r") as f:
    params_yaml = yaml.safe_load(f)


def track_best_params(dataset_name, tmp):
    mlflow.set_experiment("Third Try")

    with mlflow.start_run():
        estimator, best_params = make_prediction(dataset_name, tmp)
        metric = evaluate(dataset_name, tmp)

        mlflow.log_params(best_params)
        mlflow.log_metric("mae", metric)
        mlflow.sklearn.log_model(estimator, "model")

    return best_params


if __name__ == "__main__":
    print(track_best_params("sample", "data/"))
