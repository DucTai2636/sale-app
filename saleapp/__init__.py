from flask import Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql:///root: 12345678@localhost/labsaledb?charset=ut8mb4"
# labsaledb: co so du lieu rong
# charset=ut8mb4: doc dinh dang unikey de hon
db  = SQLAlchemy(app = app)
