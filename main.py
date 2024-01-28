import uvicorn, logging
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from lib.apputils import config, logSetup

appcfg = config('./ini/globals.ini')
echo = eval(appcfg['LOGCFG']['logecho'])
trace = eval(appcfg['LOGCFG']['trace'])
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})

app = FastAPI()

from api.gets import *

if __name__ == '__main__':
    logger = logging.getLogger('uvicorn.error')
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)