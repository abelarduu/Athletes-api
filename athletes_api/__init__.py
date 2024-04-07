from fastapi import FastAPI
from workout_api.database import dataBase
from workout_api.models import Athlete, Training_Center, Category

app = FastAPI(title= "WorkoutApi")
BD= dataBase()