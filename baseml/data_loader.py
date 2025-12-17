import pandas as pd

def build_path(dataset_name):
    tmp = "data/"
    return tmp + f"{dataset_name}" + ".csv"

def load_data(dataset_name):
    base_url = build_path(dataset_name)
    data_frame = pd.read_csv(base_url)
    return data_frame

    
if __name__ == "__main__":
    print(build_path("sample"))
    print(load_data("sample"))