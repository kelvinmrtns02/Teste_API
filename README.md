# 📝 Teste_API

API REST para gerenciamento de tarefas, desenvolvida com **FastAPI** e **SQLAlchemy**.

## 🚀 Tecnologias
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## 📋 Endpoints
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /tarefas | Lista todas as tarefas |
| POST | /tarefas | Cria uma nova tarefa |
| GET | /tarefas/{id} | Busca tarefa por ID |
| PUT | /tarefas/{id} | Atualiza uma tarefa |
| DELETE | /tarefas/{id} | Remove uma tarefa |

## ▶️ Como executar
```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Acesse a documentação em: http://127.0.0.1:8000/docs
