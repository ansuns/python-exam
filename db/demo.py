#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'


import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='py')
cursor = conn.cursor();
cursor.execute('insert into user (name, chief, access_token, expires_time) values (%s, %s, %s, %s)', [1,1,1,1])

conn.commit()
cursor.close()
