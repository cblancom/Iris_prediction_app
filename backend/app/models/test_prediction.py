import joblib
import numpy as np

model_path = "backend/app/models/iris_model.joblib"

model = joblib.load(model_path)
prediction = model.predict(np.array([1, 1, 0, 0]).reshape(1, -1))
print(prediction.shape)
print(type(prediction))
