import databases
from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "sqlite:///./equipment.db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata = MetaData()



