from src import *

# Home Page
@app.get("/")
def home():
    """Retorna uma mensagem indicando que a API está funcionando."""
    return {"Athletes Api": "Home Page"}

# Get Athletes
@app.get("/athletes/")
async def get_athletes():
    """Retorna todos os atletas cadastrados ou uma mensagem de ausência de atletas."""
    try:
        BD.query("SELECT * FROM Athletes")
        res = BD.cur.fetchall()
        if not res:
            return {"message": "Não há atletas cadastrados."}
        else: 
            return res 
    except Exception as e:
        return {"error": f"Erro ao buscar atletas: {e}"}

# Get Athlete
@app.get("/athletes/{athlete_id}")
async def get_athlete(athlete_id: int):
    """Retorna o atleta com o ID fornecido ou uma mensagem se não encontrado."""
    BD.query("SELECT * FROM Athletes WHERE id = ? ", (athlete_id,))
    res = BD.cur.fetchone()
    if not res:
        return {"message": "Atleta não encontrado."}
    else:
        return res

# Create Athlete
@app.post("/athletes/")
async def create_athlete(athlete: Athlete) -> dict:
    """Cria um novo atleta e retorna uma mensagem de confirmação."""
    athlete_values = tuple(athlete.dict().values())
    BD.query("INSERT INTO Athletes (name, cpf, age, weight, height, sex) VALUES (?, ?, ?, ?, ?, ?)", athlete_values)
    category_values = (BD.cur.lastrowid, athlete.name, athlete.weight)
    BD.query("INSERT INTO Categories (athlete_id, name, weight) VALUES (?, ?, ?)", category_values)
    return {"Atleta": "Criado!"}

# Update Athlete
@app.put("/athletes/{athlete_id}")
async def update_athlete(athlete_id, athlete: Athlete) -> dict:
    """Atualiza os dados do atleta com o ID fornecido e retorna uma mensagem de confirmação."""
    try:
        athlete_values = tuple(athlete.dict().values()) + (athlete_id,)
        BD.query("UPDATE Athletes SET name = ?, cpf = ?, age = ?, weight = ?, height = ?, sex = ? WHERE id = ?", athlete_values)
        return {"mensagem": f"Atleta com ID {athlete_id} atualizado com sucesso!"}
    except Exception as e:
        return {"error": f"Erro ao atualizar o atleta: {e}"}

# Delete Athlete
@app.delete("/athletes/{athlete_id}")
async def delete_athlete(athlete_id: int) -> dict:
    """Deleta o atleta com o ID fornecido e retorna uma mensagem de confirmação."""
    BD.query("DELETE FROM Athletes WHERE id = ?", (athlete_id,))
    BD.query("DELETE FROM Categories WHERE athlete_id  = ?", (athlete_id,))
    return {"message": f"Atleta com ID {athlete_id} deletado com sucesso!"}

if __name__ == "__main__":
    uvicorn.run('main:app', host= '0.0.0.0', port=8000, log_level='info', reload= True)
