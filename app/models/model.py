import uuid
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class BaseModel(Base):
    __abstract__ = True

    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    pw_hash = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"User id={self.auto_id}, uuid={self.uuid}, date={self.date_created}, updated={self.date_updated}\
                username={self.username},email={self.email}"
        )

class Book(BaseModel):
    __tablename__ = 'books'

    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(Date, nullable=True)
    ISBN = Column(String, unique=True, nullable=True)

    __table_args__ = (
        UniqueConstraint('title', 'author', name='uix_title_author'),
    )

    def __repr__(self):
        return (
            f"Book id={self.auto_id}, uuid={self.uuid}, date={self.date_created}, updated={self.date_updated}\
                author={self.author},title={self.title}"
        )

