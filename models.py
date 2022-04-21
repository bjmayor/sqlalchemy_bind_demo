from app import db  #从2中导入db

class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'user' # 指定数据库
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)

    #to_json 方便后面查询使用
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
         return '<users %r>' % self.id

class Email(db.Model):
    __tablename__ = 'emails'
    __bind_key__ = 'email' # 指定数据
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)

    #to_json 方便后面查询使用
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def __repr__(self):
         return '<emails %r>' % self.id