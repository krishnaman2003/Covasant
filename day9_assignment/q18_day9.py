from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import os

app = FastAPI()

def get_db():
    DATABASE = os.path.join(".", "people.db")
    db = create_engine("sqlite:///" + DATABASE)
    return db

def get_age_from_db(name: str):
    eng = get_db()
    try:
        with eng.connect() as conn:
            result = conn.execute(text("select age from people where name = :name"),
                                  dict(name=name)).fetchone()
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"Details for '{name}' not found")

class HelloData(BaseModel):
    name: str = "abc"
    format: str = "json"

@app.get("/helloj/{name}/{format}")
def read_hello_path(name: str, format: str = "json"):
    age = get_age_from_db(name)
    return {"name": name, "age": age, "source": "path", "format_requested": format}

@app.get("/helloj")
def read_hello_query(name: str = "abc", format: str = "json"):
    age = get_age_from_db(name)
    return {"name": name, "age": age, "source": "query", "format_requested": format}

@app.post("/helloj")
def create_hello(data: HelloData):
    age = get_age_from_db(data.name)
    return {"name": data.name, "age": age, "source": "post_body", "format_requested": data.format}