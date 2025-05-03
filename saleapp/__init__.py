from flask import Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saleapp:123456@localhost/saledb'
# labsaledb: co so du lieu rong
# charset=ut8mb4: doc dinh dang unikey de hon
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db  = SQLAlchemy(app=app)
