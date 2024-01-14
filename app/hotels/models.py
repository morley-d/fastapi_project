from app.database import Base
from sqlalchemy import Column, Integer, String

class Hotels(Base):
  __tablename__ = "hotels
  
  id = Column(Integer)
  name = Column(String)
  location = Column(String)
  services = Column(JSON)
  rooms_quantity = Column(Integer)
  image_id = Column(Integer)
