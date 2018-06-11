
POSTGRES = {
    'user': 'postgres',
    'pw': '88888888',
    'db': 'mini_hrd',
    'host': 'localhost',
    'port': '5432',
}

db_url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES['user'], POSTGRES['pw'], POSTGRES['host'], POSTGRES['port'], POSTGRES['db'])


SECRET_KEY = 'Secret Key'
SQLALCHEMY_DATABASE_URI = db_url