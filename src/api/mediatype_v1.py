from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.models import mediatype, mediatypeCreate, mediatypeUpdate
from src.helper import get_db
from src.orm.dbfunctions import dbDelete, dbInsert, dbSelect, dbUpdate
from src.orm.schema import Mediatype

router = APIRouter()


@router.get(
    "/",
    summary="Get All Mediatypes",
    response_model=List[mediatypeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Mediatypes:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"Id": "%"})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No mediatype found"
        )
    else:
        return result


@router.get(
    "/id/{id:int}",
    summary="Get Mediatype by Id",
    response_model=List[mediatypeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Mediatype by Mediatype Id:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {id} not found"
        )
    else:
        return result


@router.get(
    "/name/{name:str}",
    summary="Get Mediatype(s) by Name",
    response_model=List[mediatypeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Mediatype by Mediatype Name:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"MediaTypeName": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {name} not found"
        )
    else:
        return result


@router.post(
    "/name/{name:str}",
    summary="Create New Mediatype",
    response_model=mediatypeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_name(data: mediatypeCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Mediatype:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **data.model_dump())
    if result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Mediatype {data} already exists",
        )
    else:
        new_album = Mediatype(**data.model_dump())
        success = dbInsert(db, new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/id/{id:int}",
    summary="Update Mediatype by Id",
    response_model=mediatypeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def update_id(
    id: int, data: mediatypeCreate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Mediatype by Mediatype Id:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {id} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Mediatype, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/name/{name:str}",
    summary="Update Mediatype by Name",
    response_model=mediatypeUpdate,
    status_code=status.HTTP_201_CREATED,
)
async def update_name(
    name: str, data: mediatypeUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Mediatype by Mediatype Name:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"MediaTypeName": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {name} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Mediatype, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.delete(
    "/id/{id:int}",
    summary="Delete Mediatype by Id",
    response_model=List[mediatype],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Mediatype by Mediatype Id:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {id} not found"
        )
    else:
        success = dbDelete(db, Mediatype, **{"Id": id})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result


@router.delete(
    "/name/{name:str}",
    summary="Mediatype(s) by Name",
    response_model=List[mediatype],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Mediatype(s) by Mediatype Name:**
    - **Id**: Unique Id of Mediatype
    - **MediaType Name**: Name of the Mediatype
    """
    result = dbSelect(db, Mediatype, **{"MediaTypeName": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Mediatype {name} not found"
        )
    else:
        success = dbDelete(db, Mediatype, **{"MediaTypeName": name})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result
