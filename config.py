class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kAkA$84kA097@localhost:3306/community_pulse'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
