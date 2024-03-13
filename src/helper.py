from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.lib.apputils import config, logSetup

# Setup working environment
"""
appcfg - Application configuration file to read
mode - Running in LIVE mode?
trace - Trace database CRUD events to trace logs
secure - Trace security events to security logs
engine - SQL Alchemy database to use
session - SQL Alchemy session object
"""
appcfg = config('./ini/globals.ini')
mode = appcfg.get('MODE','live')
trace = appcfg.get('LOGCFG','trace')
secure = appcfg.get('LOGCFG','secure')
dbtype = appcfg.get('DBCFG', 'dbtype')
logcfg = appcfg.get('LOGCFG', 'logcfg')
logloc = appcfg.get('LOGCFG', 'logloc')

if mode:
  dbname = appcfg.get('DBCFG','dblive')
else:
  dbname = appcfg.get('DBCFG','dbtest')

# Setup logging environment
logger = logSetup(logcfg, logloc)

# Create database
engine = create_engine(dbtype + dbname, connect_args={'check_same_thread':False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Get current database
def get_db():
    db = session()
    if db.bind.name == 'sqlite':
      db.execute(text('pragma foreign_keys=on'))
    try:
        return db 
    finally:
        db.close()
