import requests
from config import APP_ID, APP_SECRET, REDIRECT_URI

from db.session import SessionLocal
from db.crud import create_business, save_instagram_connection


def build_auth_url():
    scopes = ",".join([
        "instagram_basic",
        "instagram_manage_messages",
        "pages_show_list",
        "pages_read_engagement"
    ])

    return (
        "https://api.instagram.com/oauth/authorize"
        f"?client_id={APP_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={scopes}"
        "&response_type=code"
    )


async def exchange_code_for_tokens(code: str):
    # 1. Short-lived token
    token_res = requests.post(
        "https://api.instagram.com/oauth/access_token",
        data={
            "client_id": APP_ID,
            "client_secret": APP_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code": code,
        }
    ).json()

    short_token = token_res["access_token"]
    user_id = token_res["user_id"]

    # 2. Long-lived token
    long_res = requests.get(
        "https://graph.instagram.com/access_token",
        params={
            "grant_type": "ig_exchange_token",
            "client_secret": APP_SECRET,
            "access_token": short_token,
        }
    ).json()

    long_token = long_res["access_token"]
    expires_in = long_res["expires_in"]

    # 3. Зберігаємо в БД
    db = SessionLocal()

    # Створюємо бізнес (поки без назви)
    business = create_business(db)

    # Поки що page_id не отримуємо — додамо на наступному кроці
    save_instagram_connection(
        db=db,
        business_id=business.id,
        ig_user_id=user_id,
        page_id=None,
        token=long_token,
        expires_in=expires_in
    )

    return {
        "business_id": business.id,
        "ig_user_id": user_id,
        "access_token": long_token,
        "expires_in": expires_in
    }
