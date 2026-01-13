import joblib


def load_model(path: str):
    model = joblib.load(path)
    return model
