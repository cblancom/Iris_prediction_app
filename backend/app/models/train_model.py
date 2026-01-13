from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

dataset = load_iris()
X = dataset.data
y = dataset.target

print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)
F1 = f1_score(y_test, predictions, average="weighted")

print("Accuracy:", acc)
print("F1 Score:", F1)

# save the model
savepath = "./iris_model.joblib"
joblib.dump(model, savepath)

# print(f"Data shape {X.shape}")
# print(f"Feature 1 range. Min value: {X[:, 0].min()}, Max: {X[:, 0].max()}")
# print(f"Feature 2 range. Min value: {X[:, 1].min()}, Max: {X[:, 1].max()}")
# print(f"Feature 3 range. Min value: {X[:, 2].min()}, Max: {X[:, 2].max()}")
# print(f"Feature 4 range. Min value: {X[:, 3].min()}, Max: {X[:, 3].max()}")
#
# print(f"All feat: Min: {X.min()}, max: {X.max()}")
