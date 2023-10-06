import uuid
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, UniqueConstraint
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker
from passlib.context import CryptContext
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

Base = declarative_base() # For Model Migrations

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    
    @classmethod
    def create_user(cls, username, email, password):
        try:
            new_user = cls(username=username, email=email, pw_hash=password)
            session.add(new_user)
            session.commit()
            return "User created successfully"
        except IntegrityError as e:
            # Handle unique constraint violation (e.g., duplicate username or email)
            session.rollback()
            return "User with the same username or email already exists"
    
    def verify_password(self, password):
        return password_context.verify(password, self.pw_hash)

@event.listens_for(User, 'before_insert')
def hash_user_password(mapper, connection, target):
    # Hash the user's password before insertion
    target.pw_hash = password_context.hash(target.pw_hash)


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

if __name__ == "__main__":

    print("Testing model.py")

    user = [
        User(username='admin',email='admin@books.com',pw_hash='abc123')
        ]

    engine = create_engine('postgresql+psycopg2://admin_db:abcd1234@localhost:5432/dev_db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new user and insert it into the database
    # new_user = User(username='Test User', email='test@example.com', pw_hash='abc123')
    # session.add(new_user)
    # session.commit()

    for _ in user:
        session.add(_)

    session.commit()
    session.close()

    