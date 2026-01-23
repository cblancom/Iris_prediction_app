import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine, SQLModel
from sqlmodel.pool import StaticPool

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from main import app
from database.database import get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_predict_sucesss(client: TestClient):
    input_data = {"feature1": 10.5, "feature2": 5.2, "feature3": 3.1, "feature4": 7.8}

    response = client.post("/predict/", json=input_data)

    assert response.status_code == 200

    data = response.json()

    assert "id" in data, "Debe incluir un ID"
    assert "feature1" in data, "Debe retornar feature1"
    assert "feature2" in data, "Debe retornar feature2"
    assert "feature3" in data, "Debe retornar feature3"
    assert "feature4" in data, "Debe retornar feature4"
    assert "predicted_class" in data, "Debe incluir la predicción"
    assert "timestamp" in data, "Debe incluir timestamp"

    # Verificar que los valores son correctos
    assert data["feature1"] == 10.5
    assert data["feature2"] == 5.2
    assert data["feature3"] == 3.1
    assert data["feature4"] == 7.8

    # Verificar que la clase predicha es válida (0=Setosa, 1=Versicolor, 2=Virginica)
    assert data["predicted_class"] in [0, 1, 2], "La clase debe ser 0, 1 o 2"
