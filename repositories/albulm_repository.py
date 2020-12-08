from db.run_sql import run_sql
from models.albulm import Albulm
from models.artist import Artist

def save(albulm):
    sql = "INSERT INTO albulms (title, genre) VALUES (%s, %s) RETURNING *"
    values = [albulm.title, albulm.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    albulm.id = id
    return albulm

