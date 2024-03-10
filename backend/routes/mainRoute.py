from fastapi import APIRouter, Body, Response
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from sockets import ConnectionManager
from datetime import datetime
import json

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Data from UI: {data}")
            message = {"time":current_time,"clientId":client_id,"message":data}
            print(f"Message from Backend: {message}")
            await manager.send_personal_message(json.dumps(message), websocket)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {"time":current_time,"clientId":client_id,"message":"Offline"}
        await manager.broadcast(json.dumps(message))