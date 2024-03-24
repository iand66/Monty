from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.models import track, trackCreate, trackUpdate
from src.helper import get_db, trace
from src.orm.dbfunctions import dbDelete, dbInsert, dbSelect, dbUpdate
from src.orm.schema import Track

router = APIRouter()

@router.get("/", summary='Get All Tracks', response_model=List[trackCreate], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Tracks:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No tracks found")
    else:
        return result

@router.get("/id/{id:int}", summary= 'Get Track by Track Id', response_model=List[trackCreate], status_code=status.HTTP_200_OK)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Track by Track Id:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {id} not found")
    else:
        return result

@router.get("/name/{name:str}", summary='Get Track(s) by Track Name', response_model=List[trackCreate], status_code=status.HTTP_200_OK)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Track(s) by Track Name:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"TrackName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {name} not found")
    else:
        return result

@router.post("/name/{name:str}", summary='Create New Track', response_model=trackCreate, status_code=status.HTTP_201_CREATED)
async def create_name(data: trackCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Track:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Track {data} already exists")
    else:
        new_album = Track(**data.model_dump())
        success = dbInsert(db, new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/id/{id:int}", summary='Update Track by Track Id', response_model=trackCreate, status_code=status.HTTP_201_CREATED)
async def update_id(id: int, data: trackCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Track by Track Id:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Track, result[0], new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/name/{name:str}", summary='Update Track by Track Name', response_model=trackUpdate, status_code=status.HTTP_201_CREATED)
async def update_name(name: str, data: trackUpdate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Track by Track Name:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"TrackName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Track, result[0], new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.delete("/id/{id:int}", summary='Delete Track by Track Id', response_model=List[track], status_code=status.HTTP_202_ACCEPTED)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Track by Track Id:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {id} not found")
    else:
        success = dbDelete(db, Track, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

@router.delete("/name/{name:str}", summary='Delete Track(s) by Track Name', response_model=List[track], status_code=status.HTTP_202_ACCEPTED)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Track by Track Name:**
    - **Id**: Unique Id of Track
    - **Track Name**: Name of the Track
    - **Album Id**: Unique Id of Album
    - **Mediatype Id**: Unique Id of Mediatype
    - **Genre Id**: Unique Id of Genre
    - **Composer**: Name of Composer(s)
    - **Milliseconds**: Length of Track in Milliseconds
    - **Bytes**: Size of Track in Bytes
    - **Unit Price**: Price of Track in Currency
    - **Currency**: Trading Currency
    """
    result = dbSelect(db, Track, trace, **{"TrackName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Track {name} not found")
    else:
        success = dbDelete(db, Track, trace, **{"TrackName": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result