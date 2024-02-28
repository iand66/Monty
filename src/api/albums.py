from typing import List, Any

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, status

from src.helper import get_db, echo, trace
from src.orm.dbfunctions import dbSelect, dbInsert, dbDelete, dbUpdate
from src.orm.schema import Album
from src.api.schema import albumCreate, albumUpdate, albumDelete

router = APIRouter()

# GET All Album(s)
@router.get("/", status_code=status.HTTP_200_OK, tags=["Albums"], response_model=List[albumCreate])
async def get_albums(db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No albums found")
    else:
        return result

# GET Album by Id
@router.get("/id/{id:int}", status_code=status.HTTP_200_OK, tags=["Albums"], response_model=List[albumCreate])
async def get_albums_id(id: int, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        return result

# GET Album(s) by Album Name - Supports SQL % wildcard
@router.get("/name/{name:str}", status_code=status.HTTP_200_OK, tags=["Albums"], response_model=List[albumCreate])
async def get_albums_name(name: str, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        return result

# GET Album(s) by Artist Id
@router.get("/artist/{artist:int}", status_code=status.HTTP_200_OK, tags=["Albums"], response_model=List[albumCreate])
async def get_albums_artist(artist: int, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"ArtistId": artist})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist Id {artist} not found")
    else:
        return result

# POST Album by Name
@router.post("/name/{name:str}", status_code=status.HTTP_201_CREATED, tags=["Albums"], response_model=albumCreate)
async def create_albums_name(data: albumCreate, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Album {data} already exists")
    else:
        new_album = Album(**data.model_dump())
        success = dbInsert(db, new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

# PUT Album by Album Id
@router.put("/id/{id:int}", status_code=status.HTTP_201_CREATED, tags=["Albums"], response_model=albumCreate)
async def update_albums_id(id: int, data: albumCreate, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Album, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

# PUT Album by Album name
@router.put("/name/{name:str}", status_code=status.HTTP_201_CREATED, tags=["Albums"], response_model=albumUpdate)
async def update_albums_name(name: str, data: albumUpdate, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Album, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

# DELETE Album by Album Id
@router.delete("/id/{id:int}", status_code=status.HTTP_202_ACCEPTED, tags=["Albums"], response_model=List[albumDelete])
async def delete_albums_id(id: int, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        success = dbDelete(db, Album, echo, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

# DELETE Album(s) by Album name  - Supports SQL % wildcard
@router.delete("/name/{name:str}", status_code=status.HTTP_202_ACCEPTED, tags=["Albums"], response_model=List[albumDelete])
async def delete_albums_name(name: str, db: Session = Depends(get_db)) -> Any:
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        success = dbDelete(db, Album, echo, trace, **{"AlbumTitle": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result