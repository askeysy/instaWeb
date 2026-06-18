import requests

def send_message(page_id: str, access_token: str, recipient_id: str, text: str):
    url = f"https://graph.facebook.com/v19.0/{page_id}/messages"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text},
        "messaging_type": "RESPONSE"
    }

    res = requests.post(url, json=payload, params={"access_token": access_token})
    return res.json()


def get_ig_profile(ig_user_id: str, access_token: str):
    url = f"https://graph.instagram.com/{ig_user_id}"
    params = {
        "fields": "id,username,account_type",
        "access_token": access_token
    }
    return requests.get(url, params=params).json()


def get_page_info(access_token: str):
    url = "https://graph.facebook.com/v19.0/me/accounts"
    return requests.get(url, params={"access_token": access_token}).json()
