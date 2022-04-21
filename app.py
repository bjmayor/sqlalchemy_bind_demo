from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config #导入1中的配置

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)