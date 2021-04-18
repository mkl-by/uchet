import sqlite3
import configg
from flask import g

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

    if not hasattr(g, 'link_db'): #если линк дб есть то соединение уже установлено
        g.link_db = connect_db()
    return g.link_db

