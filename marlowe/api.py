from fastapi import FastAPI, Response, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agents import ask
from fastapi.middleware.cors import CORSMiddleware
from handlers import create_case

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)



class ChatRequest(BaseModel):
    id: str
    messages: list[dict]

class CreateCaseRequest(BaseModel):
    scene_evidence: str | None=""
    crime_report: str | None=""
    records: str | None=""
    security_log: str | None=""
    suspects: str | None=""

@app.post("/api/detective")
def detective(payload: ChatRequest):
    last_message = payload.messages[-1]
    question = "".join(part["text"] for part in last_message["parts"] if part["type"] == "text")
    return StreamingResponse(ask(question, payload.id), media_type="text/event-stream")

@app.post("/api/detective/create-case")
def new_case(payload: CreateCaseRequest, response: Response):
    res = create_case(payload.scene_evidence, payload.crime_report, payload.records, payload.security_log, payload.suspects)
    response.status_code = res["create_case_status"]
    return res["create_case_content"]
