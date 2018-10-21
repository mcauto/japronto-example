import os

class Config:
    APP_ENV =  os.getenv('APP_ENV', 'production')
    SECRET_KEY = os.getenv('APP_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'front/dist')

    HOST = '0.0.0.0'
    PORT = '5000'
    DEBUG = True

    LOG_PATH = os.path.abspath(APP_DIR)+"/log"

    MYSQL_DATABASE_USERNAME='root'
    MYSQL_DATABASE_PASSWORD='japronto'
    MYSQL_DATABASE_NAME='japronto'
#    MYSQL_DATABASE_HOST='localhost'
    MYSQL_DATABASE_HOST='mysql_japronto'
    MYSQL_PORT=os.getenv('MYSQL_PORT','3306')

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(DB_USER=MYSQL_DATABASE_USERNAME,
                                                             DB_PASS=MYSQL_DATABASE_PASSWORD,
                                                             DB_ADDR=MYSQL_DATABASE_HOST,
                                                             DB_PORT=MYSQL_PORT,
                                                             DB_NAME=MYSQL_DATABASE_NAME)
