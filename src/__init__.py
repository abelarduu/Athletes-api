from fastapi import FastAPI
from src.database import dataBase
from src.models import Athlete, Category

app = FastAPI(title= "Athetles_Api")
BD= dataBase()
