from fastapi import Depends, FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field
import models
from models import Todos
from database import engine, SessionLocal
import sqlite3
from typing import Annotated
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str = Field(min_length=3, max_length=100)
    priority : int = Field(gt=0, lt=6)
    complete: bool 

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db : db_dependency, todo_id : int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

@app.get("/todo/name/{todo_title}", status_code=status.HTTP_200_OK)
async def find_todo(db : db_dependency, todo_title : str):
    todo_model = db.query(Todos).filter(Todos.title.ilike(todo_title)).all()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo Not found')

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db : db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()

@app.put("/todo/update/{todo_id}")
async def update_todo(db : db_dependency, todo_request : TodoRequest, todo_id : int = Path(gt=0)):
    todo_model  = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/delete/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo_model)
    db.commit()
