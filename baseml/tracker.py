import mlflow
import yaml
from baseml.train_models import make_prediction


with open("config/model.yaml", "r") as f:
    params_yaml = yaml.safe_load(f)


def track_best_params(dataset_name, tmp):
    mlflow.set_experiment("Second Try")

    with mlflow.start_run():
        best_params = make_prediction(dataset_name, tmp)
        mlflow.log_params(best_params)

    return best_params


if __name__ == "__main__":
    print(track_best_params("sample", "data/"))
