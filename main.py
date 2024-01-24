import uvicorn, logging
from fastapi import FastAPI
from sqlalchemy import create_engine
from lib.apputils import config, logSetup
from api.gets import *

appcfg = config('./ini/globals.ini')
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], eval(appcfg['LOGCFG']['logecho']))
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})

app = FastAPI()

if __name__ == '__main__':
    logger = logging.getLogger('uvicorn.error')
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)