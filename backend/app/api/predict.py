import joblib
from pathlib import Path
from fastapi import APIRouter
from schemas.input_output import InputFeatures, Prediction, PredictionResponse
from utils.loader import load_model
from database.database import SessionDep
import numpy as np
from sqlmodel import select, func

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "iris_model.joblib"

# model = joblib.load(MODEL_PATH)
router = APIRouter()


@router.post("/predict/", response_model=PredictionResponse)
def make_prediction(
    features: InputFeatures,
    session: SessionDep,
):
    model = load_model(MODEL_PATH)
    prediction = model.predict(
        np.array(
            [features.feature1, features.feature2, features.feature3, features.feature4]
        ).reshape(1, -1)
    )

    db_prediction = Prediction(
        feature1=features.feature1,
        feature2=features.feature2,
        feature3=features.feature3,
        feature4=features.feature4,
        predicted_class=float(prediction.item()),
    )

    session.add(db_prediction)
    session.commit()
    session.refresh(db_prediction)
    # return prediction.item()
    return db_prediction
