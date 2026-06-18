import requests
from config import APP_SECRET

def refresh_long_lived_token(access_token: str):
    url = "https://graph.instagram.com/refresh_access_token"
    params = {
        "grant_type": "ig_refresh_token",
        "access_token": access_token
    }
    return requests.get(url, params=params).json()
