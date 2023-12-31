from app.env import APPENV
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
import warnings

db_config = APPENV.get_sql()

PGSQL_DATABASE_URL = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
    db_config['user'],
    db_config['password'],
    db_config['host'],
    db_config['port'],
    db_config['db'],
    )

print("DB STR: ", PGSQL_DATABASE_URL)

options = {
    'options': '-c timezone=UTC'
}


try:
    engine = create_engine(PGSQL_DATABASE_URL, connect_args=options)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("Connection String Loaded")
except exc.SQLAlchemyError as e:
    print("SQL Alchemy Create Engine Error: ", e)


@contextmanager
def SessionManager() -> Session:
    db = SessionLocal()
    try:
        yield db
    except Exception as db_exception:
        # if we fail somehow rollback the connection
        warnings.warn("Failed in a DB operation and auto-rollback...")
        db.rollback()
        print(db_exception)
        raise
    finally:
        db.close()


async def paginate(query, page_number=0, page_limit=100):
    length = query.count()
    items = query.offset(page_number).limit(page_limit).all()
    return {"items": items, "total": length, "limit": page_limit, "offset": page_number}

