#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

from sqlalchemy import create_engine
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    chief = Column(String(20))
    access_token = Column(String(20))
    expires_time = Column(String(20))



engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/py')
DBSession = sessionmaker(bind=engine)


session = DBSession()
new_user = User(id='1')






