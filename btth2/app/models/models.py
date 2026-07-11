from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    major = Column(String(50), nullable=False)
    gpa = Column(Float(4, 2), nullable=False)