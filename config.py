class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/user.sqlite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 支持多数据库
    SQLALCHEMY_BINDS = {
        'user': 'sqlite:///data/user.sqlite',
        'email': 'sqlite:///data/email.sqlite',
    }
