from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.models import employee, employeeCreate, employeeUpdate
from src.helper import get_db
from src.orm.dbfunctions import dbDelete, dbInsert, dbSelect, dbUpdate
from src.orm.schema import Employee

router = APIRouter()


@router.get(
    "/",
    summary="Get All Employees",
    response_model=List[employeeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Employees:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Id": "%"})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No employees found"
        )
    else:
        return result


@router.get(
    "/id/{id:int}",
    summary="Get Employee by Employee Id",
    response_model=List[employeeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Employee by Employee Id:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee {id} not found"
        )
    else:
        return result


@router.get(
    "/name/{name:str}",
    summary="Get Employee(s) by Employee Name",
    response_model=List[employeeCreate],
    status_code=status.HTTP_200_OK,
)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Employee by Employee Name:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {name} not found"
        )
    else:
        return result


@router.get("/search", response_model=List[employeeCreate])
async def get_query(
    lastname: str | None = None,
    firstname: str | None = None,
    title: str | None = None,
    address: str | None = None,
    city: str | None = None,
    state: str | None = None,
    country: str | None = None,
    postal: str | None = None,
    phone: str | None = None,
    email: str | None = None,
    db: Session = Depends(get_db),
) -> employeeCreate:
    """
    **Employee Search:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    if lastname:
        result = dbSelect(db, Employee, **{"Lastname": lastname})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee lastname {lastname} not found",
            )
        else:
            return result
    if firstname:
        result = dbSelect(db, Employee, **{"Firstname": firstname})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee firstname {firstname} not found",
            )
        else:
            return result
    if title:
        result = dbSelect(db, Employee, **{"Title": title})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee company {title} not found",
            )
        else:
            return result
    if address:
        result = dbSelect(db, Employee, **{"Address": address})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee address {address} not found",
            )
        else:
            return result
    if city:
        result = dbSelect(db, Employee, **{"City": city})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee city {city} not found",
            )
        else:
            return result
    if state:
        result = dbSelect(db, Employee, **{"State": state})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee state {state} not found",
            )
        else:
            return result
    if country:
        result = dbSelect(db, Employee, **{"Country": country})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee country {country} not found",
            )
        else:
            return result
    if postal:
        result = dbSelect(db, Employee, **{"Postalcode": postal})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee postcode {postal} not found",
            )
        else:
            return result
    if phone:
        result = dbSelect(db, Employee, **{"Phone": phone})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee phone {phone} not found",
            )
        else:
            return result
    if email:
        result = dbSelect(db, Employee, **{"Email": email})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee email {email} not found",
            )
        else:
            return result


@router.post(
    "/name/{name:str}",
    summary="Create New Employee",
    response_model=employeeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_name(data: employeeCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Employee:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **data.model_dump())
    if result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Employee {data} already exists",
        )
    else:
        new_album = Employee(**data.model_dump())
        success = dbInsert(db, new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/id/{id:int}",
    summary="Update Employee by Employee Id",
    response_model=employeeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def update_id(
    id: int, data: employeeCreate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Employee by Employee Id:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee {id} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Employee, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/name/{name:str}",
    summary="Update Employee by Employee Name",
    response_model=employeeUpdate,
    status_code=status.HTTP_201_CREATED,
)
async def update_name(
    name: str, data: employeeUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Employee by Employee Name:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee {name} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Employee, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.delete(
    "/id/{id:int}",
    summary="Delete Employee by Employee Id",
    response_model=List[employee],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Employee by Employee Id:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {id} not found"
        )
    else:
        success = dbDelete(db, Employee, **{"Id": id})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result


@router.delete(
    "/name/{name:str}",
    summary="Employee(s) by Employee Name",
    response_model=List[employee],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Employee(s) by Employee Name:**
    - **Id**: Unique Id of Employee
    - **Lastname**: Surname of Employee
    - **Firstname**: Firstname of Employee
    - **Title**: Employee's Title
    - **ReportsTo**: Employee's Line Manager
    - **Birthdate**: Employee's Date of Birth
    - **Hiredate**: Employee's Date of Hire
    - **Address**: Employee's Location Address
    - **City**: Employee's Location City
    - **State**: Employee's Location State
    - **Country**: Employee's Location Country
    - **Postalcode**: Employee's Location Postal Code
    - **Phone**: Employee's Phone Number
    - **Email**: Employee's Email Address
    """
    result = dbSelect(db, Employee, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee {name} not found"
        )
    else:
        success = dbDelete(db, Employee, **{"Lastname": name})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result
