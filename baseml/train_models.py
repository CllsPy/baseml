from baseml.data_loader import load_data
from sklearn.model_selection import train_test_split


def split_data(dataset_name: str, target: str):
    data_frame = load_data(dataset_name)

    X = data_frame.drop(target, axis=1)
    y = data_frame.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


if __name__=='__main__':
    X_train, X_test, y_train, y_test = (split_data("sample", "target"))
    
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)
    print(X_test.shape[1], X_train.shape[1])
    