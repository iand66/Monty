from main import app, engine, echo, trace, HTTPException
from typing import List
from orm.schema import *
from api.schema import *
from orm.dbfunctions import dbSelectAll, dbSelect

@app.get('/')
async def index():
  return 'Welcome to Monty'

@app.get('/albums', response_model=List[album])
async def get_albums() -> list:
    result = dbSelectAll(engine, Album, echo, trace)
    return result

@app.get('/album/{id}', response_model=List[album])
async def get_album(id: int) -> list:
    result = dbSelect(engine, Album, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Album id {id} not found')
    else:
        return result

@app.get('/artists', response_model=List[artist])
async def get_artists() -> list:
    result = dbSelectAll(engine, Artist, echo, trace)
    return result

@app.get('/customers', response_model=List[customer])
async def get_customers() -> list:
    result = dbSelectAll(engine, Customer, echo, trace)
    return result

@app.get('/employees', response_model=List[employee])
async def get_employees() -> list:
    result = dbSelectAll(engine, Employee, echo, trace)
    return result

@app.get('/genres', response_model=List[genre])
async def get_genres() -> list:
    result = dbSelectAll(engine, Genre, echo, trace)
    return result

@app.get('/invoices', response_model=List[invoice])
async def get_invoices() -> list:
    result = dbSelectAll(engine, Invoice, echo, trace)
    return result

@app.get('/mediatypes', response_model=List[mediatype])
async def get_mediatypes() -> list:
    result = dbSelectAll(engine, Mediatype, echo, trace)
    return result

@app.get('/playlists', response_model=List[playlist])
async def get_playLists() -> list:
    result = dbSelectAll(engine, Playlist, echo, trace)
    return result

@app.get('/tracks', response_model=List[track])
async def get_tracks() -> list:
    result = dbSelectAll(engine, Track, echo, trace)
    return result