from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Load saved model
model = joblib.load("./energy_model.pkl") 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] if frontend runs there
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, OPTIONS etc.
    allow_headers=["*"],
)
# Input schema
class EnergyInput(BaseModel):
    Global_reactive_power: float
    Voltage: float
    Global_intensity: float
    Sub_metering_1: float
    Sub_metering_2: float
    Sub_metering_3: float
    Avg_Intensity_1h: float
    Avg_Intensity_1d: float
@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.post("/predict")
def predict_energy(data: EnergyInput):
    features = np.array([[data.Global_reactive_power,
                          data.Voltage,
                          data.Global_intensity,
                          data.Sub_metering_1,
                          data.Sub_metering_2,
                          data.Sub_metering_3,
                          data.Avg_Intensity_1h,
                          data.Avg_Intensity_1d]])
    
    prediction = model.predict(features)[0]
    
    # Convert numpy.float32 -> Python float
    return {"predicted_Global_active_power": float(prediction)}
