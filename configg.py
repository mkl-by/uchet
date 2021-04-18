import os
from app import app

SECRET_KEY = 'sdfgfdgwefsdfsdvf'
DEBUG = True
PORT = 5050
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
print(DATABASE)