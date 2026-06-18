from fastapi import FastAPI
from webhook.router import router as webhook_router
from auth.router import router as auth_router

app = FastAPI()

app.include_router(webhook_router, prefix="/webhook")
app.include_router(auth_router, prefix="/auth")
