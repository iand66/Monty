import uvicorn, logging, json
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from lib.apputils import config, logSetup
from orm.dbfunctions import dbSelect, dbSelectAll
from orm.schema import Album, Customer, Employee

appcfg = config('./ini/globals.ini')
echo = eval(appcfg['LOGCFG']['logecho'])
trace = eval(appcfg['LOGCFG']['trace'])
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})

app = FastAPI()

@app.get('/')
async def index():
  return 'TESTING TESTING TESTING'

@app.get('/albums', response_model=None)
async def get_albums() -> list:
    result = dbSelectAll(engine, Album, echo, trace)
    return result

@app.get('/albums/{id:int}', response_model=None)
async def get_albums_id(id: int) -> list:
    result = dbSelect(engine, Album, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Album id {id} not found')
    else:
        return result

@app.get('/albums/{title:str}', response_model=None)
async def get_albums_title(title: str) -> list:
    result = dbSelect(engine, Album, {'AlbumTitle':title}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Album title {title} not found')
    else:
        return result

if __name__ == '__main__':
    title = 'Park'
    result = json.dumps(dbSelect(engine, Employee, {'Lastname':title}, False, False))
    print(result)
    #logger = logging.getLogger('uvicorn.error')
    #uvicorn.run("tryme:app", port=8001, log_level="debug", reload=True)
