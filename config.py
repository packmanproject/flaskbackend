
from flask import Flask
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'uinib'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

port=80
host='192.168.43.182'