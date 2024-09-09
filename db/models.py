from sqlalchemy import (Column, Integer, String, DateTime,
                        BigInteger, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(55), nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level", nullable=True)
    reg_date = Column(DateTime, default=datetime.now())


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    timer = Column(DateTime)


class LiderResult(Base):
    __tablename__ = "results"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String, nullable=False)

    user_fk = relationship(User, lazy="subquery")



class UserAnswer(Base):
    __tablename__ = "useranswers"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    level = Column(String)
    user_answer = Column(String)
    correctness = Column(Boolean, default=False)
    timer = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery", foreign_keys=[user_id, level])
    question_fk = relationship(Question, lazy="subquery")
