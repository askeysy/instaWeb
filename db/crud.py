from sqlalchemy.orm import Session
from . import models
from datetime import datetime, timedelta

def create_business(db: Session, name: str | None = None):
    business = models.Business(name=name)
    db.add(business)
    db.commit()
    db.refresh(business)
    return business


def save_instagram_connection(db: Session, business_id: str, ig_user_id: str, page_id: str, token: str, expires_in: int):
    expires_at = datetime.utcnow() + timedelta(seconds=expires_in)

    conn = models.InstagramConnection(
        business_id=business_id,
        ig_user_id=ig_user_id,
        page_id=page_id,
        access_token=token,
        expires_at=expires_at
    )

    db.add(conn)
    db.commit()
    db.refresh(conn)
    return conn


def get_business_by_ig_user(db: Session, ig_user_id: str):
    return db.query(models.InstagramConnection).filter_by(ig_user_id=ig_user_id).first()
