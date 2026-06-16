from fastapfrom fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "my_secret_token"

@app.get("/")
def root():
    return {"status": "ok"}

# VERIFY WEBHOOK
@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params["hub.challenge"])
    return "Verification failed"

# RECEIVE WEBHOOK EVENTS
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("New Instagram event:", data)
    return {"status": "received"}
i import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "my_secret_token"

@app.get("/")
def root():
    return {"status": "ok"}

# VERIFY WEBHOOK
@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params["hub.challenge"])
    return "Verification failed"

# RECEIVE WEBHOOK EVENTS
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("New Instagram event:", data)
    return {"status": "received"}
