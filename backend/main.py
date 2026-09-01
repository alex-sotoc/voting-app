from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI(
    title="Voting App API",
    description="Backend para gestión de votaciones y encuestas en tiempo real",
    version="1.0.0"
)

# Permitir conexiones desde la app de Flutter (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar Base de Datos SQLite
def init_db():
    conn = sqlite3.connect("voting.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            votes INTEGER DEFAULT 0
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM candidate")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO candidate (name, votes) VALUES ('Opción A: Flutter', 0)")
        cursor.execute("INSERT INTO candidate (name, votes) VALUES ('Opción B: React Native', 0)")
        cursor.execute("INSERT INTO candidate (name, votes) VALUES ('Opción C: Swift/Kotlin', 0)")
    conn.commit()
    conn.close()

init_db()

@app.get("/candidates")
def get_candidates():
    conn = sqlite3.connect("voting.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, votes FROM candidate")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "votes": r[2]} for r in rows]

@app.post("/vote/{candidate_id}")
def register_vote(candidate_id: int):
    conn = sqlite3.connect("voting.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE candidate SET votes = votes + 1 WHERE id = ?", (candidate_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    conn.commit()
    conn.close()
    return {"message": "Voto registrado exitosamente"}