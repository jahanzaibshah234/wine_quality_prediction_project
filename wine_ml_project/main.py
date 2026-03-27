from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load the saved model
model = joblib.load("wine_quality.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define a request model for the input
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Wine Quality Prediction API! Use the /predict endpoint to predict wine quality."
    }


# Prediction endpoint
@app.post("/predict")
def predict(wine: WineFeatures):
    # Extract the features from incoming request
    features = np.array([[
        wine.fixed_acidity,
        wine.volatile_acidity,
        wine.citric_acid,
        wine.residual_sugar,
        wine.chlorides,
        wine.free_sulfur_dioxide,
        wine.total_sulfur_dioxide,
        wine.density,
        wine.pH,
        wine.sulphates,
        wine.alcohol
    ]
    ])
     # Make prediction using the model
    prediction = model.predict(features)

    # Return the result
    return {"predicted_quality": str(prediction[0])}

