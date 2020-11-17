from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#App instance
app = Flask("CTH")
app.config['SECRET_KEY'] = '34f17fc6c2d3dbc65842162b549486f6764c9c1462317f5607bd36f93c8d3986'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ewlsfolgbjbyin:34f17fc6c2d3dbc65842162b549486f6764c9c1462317f5607bd36f93c8d3986@ec2-34-235-62-201.compute-1.amazonaws.com:5432/d662524kgh9iqj'

db = SQLAlchemy(app)