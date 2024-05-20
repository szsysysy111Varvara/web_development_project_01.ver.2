class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/your_db'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
