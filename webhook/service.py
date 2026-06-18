from db.session import SessionLocal
from db.crud import get_business_by_ig_user

async def handle_webhook_event(data: dict):
    db = SessionLocal()

    ig_user_id = data["entry"][0]["id"]
    business = get_business_by_ig_user(db, ig_user_id)

    if business:
        print("Подія від бізнесу:", business.id)
