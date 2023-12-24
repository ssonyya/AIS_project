from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime


# Объявление декларативного (описательного) метода представления БД
Base = declarative_base()


class Car(Base):
    __tablename__ = "Car"

    name = Column('name', String(6), primary_key=True)  # объявление первичного ключа
    coord_x = Column('coord_x', Numeric, nullable=False)
    coord_y = Column('coord_y', Numeric, nullable=False)
    acc = Column('acc', Integer, nullable=False)
    oil = Column('oil', Integer, nullable=False)
    fuel = Column('fuel', Numeric, nullable=False)
    temp = Column('temp', Numeric, nullable=False)
    fuel_consumption = Column('fuel_consumption', Numeric, nullable=False)
    milease = Column('milease', Integer, nullable=False)

    status = Column(Integer, ForeignKey('Errors.id'))


class Errors(Base):
    __tablename__ = "Errors"

    id = Column('id', Integer, primary_key=True)
    not_errors = Column('not_errors', Boolean, nullable=False)
    error_acc = Column('error_acc', Boolean, nullable=False)
    error_oil = Column('error_oil', Boolean, nullable=False)
    error_fuel = Column('error_fuel', Boolean, nullable=False)
    error_temp = Column('error_temp', Boolean, nullable=False)
    error_fuel_consumption = Column('error_fuel_consumption', Boolean, nullable=False)

    advice = Column(Integer, ForeignKey('Recommendation.id'))


class Recommendation(Base):
    __tablename__ = "Recommendation"

    id = Column('id', Integer, primary_key=True)
    info = Column('info', String(100), nullable=False)
