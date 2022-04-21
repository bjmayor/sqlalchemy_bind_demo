from models import User, Email 
from sqlalchemy.sql import text,and_,or_
from app import app,db




def feedData():
    db.create_all()
    user = User()
    user.name = "han meimei"
    db.session.add(user)

    email = Email()
    email.email = "dish@qq.com"
    db.session.add(email)
    db.session.commit()

feedData()

if __name__ == '__main__':
    app.run('0.0.0.0',6666)