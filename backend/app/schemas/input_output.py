from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class InputFeatures(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


class PredictionResponse(BaseModel):
    """Schema para la respuesta"""

    id: int
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    predicted_class: int
    timestamp: datetime


class Prediction(SQLModel, table=True):
    """
    Model to store prediction results along with input features and timestamp.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    predicted_class: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
