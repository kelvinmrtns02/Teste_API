from pydantic import BaseModel
from typing import Optional

class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    
class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[bool] = None
    
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    status: bool
    
class Config:
    from_attributes = True