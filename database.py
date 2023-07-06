from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql://postgres:41418002818@localhost/postgres', echo=True)
Base = declarative_base()
# for maintaining each transaction session.
SessionLocal = sessionmaker(bind=engine)
