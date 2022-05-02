import os

from sqlalchemy import (create_engine, MetaData, Table, Integer, String, 
    Column, DateTime, ForeignKey, Numeric, func, Text)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

dbLogin = os.getenv('DB_USER')
dbPass = os.getenv('DB_PASSWORD')
dbName = os.getenv('DB_NAME')

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, nullable=False)
    question_text = Column(Text, nullable=False)
    answer_text = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False, server_default=func.now())

if __name__ == '__main__':
    engine = create_engine(
        f"postgresql+psycopg2://{dbLogin}:{dbPass}@postgres_db_container/{dbName}", echo=True
    )
    Base.metadata.create_all(engine)