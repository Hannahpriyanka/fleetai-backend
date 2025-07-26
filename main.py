from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow your React app origin(s)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Vehicle(BaseModel):
    vehicleId: str
    model: str
    latitude: float
    longitude: float
    speed: float
    engineTemp: float
    isFaulty: bool

# Sample data store
vehicles_db: List[Vehicle] = [
    Vehicle(
        vehicleId="string",
        model="string",
        latitude=0.0,
        longitude=0.0,
        speed=0.0,
        engineTemp=0.0,
        isFaulty=True
    ),
    Vehicle(
        vehicleId="abc123",
        model="Tesla Model 3",
        latitude=37.7749,
        longitude=-122.4194,
        speed=65.0,
        engineTemp=75.0,
        isFaulty=False
    )
]

@app.get("/")
def root():
    return {"message": "FleetAI Vehicle API"}

@app.get("/vehicles/", response_model=List[Vehicle])
def get_vehicles():
    return vehicles_db

@app.post("/vehicles/")
def update_vehicle(vehicle: Vehicle):
    # Check if vehicle exists; if yes, update it, else add new
    for idx, v in enumerate(vehicles_db):
        if v.vehicleId == vehicle.vehicleId:
            vehicles_db[idx] = vehicle
            return {"message": "Vehicle updated", "data": vehicle}
    vehicles_db.append(vehicle)
    return {"message": "Vehicle added", "data": vehicle}
