from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.layers import LSTM, Dense
import joblib

# Load the trained model
model = load_model('fire_prediction_model.h5')

# Load the scaler (used during training)
scaler = joblib.load('scaler.pkl')

class FirePredictionInput(BaseModel):
    temp: float
    RH: float

@app.post("/predict")
def predict_fire(data: FirePredictionInput):
    try:
        # Convert input data to numpy array
        input_data = np.array([[data.temp, data.RH]])

        # Apply the same scaling as during training
        input_data_scaled = scaler.transform(input_data)

        # Predict using the model
        prediction = model.predict(input_data_scaled)
        probability = float(prediction[0][0])

        # Return 1 if probability >= 0.5, otherwise 0
        fire = 1 if probability >= 0.5 else 0

        return {"fire": fire, "probability": probability}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing input: {e}")

