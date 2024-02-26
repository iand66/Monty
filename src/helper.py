from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.lib.apputils import config, logSetup

# Setup working environment
appcfg = config('./ini/globals.ini')
echo = eval(appcfg['LOGCFG']['logecho'])
trace = eval(appcfg['LOGCFG']['trace'])
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
#engine = create_engine(appcfg['DBCFG']['dbType'] + appcfg['DBCFG']['dbName'], connect_args={'check_same_thread':False})
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={'check_same_thread':False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define current database
def get_db():
    db = session()
    if db.bind.name == 'sqlite':
      db.execute(text('pragma foreign_keys=on'))
    try:
        yield db 
    finally:
        db.close()