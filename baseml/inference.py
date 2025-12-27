from baseml.tracker import track_best_params
from baseml.train_models import split_data
import mlflow


def make_inference(dataset_name, tmp, dataset_inf, tmp_info):
    _, X_test, _, _ = split_data(dataset_inf, tmp_info)

    model_info = track_best_params(dataset_name, tmp)
    loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
    predictions = loaded_model.predict(X_test)

    return predictions


if __name__ == "__main__":
    print(make_inference("sample", "data/", "sample", "data/"))
