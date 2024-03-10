from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from routes.mainRoute import router as socketRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define endpoint
app.include_router(socketRouter)

@app.get("/welcome")
def Home():
    return "Welcome home"

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to AgentStack API Docs"}

