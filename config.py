# config.py
import os
class Config:
    # URL de conexão do MySQL para o SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = 'mysql://fatec:F%40tec2022@localhost/clientes_db'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/clientes_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fatec:F%40tec2022@localhost/clientes_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    CORS_HEADERS = 'Content-Type'
    API_TITLE = 'API CRUD Clientes'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'