import uuid

from fastapi import FastAPI
from pydantic import BaseModel

from agents import ask

app = FastAPI()

thread_id = str(uuid.uuid4())


class Question(BaseModel):
    question: str


@app.post("/api/detective")
def detective(payload: Question):
    return {"answer": ask(payload.question, thread_id)}
