from app.models.model import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://admin_db:abcd1234@localhost:5432/dev_db')
Session = sessionmaker(bind=engine)
session = Session()

user = [
    User(username='testuser',email='testusr@books.com',pw_hash='abc123')
    ]

# Create a new user and insert it into the database

for _ in user:
    session.add(_)
    
session.commit()
session.close()