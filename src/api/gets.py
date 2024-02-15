from typing import List

from src.orm.schema import *
from src.api.schema import *
from src.orm.dbfunctions import dbSelect
from src.main import app, engine, echo, trace, HTTPException

@app.get('/artists', response_model=List[artist])
async def get_artists() -> artist:
    result = dbSelect()
    return result

@app.get('/artists/{id:int}', response_model=List[artist])
async def get_artists_id(id: int) -> artist:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Artist {id} not found')
    else:
        return result

@app.get('/artists/{name:str}', response_model=List[artist])
async def get_artists_name(name: str) -> artist:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Artist {name} not found')
    else:
        return result

@app.get('/customers', response_model=List[customer])
async def get_customers() -> customer:
    result = dbSelect()
    return result

@app.get('/customers/{id:int}', response_model=List[customer])
async def get_customers_id(id: int) -> customer:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Customer {id} not found')
    else:
        return result
    
@app.get('/customers/{name:str}', response_model=List[customer])
async def get_customers_name(name: str) -> customer:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Customer {name} not found')
    else:
        return result

@app.get('/customer_search', response_model=List[customer])
async def get_customers_query(
    lastname: str | None = None,
    company: str | None = None,
    city: str | None = None,
    state: str | None = None,
    email: str | None = None
    ) -> customer:
    if lastname:
        result = dbSelect()
        if result is None:
            raise HTTPException(status_code=404, detail=f'Customer {lastname} not found')
        else:
            return result
    if company:
        result = dbSelect()
        if result is None:
            raise HTTPException(status_code=404, detail=f'Company {company} not found')
        else:
            return result
    if city:
        result = dbSelect()
        if result is None:
            raise HTTPException(status_code=404, detail=f'City {city} not found')
        else:
            return result
    if state:
        result = dbSelect()
        if result is None:
            raise HTTPException(status_code=404, detail=f'State {state} not found')
        else:
            return result
    if email:
        result = dbSelect()
        if result is None:
            raise HTTPException(status_code=404, detail=f'Email {email} not found')
        else:
            return result
        
@app.get('/employees', response_model=List[employee])
async def get_employees() -> employee:
    result = dbSelect()
    return result

@app.get('/employees/{id:int}', response_model=List[employee])
async def get_employees_id(id: int) -> employee:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Employee {id} not found')
    else:
        return result

@app.get('/employees/{name:str}', response_model=List[employee])
async def get_employees_name(name: str) -> employee:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Employee {name} not found')
    else:
        return result

@app.get('/genres', response_model=List[genre])
async def get_genres() -> genre:
    result = dbSelect()
    return result

@app.get('/genres/{id:int}', response_model=List[genre])
async def get_genres_id(id: int) -> genre:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Genre {id} not found')
    else:
        return result

@app.get('/genres/{name:str}', response_model=List[genre])
async def get_genres_name(name: str) -> genre:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Genre {name} not found')
    else:
        return result

@app.get('/invoices', response_model=List[invoice])
async def get_invoices() -> invoice:
    result = dbSelect()
    return result

@app.get('/invoices/{id:int}', response_model=List[invoice])
async def get_invoices_id(id: int) -> invoice:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Invoice {id} not found')
    else:
        return result

@app.get('/invoices/{postcode:str}', response_model=List[invoice])
async def get_invoices_postcode(postcode: str) -> invoice:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Postcode {postcode} not found')
    else:
        return result

@app.get('/mediatypes', response_model=List[mediatype])
async def get_mediatypes() -> mediatype:
    result = dbSelect()
    return result

@app.get('/mediatypes/{id:int}', response_model=List[mediatype])
async def get_mediatypes_id(id: int) -> mediatype:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Mediatype {id} not found')
    else:
        return result
    
@app.get('/mediatypes/{name:str}', response_model=List[mediatype])
async def get_mediatypes_name(name: str) -> mediatype:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Mediatype {name} not found')
    else:
        return result

@app.get('/playlists', response_model=List[playlist])
async def get_playlists() -> playlist:
    result = dbSelect()
    return result

@app.get('/playlists/{id:int}', response_model=List[playlist])
async def get_playlists_id(id: int) -> playlist:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Playlist {id} not found')
    else:
        return result

@app.get('/playlists/{name:str}', response_model=List[playlist])
async def get_playlists_name(name: str) -> playlist:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Playlist {name} not found')
    else:
        return result

@app.get('/tracks', response_model=List[track])
async def get_tracks() -> track:
    result = dbSelect()
    return result

@app.get('/tracks/{id:int}', response_model=List[track])
async def get_tracks_id(id: int) -> track:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Track {id} not found')
    else:
        return result

@app.get('/tracks/{name:str}', response_model=List[track])
async def get_tracks_name(name: str) -> track:
    result = dbSelect()
    if result is None:
        raise HTTPException(status_code=404, detail=f'Track {name} not found')
    else:
        return result
