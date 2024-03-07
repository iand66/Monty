from typing import List, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, status
from src.helper import get_db, echo, trace
from src.orm.dbfunctions import dbSelect, dbInsert, dbDelete, dbUpdate
from src.orm.schema import Artist
from src.api.models import artist, artistCreate, artistUpdate

router = APIRouter()

@router.get("/", summary='Get All Artists', response_model=List[artistCreate], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Artists:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No artists found")
    else:
        return result

@router.get("/id/{id:int}", summary= 'Get Artist by Artist Id', response_model=List[artistCreate], status_code=status.HTTP_200_OK)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Artist by Artist Id:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {id} not found")
    else:
        return result

@router.get("/name/{name:str}", summary='Get Artists(s) by Artist Name', response_model=List[artistCreate], status_code=status.HTTP_200_OK)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Artist by Artist Name:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"ArtistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {name} not found")
    else:
        return result

@router.post("/name/{name:str}", summary='Create New Artist', response_model=artistCreate, status_code=status.HTTP_201_CREATED)
async def create_name(data: artistCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Artist:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Artist {data} already exists")
    else:
        new_album = Artist(**data.model_dump())
        success = dbInsert(db, new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/id/{id:int}", summary='Update Artist by Artist Id', response_model=artistCreate, status_code=status.HTTP_201_CREATED)
async def update_id(id: int, data: artistCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Artist by Artist Id:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Artist, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/name/{name:str}", summary='Update Artist by Artist Name', response_model=artistUpdate, status_code=status.HTTP_201_CREATED)
async def update_name(name: str, data: artistUpdate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Artist by Artist Name:**
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"ArtistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Artist, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.delete("/id/{id:int}", summary='Delete Artist by Artist Id', response_model=List[artist], status_code=status.HTTP_202_ACCEPTED)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Artist by Artist Id:**
    - **Id**: Unique Id of Artist
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {id} not found")
    else:
        success = dbDelete(db, Artist, echo, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

@router.delete("/name/{name:str}", summary='Artist(s) by Artist Name', response_model=List[artist], status_code=status.HTTP_202_ACCEPTED)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Artist(s) by Artist Name:**
    - **Id**: Unique Id of Artist
    - **ArtistName**: Name of the Artist
    """
    result = dbSelect(db, Artist, echo, trace, **{"ArtistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist {name} not found")
    else:
        success = dbDelete(db, Artist, echo, trace, **{"ArtistName": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result