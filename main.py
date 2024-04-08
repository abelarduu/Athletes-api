from athletes_api import *
from athletes_api.models import *
import uvicorn

@app.get("/")
def home():
    return {"Home": "Page"}

#Create Athlete
@app.post("/athletes/")
async def create_athlete(athlete: Athlete) -> dict:
    athlete_values = tuple(athlete.dict().values())
    BD.query("INSERT INTO Athletes (name, cpf, age, weight, height, sex) VALUES (?, ?, ?, ?, ?, ?)", athlete_values)
    
    category_values= (BD.cur.lastrowid, athlete.name, athlete.weight)
    BD.query("INSERT INTO Categories (athlete_id, name, weight) VALUES (?, ?, ?)", category_values)
    return {"Atleta": "Criado!"}

#Get Athlete
@app.get("/athletes/{athlete_id}")
async def get_athlete(athlete_id: int) -> dict:
    BD.query("SELECT * FROM Athletes WHERE id = ? ", (athlete_id,))
    res_athlete= BD.cur.fetchone()

    if res_athlete:
        # Obtendo os nomes das colunas
        # Criando um dicionário combinando os nomes das colunas com os valores da linha
        columns = [desc[0] for desc in BD.cur.description]
        athlete_dict = dict(zip(columns, res_athlete))
        return athlete_dict

    else:
        return {"message": "Atleta não encontrado."}

#update Athlete
@app.put("/athletes/{athlete_id}")
def update_athlete(athlete_id) -> dict:
    athlete_values = tuple(athlete.dict().values())
    BD.query("UPDATE Athletes SET name = ?, cpf = ?, age = ?, weight = ?, height = ?, sex = ? WHERE id = ?", athlete_values)
    return {"mensagem": f"Atleta com ID {athlete_id} atualizado com sucesso!"}

#delete Athlete
@app.delete("/athletes/{athlete_id}")
async def delete_athlete(athlete_id: int) -> dict:
    BD.query("DELETE FROM Athletes WHERE id = ?", (athlete_id,))
    return {"message": f"Atleta com ID {athlete_id} deletado com sucesso!"}

'''
def get_athletes():
    BD.query("SELECT * FROM  Athletes")
    res= BD.cur.fetchall()
    return res'''

if __name__ == "__main__":
    uvicorn.run('main:app', host= '0.0.0.0', port=8000, log_level='info', reload=True)