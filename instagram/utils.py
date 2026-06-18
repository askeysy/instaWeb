def extract_sender_id(webhook_data: dict) -> str | None:
    try:
        return webhook_data["entry"][0]["messaging"][0]["sender"]["id"]
    except:
        return None
