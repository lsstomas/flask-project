from decouple import config


class Config:
    MYSQL_HOST = config("MYSQL_HOST")
    MYSQL_PORT = config("MYSQL_PORT", default=3306, cast=int)
    MYSQL_USER = config("MYSQL_USER")
    MYSQL_PASSWORD = config("MYSQL_PASSWORD")
    MYSQL_DB = config("MYSQL_DB")
