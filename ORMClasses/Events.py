from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    
    def __repr__(self) -> str:
        return f"id={self.id!r}, user_id={self.user_id!r}, title={self.title!r}, description={self.description!r})"
    
    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description
        }