import mlflow
import yaml
from baseml.train_models import make_prediction, evaluate
from baseml.data_loader import load_data
from mlflow.data.pandas_dataset import PandasDataset


with open("config/model.yaml", "r") as f:
    params_yaml = yaml.safe_load(f)


def track_best_params(dataset_name, tmp):
    mlflow.set_experiment("26 Dez 2025")

    with mlflow.start_run():
        df = load_data(dataset_name, tmp)
        dataset: PandasDataset = mlflow.data.from_pandas(df)
        estimator, best_params = make_prediction(dataset_name, tmp)
        metric = evaluate(dataset_name, tmp)
        model_info = mlflow.sklearn.log_model(sk_model=estimator, name="sample_model")

        mlflow.log_params(best_params)
        mlflow.log_metric("mae", metric)
        mlflow.log_input(dataset, context="training")

        mlflow.set_tag("Training Info", "Basic  model for sample data")

    return model_info


if __name__ == "__main__":
    print(track_best_params("sample", "data/"))
