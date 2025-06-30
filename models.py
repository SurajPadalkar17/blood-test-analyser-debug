# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ReportResult(Base):
    __tablename__ = "report_results"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)
    result = Column(Text, nullable=False)
    filename = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
