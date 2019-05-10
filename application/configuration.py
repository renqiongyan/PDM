from pathlib import Path


class Configuration:
    APP_DIR = Path(__file__).resolve().parent
    BASE_DIR = APP_DIR.parent
    # DATABASE = 'mysql://app:123456@localhost:3306/app'
    DB_FILE = str(BASE_DIR.joinpath('app.db'))
    DATABASE = f'sqliteext:///{DB_FILE}'
    SECRET_KEY = '123456abcdef'
    WTF_CSRF_ENABLED = False


class DevelopmentConfiguration(Configuration):
    DEBUG = True


class TestingConfiguration(Configuration):
    TESTING = True


class ProductionConfiguration(Configuration):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}