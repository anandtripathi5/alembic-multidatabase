from sqlalchemy import Text, Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FirstTest(Base):
    __table_args__ = ({'schema': 'first'})
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)


class SecondTest(Base):
    __table_args__ = ({'schema': 'second'})
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)


class ThirdTest(Base):
    __table_args__ = ({'schema': 'third'})
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)
