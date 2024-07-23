from pydantic import BaseModel
          
class Athlete(BaseModel):
    """Modelo de dados para um atleta."""
    name: str
    cpf: str
    age: int
    weight: float
    height: float
    sex: str

class Category(BaseModel):
    """Modelo de dados para uma categoria de atleta."""
    name: str
    weight: float
