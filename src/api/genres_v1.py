from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.models import genre, genreCreate, genreUpdate
from src.helper import get_db, trace
from src.orm.dbfunctions import dbDelete, dbInsert, dbSelect, dbUpdate
from src.orm.schema import Genre

router = APIRouter()

@router.get("/", summary='Get All Genres', response_model=List[genreCreate], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Genres:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre,trace, **{"Id": "%"})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No genres found")
    else:
        return result

@router.get("/id/{id:int}", summary= 'Get Genre by Genre Id', response_model=List[genreCreate], status_code=status.HTTP_200_OK)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Genre by Genre Id:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {id} not found")
    else:
        return result

@router.get("/name/{name:str}", summary='Get Genre(s) by Genre Name', response_model=List[genreCreate], status_code=status.HTTP_200_OK)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Genre by Genre Name:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"GenreName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {name} not found")
    else:
        return result

@router.post("/name/{name:str}", summary='Create New Genre', response_model=genreCreate, status_code=status.HTTP_201_CREATED)
async def create_name(data: genreCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Genre:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **data.model_dump())
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Genre {data} already exists")
    else:
        new_album = Genre(**data.model_dump())
        success = dbInsert(db, new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/id/{id:int}", summary='Update Genre by Genre Id', response_model=genreCreate, status_code=status.HTTP_201_CREATED)
async def update_id(id: int, data: genreCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Genre by Genre Id:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {id} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Genre, result[0], new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.put("/name/{name:str}", summary='Update Genre by Genre Name', response_model=genreUpdate, status_code=status.HTTP_201_CREATED)
async def update_name(name: str, data: genreUpdate, db: Session = Depends(get_db)) -> Any:
    """
    **Update Genre by Genre Name:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"GenreName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {name} not found")
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Genre, result[0], new_album, trace)
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return data

@router.delete("/id/{id:int}", summary='Delete Genre by Genre Id', response_model=List[genre], status_code=status.HTTP_202_ACCEPTED)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Genre by Genre Id:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"Id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {id} not found")
    else:
        success = dbDelete(db, Genre, trace, **{"Id": id})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result

@router.delete("/name/{name:str}", summary='Genre(s) by Genre Name', response_model=List[genre], status_code=status.HTTP_202_ACCEPTED)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Genre(s) by Genre Name:**
    - **Id**: Unique Id of Genre
    - **Genre Name**: Name of the Genre
    """
    result = dbSelect(db, Genre, trace, **{"GenreName": name})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Genre {name} not found")
    else:
        success = dbDelete(db, Genre, trace, **{"GenreName": name})
        if not success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database Error. Please check application logs")
    return result