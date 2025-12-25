import pandas as pd


def build_and_save_datset():
    "return csv file"

    data_dic = {"feature_a": [100, 90], "target": [0, 1]}

    dataset = pd.DataFrame(data_dic)
    return dataset.to_csv("tests/assets/sample.csv")


if __name__ == "__main__":
    build_and_save_datset()
