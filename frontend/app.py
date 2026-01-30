import streamlit as st
import requests
import os

# BASE_URL = "http://127.0.0.1:8000/"
# BASE_URL = "http://backend:8000"
# Detectar el entorno
# if os.getenv("DOCKER_ENV"):
#     BASE_URL = "http://backend:8000"
# else:
#     BASE_URL = "http://localhost:8000"
#
BASE_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def main():
    st.title("Iris model prediction")

    feat_1 = st.slider("Feature 1", 0.1, 8.0, 4.0)
    feat_2 = st.slider("Feature 2", 0.1, 8.0, 4.0)
    feat_3 = st.slider("Feature 3", 0.1, 8.0, 4.0)
    feat_4 = st.slider("Feature 4", 0.1, 8.0, 4.0)

    data = {
        "feature1": feat_1,
        "feature2": feat_2,
        "feature3": feat_3,
        "feature4": feat_4,
    }
    response = requests.post(f"{BASE_URL}/predict/", json=data)

    target_names = ["Setosa", "Versicolor", "Virginica"]
    if st.button("Prediction"):
        prediction_data = response.json()
        predicted_class = prediction_data["predicted_class"]
        st.write(f"Prediction is {target_names[predicted_class]}")
        # st.write(f"Prediction is {prediction}")


if __name__ == "__main__":
    main()
