from models import Base
from services.database import engine


def create_tables():
    Base.metadata.create_all(bind=engine)
