# TODO DocStrings
from typing import List
from src.orm.schema import Album
from src.api.schema import album
from src.orm.dbfunctions import dbSelect
from src.main import app, engine, echo, trace, HTTPException

@app.get('/albums', response_model=List[album])
async def get_albums() -> album:
    result = dbSelect
    return result

@app.get('/albums/{id:int}', response_model=List[album])
async def get_albums_id(id: int) -> album:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Album id {id} not found')
    else:
        return result

@app.get('/albums/{name:str}', response_model=List[album])
async def get_albums_name(name: str) -> album:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Album {name} not found')
    else:
        return result