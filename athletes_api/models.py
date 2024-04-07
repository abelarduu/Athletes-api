from pydantic import BaseModel
          
class Athlete(BaseModel):
        name: str
        cpf: str
        age: int
        weight: float
        height: float
        sex: str

class Training_Center(BaseModel):
        name: str
        address: str
        owner: float

class Category(BaseModel):
        name: str
        weight:float