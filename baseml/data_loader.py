import pandas as pd

def build_path(dataset_name, tmp):
    """
    we need to set tmp as tmp/
    e.g data/
    
    :param dataset_name: Description
    :param tmp: Description
    """
    return tmp + f"{dataset_name}" + ".csv"

def load_data(dataset_name, tmp):
    base_url = build_path(dataset_name, tmp)
    data_frame = pd.read_csv(base_url)
    return data_frame


if __name__ == "__main__":
    dataset_name = "sample"
    tmp = "data/"
    print(build_path(dataset_name, tmp))
    print(load_data(dataset_name, tmp))