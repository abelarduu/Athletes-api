from fastapi import FastAPI
from src.database import dataBase
from src.models import Athlete, Category
import uvicorn

# Inicializa a aplicação FastAPI
# Instancia o banco de dados.
app = FastAPI(title="Athetles_Api")
BD = dataBase()  