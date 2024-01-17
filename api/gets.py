from main import engine, app
from orm.dbfunctions import dbSelectAll
from orm.schema import Album, Artist, Customer, Employee, Genre, Mediatype, Track
from api.schema import album, artist, customer, employee, genre, mediatype, track

#TODO playlists playlisttracks invoices invoiceitems
#TODO Get {id} // Gets {criteria}

@app.get('/albums', response_model=list[album])
async def get_albums():
    result = dbSelectAll(engine, Album, True)
    return result

@app.get('/artists', response_model=list[artist])
async def get_artists():
    result = dbSelectAll(engine, Artist, True)
    return result

@app.get('/customers', response_model=list[customer])
async def get_customers():
    result = dbSelectAll(engine, Customer, True)
    return result

@app.get('/employees', response_model=list[employee])
async def get_employees():
    result = dbSelectAll(engine, Employee, True)
    return result

@app.get('/genres', response_model=list[genre])
async def get_genres():
    result = dbSelectAll(engine, Genre, True)
    return result

@app.get('/mediatypes', response_model=list[mediatype])
async def get_mediatypes():
    result = dbSelectAll(engine, Mediatype, True)
    return result

@app.get('/tracks', response_model=list[track])
async def get_tracks():
    result = dbSelectAll(engine, Track, True)
    return result