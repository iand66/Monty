from typing import List, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, status
from src.helper import get_db, echo, trace
from src.orm.dbfunctions import dbSelect, dbInsert, dbDelete, dbUpdate
from src.orm.schema import Album
from src.api.models import album, albumCreate, albumUpdate, albumDelete

router = APIRouter()

@router.get("/", summary='Get All Albums', response_model=List[albumCreate], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Albums:**
    - **AlbumTitle**: Title of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No albums found")
    else:
        return result

@router.get("/id/{id:int}", summary= 'Get Album by Album Id', response_model=List[albumCreate], status_code=status.HTTP_200_OK)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Album by Album Id:**
    - **AlbumTitle**: Title of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        return result

@router.get("/name/{name:str}", summary='Get Album(s) by Album Name', response_model=List[albumCreate], status_code=status.HTTP_200_OK)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Album(s) by Album Name:**
    - **AlbumTitle**: Title of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        return result

@router.get("/artist/{artist:int}", summary='Get Album(s) by Artist Id', response_model=List[albumCreate], status_code=status.HTTP_200_OK)
async def get_artist(artist: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Album(s) by Artist Id:**
    - **AlbumTitle**: Title of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"ArtistId": artist})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist Id {artist} not found")
    else:
        return result

@router.post("/name/{name:str}", summary='Create New Album', response_model=albumCreate, status_code=status.HTTP_201_CREATED)
async def create_name(data: albumCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Album:**
    - **AlbumTitle**: Name of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Album {data} already exists")
    else:
        new_album = Album(**data.model_dump())
        success = dbInsert(db, new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/id/{id:int}", summary='Update Album by Album Id', response_model=albumCreate, status_code=status.HTTP_201_CREATED)
async def update_id(id: int, data: albumCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Album by Album Id:**
    - **AlbumTitle**: Name of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Album, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/name/{name:str}", summary='Update Album by Album Name', response_model=albumUpdate, status_code=status.HTTP_201_CREATED)
async def update_name(name: str, data: albumUpdate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Album by Album Name:**
    - **AlbumTitle**: Name of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Album, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.delete("/id/{id:int}", summary='Delete Album by Album Id', response_model=List[albumDelete], status_code=status.HTTP_202_ACCEPTED)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Album by Album Id:**
    - **Id**: Unique Id of Album
    - **AlbumTitle**: Name of the album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {id} not found")
    else:
        success = dbDelete(db, Album, echo, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

@router.delete("/name/{name:str}", summary='Delete Album(s) by Album Name', response_model=List[albumDelete], status_code=status.HTTP_202_ACCEPTED)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Album by Album Name:**
    - **Id**: Unique Id of Album
    - **AlbumTitle**: Name of the Album
    - **ArtistId**: Unique Id of Artist
    """
    result = dbSelect(db, Album, echo, trace, **{"AlbumTitle": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Album {name} not found")
    else:
        success = dbDelete(db, Album, echo, trace, **{"AlbumTitle": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result