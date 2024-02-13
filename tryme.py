import logging, uvicorn, warnings
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.lib.apputils import config, logSetup
from src.orm.dbfunctions import dbSelect, dbInsert, dbDelete, dbUpdate
from src.orm.schema import Album
from src.api.schema import album, albumCreate, albumUpdate

warnings.filterwarnings("ignore", category=DeprecationWarning)

appcfg = config('./ini/globals.ini')
echo = eval(appcfg['LOGCFG']['logecho'])
trace = eval(appcfg['LOGCFG']['trace'])
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(debug=True)

def get_db():
    db = session()
    try:
        yield db 
    finally:
        db.close()

@app.get('/')
async def index():
  return 'TEST App'

@app.get('/albums', response_model=List[album])
async def get_albums(db: Session = Depends(get_db)) -> album:
    result = dbSelect()
    return result

@app.get('/albums/{id: int}', response_model=List[album])
async def get_albums_id(id: int, db: Session = Depends(get_db)) -> album:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Album {id} not found')
    else:
        return result

@app.post('/albums', status_code=201)
async def create_album(data: albumCreate, db: Session = Depends(get_db)):
  new = Album(**data.model_dump())
  result = dbSelect()
  if result is not None:
    raise HTTPException(status_code=409, detail='Duplicate Record')
  else:
    dbInsert()
    return album(**new.__dict__)
  
@app.put('/albums/{id: int}', status_code=201)
async def update_album(id: int, data: albumUpdate, db: Session = Depends(get_db)):
  result = dbSelect()
  if result is None:
    raise HTTPException(status_code=404, detail=f"Album {id} not found")
  else:
    dbUpdate()
    return result.__dict__
  
@app.delete('/albums/{id: int}')
async def delete_album(id: int, db: Session = Depends(get_db)):
  result = dbSelect()
  if result is None:
    raise HTTPException(status_code=404, detail=f"Album {id} not found")
  else:
    dbDelete()
    return result
      
if __name__ == '__main__':
    logger = logging.getLogger('uvicorn.access')
    uvicorn.run("tryme:app", port=8001, log_level="debug", reload=True)
   
 
