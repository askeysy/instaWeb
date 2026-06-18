from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from .service import build_auth_url

router = APIRouter()

@router.get("/start")
def start_auth():
    url = build_auth_url()
    return RedirectResponse(url)

@router.get("/callback")
async def auth_callback(code: str):
    try:
        result = await exchange_code_for_tokens(code)
        return JSONResponse({"status": "connected", "data": result})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=400)
