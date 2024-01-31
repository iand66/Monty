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

@app.get('/albums/{id:int}', response_model=List[album])
async def get_albums_id(id: int) -> list:
    result = dbSelect(engine, Album, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Album id {id} not found')
    else:
        return result

@app.get('/albums/{name:str}', response_model=List[album])
async def get_albums_name(name: str) -> list:
    result = dbSelect(engine, Album, {'AlbumTitle':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Album name {name} not found')
    else:
        return result

@app.get('/artists', response_model=List[artist])
async def get_artists() -> list:
    result = dbSelectAll(engine, Artist, echo, trace)
    return result

@app.get('/artists/{id:int}', response_model=List[artist])
async def get_artists_id(id: int) -> list:
    result = dbSelect(engine, Artist, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Artist id {id} not found')
    else:
        return result

@app.get('/artists/{name:str}', response_model=List[artist])
async def get_artists_name(name: str) -> list:
    result = dbSelect(engine, Artist, {'ArtistName':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Artist name {name} not found')
    else:
        return result

@app.get('/customers', response_model=List[customer])
async def get_customers() -> list:
    result = dbSelectAll(engine, Customer, echo, trace)
    return result

@app.get('/customers/{id:int}', response_model=List[customer])
async def get_customers_id(id: int) -> list:
    result = dbSelect(engine, Customer, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Customer id {id} not found')
    else:
        return result
    
@app.get('/customers/{name:str}', response_model=List[customer])
async def get_customers_name(name: str) -> list:
    result = dbSelect(engine, Customer, {'Lastname':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Customer lastname {name} not found')
    else:
        return result

@app.get('/employees', response_model=List[employee])
async def get_employees() -> list:
    result = dbSelectAll(engine, Employee, echo, trace)
    return result

@app.get('/employees/{id:int}', response_model=List[employee])
async def get_employees_id(id: int) -> list:
    result = dbSelect(engine, Employee, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Employee id {id} not found')
    else:
        return result

@app.get('/employees/{name:str}', response_model=List[employee])
async def get_employees_name(name: str) -> list:
    result = dbSelect(engine, Employee, {'Lastname': name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Employee {name} not found')
    else:
        return result

@app.get('/genres', response_model=List[genre])
async def get_genres() -> list:
    result = dbSelectAll(engine, Genre, echo, trace)
    return result

@app.get('/genres/{id:int}', response_model=List[genre])
async def get_genres_id(id: int) -> list:
    result = dbSelect(engine, Genre, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Genre id {id} not found')
    else:
        return result

@app.get('/genres/{name:str}', response_model=List[genre])
async def get_genres_name(name: str) -> list:
    result = dbSelect(engine, Genre, {'GenreName':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Genre {name} not found')
    else:
        return result

@app.get('/invoices', response_model=List[invoice])
async def get_invoices() -> list:
    result = dbSelectAll(engine, Invoice, echo, trace)
    return result

@app.get('/invoices/{id:int}', response_model=List[invoice])
async def get_invoices_id(id: int) -> list:
    result = dbSelect(engine, Invoice, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Invoice id {id} not found')
    else:
        return result

# TODO Missing values?
@app.get('/invoices/{postcode:str}', response_model=List[invoice])
async def get_invoices_postcode(postcode: str) -> list:
    result = dbSelect(engine, Invoice, {'BillingPostalcode':postcode}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Invoice {postcode} not found')
    else:
        return result

@app.get('/mediatypes', response_model=List[mediatype])
async def get_mediatypes() -> list:
    result = dbSelectAll(engine, Mediatype, echo, trace)
    return result

@app.get('/mediatypes/{id:int}', response_model=List[mediatype])
async def get_mediatypes_id(id: int) -> list:
    result = dbSelect(engine, Mediatype, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Mediatype id {id} not found')
    else:
        return result
    
@app.get('/mediatypes/{name:str}', response_model=List[mediatype])
async def get_mediatypes_name(name: str) -> list:
    result = dbSelect(engine, Mediatype, {'MediaTypeName':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Mediatype {name} not found')
    else:
        return result

@app.get('/playlists', response_model=List[playlist])
async def get_playlists() -> list:
    result = dbSelectAll(engine, Playlist, echo, trace)
    return result

@app.get('/playlists/{id:int}', response_model=List[playlist])
async def get_playlists_id(id: int) -> list:
    result = dbSelect(engine, Playlist, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Playlist id {id} not found')
    else:
        return result

@app.get('/playlists/{name:str}', response_model=List[playlist])
async def get_playlists_name(name: str) -> list:
    result = dbSelect(engine, Playlist, {'PlaylistName':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Playlist name {name} not found')
    else:
        return result

@app.get('/tracks', response_model=List[track])
async def get_tracks() -> list:
    result = dbSelectAll(engine, Track, echo, trace)
    return result

@app.get('/tracks/{id:int}', response_model=List[track])
async def get_tracks_id(id: int) -> list:
    result = dbSelect(engine, Track, {'Id':id}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Track id {id} not found')
    else:
        return result

@app.get('/tracks/{name:str}', response_model=List[track])
async def get_tracks_name(name: str) -> list:
    result = dbSelect(engine, Track, {'TrackName':name}, echo, trace)
    if result == None:
        raise HTTPException(status_code=404, detail=f'Track name {name} not found')
    else:
        return result
