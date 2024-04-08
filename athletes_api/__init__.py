from fastapi import FastAPI
from athletes_api.database import dataBase
from athletes_api.models import Athlete, Training_Center, Category

app = FastAPI(title= "WorkoutApi")
BD= dataBase()