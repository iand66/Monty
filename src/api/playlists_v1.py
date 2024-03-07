from typing import List, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, status
from src.helper import get_db, echo, trace
from src.orm.dbfunctions import dbSelect, dbInsert, dbDelete, dbUpdate
from src.orm.schema import Playlist
from src.api.models import playlist, playlistCreate, playlistUpdate, playlistDelete

router = APIRouter()

@router.get("/", summary='Get All Playlists', response_model=List[playlistCreate], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Playlists:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No artists found")
    else:
        return result

@router.get("/id/{id:int}", summary= 'Get Playlist by Playlist Id', response_model=List[playlistCreate], status_code=status.HTTP_200_OK)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Playlist by Playlist Id:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {id} not found")
    else:
        return result

@router.get("/name/{name:str}", summary='Get Playlist(s) by Playlist Name', response_model=List[playlistCreate], status_code=status.HTTP_200_OK)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Playlist by Playlist Name:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"PlaylistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {name} not found")
    else:
        return result

@router.post("/name/{name:str}", summary='Create New Playlist', response_model=playlistCreate, status_code=status.HTTP_201_CREATED)
async def create_name(data: playlistCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Playlist:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Playlist {data} already exists")
    else:
        new_album = Playlist(**data.model_dump())
        success = dbInsert(db, new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/id/{id:int}", summary='Update Playlist by Playlist Id', response_model=playlistCreate, status_code=status.HTTP_201_CREATED)
async def update_id(id: int, data: playlistCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Playlist by Playlist Id:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Playlist, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/name/{name:str}", summary='Update Playlist by Playlist Name', response_model=playlistUpdate, status_code=status.HTTP_201_CREATED)
async def update_name(name: str, data: playlistUpdate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Playlist by Playlist Name:**
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"PlaylistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Playlist, result[0], new_album, echo, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.delete("/id/{id:int}", summary='Delete Playlist by Playlist Id', response_model=List[playlist], status_code=status.HTTP_202_ACCEPTED)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Playlist by Playlist Id:**
    - **Id**: Unique Id of Playlist
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {id} not found")
    else:
        success = dbDelete(db, Playlist, echo, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

@router.delete("/name/{name:str}", summary='Playlist(s) by Playlist Name', response_model=List[playlist], status_code=status.HTTP_202_ACCEPTED)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Playlist(s) by Playlist Name:**
    - **Id**: Unique Id of Playlist
    - **PlaylistName**: Name of the Playlist
    """
    result = dbSelect(db, Playlist, echo, trace, **{"PlaylistName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist {name} not found")
    else:
        success = dbDelete(db, Playlist, echo, trace, **{"PlaylistName": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result