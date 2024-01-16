from app.database import Base
from sqlalchemy import JSON, Column, Computed, Date, ForeignKey, Integer, String

class Users(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  email = Column(String)
  hashed_password = Column(String)
