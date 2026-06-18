from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .session import Base
import uuid

def gen_uuid():
    return str(uuid.uuid4())

class Business(Base):
    __tablename__ = "businesses"

    id = Column(String, primary_key=True, default=gen_uuid)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    instagram = relationship("InstagramConnection", back_populates="business", uselist=False)


class InstagramConnection(Base):
    __tablename__ = "instagram_connections"

    id = Column(String, primary_key=True, default=gen_uuid)
    business_id = Column(String, ForeignKey("businesses.id"))

    ig_user_id = Column(String)
    page_id = Column(String)
    access_token = Column(String)
    expires_at = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)

    business = relationship("Business", back_populates="instagram")
