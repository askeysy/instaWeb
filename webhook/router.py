from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from .service import handle_webhook_event
from config import VERIFY_TOKEN

router = APIRouter()

@router.get("/")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge, status_code=200)

    return {"status": "error", "message": "Invalid token"}

@router.post("/")
async def receive_webhook(request: Request):
    data = await request.json()
    await handle_webhook_event(data)
    return {"status": "received"}
