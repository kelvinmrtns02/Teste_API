from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Tarefa
from schemas import TarefaCreate, TarefaUpdate, TarefaResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Tarefas", description="Uma API simples para gerenciar tarefas.", version="1.0.0")

@app.get("/tarefas", response_model=List[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(Tarefa).all()

@app.post("/tarefas", response_model=TarefaResponse, status_code=201)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    nova_tarefa = Tarefa(**tarefa.model_dump())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas/{id}", response_model=TarefaResponse)
def buscar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@app.put("/tarefas/{id}", response_model=TarefaResponse)
def atualizar_tarefa(id: int, dados: TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tarefa, campo, valor)
    
    db.commit()
    db.refresh(tarefa)
    return tarefa

@app.delete("/tarefas/{id}", status_code=204)
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()