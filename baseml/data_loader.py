def build_path(dataset_name):
    tmp = "data/"
    return tmp + f"{dataset_name}" + ".csv"

if __name__ == "__main__":
    print(build_path("sample"))