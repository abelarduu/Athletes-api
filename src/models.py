from pydantic import BaseModel
          
class Athlete(BaseModel):
        name: str
        cpf: str
        age: int
        weight: float
        height: float
        sex: str

class Category(BaseModel):
        name: str
        weight:float