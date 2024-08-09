from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    slug = Column(String, unique = True, index = True)
    # description = Column(String)
    # price = Column(Integer)
    # image_url = Column(String)
    # stock = Column(Integer)
    # user_id = Column(Integer, ForeignKey('categories.id'))
    # rating = Column(Float)
    # is_active = Column(Boolean, default = True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)


    task = relationship('Task', back_populates = 'users')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))



