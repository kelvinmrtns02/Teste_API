from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Tarefa(Base):
    __tablename__ = "Tarefas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    titulo = Column(String, nullable=True)
    status = Column(String, nullable=False)