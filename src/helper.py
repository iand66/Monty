from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.lib.apputils import config, logSetup

# Setup working environment
"""
appcfg - Application configuration file to read
mode - Running in LIVE mode?
echo - Echo application logs to application logs
trace - Trace database CRUD events to trace logs
sec - Trace security events to security logs
logger - Application & database logged events object
engine - SQL Alchemy database to use
session - SQL Alchemy session object
"""
appcfg = config('./ini/globals.ini')
mode = eval(appcfg['MODE']['live'])
echo = eval(appcfg['LOGCFG']['echo'])
trace = eval(appcfg['LOGCFG']['trace'])
sec = eval(appcfg['LOGCFG']['sec'])
logger = logSetup(appcfg['LOGCFG']['cfg'], appcfg['LOGCFG']['loc'], echo, trace, sec)

if mode:
  engine = create_engine(appcfg['DBCFG']['dbType'] + appcfg['DBCFG']['dbName'], connect_args={'check_same_thread':False})
else:
  engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={'check_same_thread':False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define current database
def get_db():
    db = session()
    if db.bind.name == 'sqlite':
      db.execute(text('pragma foreign_keys=on'))
    try:
        return db 
    finally:
        db.close()