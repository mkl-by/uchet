import sqlite3
import configg
from flask import g
import math
import time

def connect_db():
    con = sqlite3.connect(configg.DATABASE)
    con.row_factory = sqlite3.Row
    return con

def create_db():
    """Создаем таблицы в базе данных"""
    db = connect_db()
    with open('sql_base.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'): #если линк дб есть, то соединение уже установлено
        g.link_db = connect_db()
    return g.link_db

class readdatabaseall():
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getdata(self):
        #выборка всех данных
        sql = 'SELECT * FROM documents'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("ошибка чтения бд")
        return []

    def adddata(self, data1, data2):
        # вставка данных в таблицу
        try:
            tm = math.floor(time.time())
            print(tm, '!!!!!!!')
            self.__cur.execute("INSERT INTO documents VALUES (NULL, ?,?)", (data1, data2))
            self.__db.commit()
        except sqlite3.Error as e:
            print('ошибка', str(e))
            return False
        return True
