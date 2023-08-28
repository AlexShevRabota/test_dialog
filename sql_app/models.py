from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    name = Column(String, default=True)
    surname = Column(String, default=True)
    password = Column(String)

    Restaurant_table = relationship("Restaurant_table", back_populates="owner")



class Restaurant_table(Base):
    __tablename__ = "restaurant_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="Restaurant_table")


# class Reserved_table(Base):
#     __tablename__ = "reserved_table"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     number_people = Column(Integer, index=True)

