from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.models import customer, customerCreate, customerUpdate
from src.helper import get_db
from src.orm.dbfunctions import dbDelete, dbInsert, dbSelect, dbUpdate
from src.orm.schema import Customer

router = APIRouter()


@router.get(
    "/",
    summary="Get All Customers",
    response_model=List[customerCreate],
    status_code=status.HTTP_200_OK,
)
async def get_all(db: Session = Depends(get_db)) -> Any:
    """
    **Get All Customers:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Id": "%"})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No customers found"
        )
    else:
        return result


@router.get(
    "/id/{id:int}",
    summary="Get Customer by Customer Id",
    response_model=List[customerCreate],
    status_code=status.HTTP_200_OK,
)
async def get_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Get Customer by Customer Id:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {id} not found"
        )
    else:
        return result


@router.get(
    "/name/{name:str}",
    summary="Get Customer(s) by Customer Name",
    response_model=List[customerCreate],
    status_code=status.HTTP_200_OK,
)
async def get_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Get Customer by Customer Name:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {name} not found"
        )
    else:
        return result


@router.get("/search", response_model=List[customerCreate])
async def get_query(
    lastname: str | None = None,
    firstname: str | None = None,
    company: str | None = None,
    address: str | None = None,
    city: str | None = None,
    state: str | None = None,
    country: str | None = None,
    postal: str | None = None,
    phone: str | None = None,
    email: str | None = None,
    db: Session = Depends(get_db),
) -> customerCreate:
    """
    **Customer Search:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    if lastname:
        result = dbSelect(db, Customer, **{"Lastname": lastname})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer lastname {lastname} not found",
            )
        else:
            return result
    if firstname:
        result = dbSelect(db, Customer, **{"Firstname": firstname})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer firstname {firstname} not found",
            )
        else:
            return result
    if company:
        result = dbSelect(db, Customer, **{"Company": company})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer company {company} not found",
            )
        else:
            return result
    if address:
        result = dbSelect(db, Customer, **{"Address": address})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer address {address} not found",
            )
        else:
            return result
    if city:
        result = dbSelect(db, Customer, **{"City": city})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer city {city} not found",
            )
        else:
            return result
    if state:
        result = dbSelect(db, Customer, **{"State": state})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer state {state} not found",
            )
        else:
            return result
    if country:
        result = dbSelect(db, Customer, **{"Country": country})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer country {country} not found",
            )
        else:
            return result
    if postal:
        result = dbSelect(db, Customer, **{"Postalcode": postal})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer postcode {postal} not found",
            )
        else:
            return result
    if phone:
        result = dbSelect(db, Customer, **{"Phone": phone})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer phone {phone} not found",
            )
        else:
            return result
    if email:
        result = dbSelect(db, Customer, **{"Email": email})
        if len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer email {email} not found",
            )
        else:
            return result


@router.post(
    "/name/{name:str}",
    summary="Create New Customer",
    response_model=customerCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_name(data: customerCreate, db: Session = Depends(get_db)) -> Any:
    """
    **Create New Customer:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **data.model_dump())
    if result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Customer {data} already exists",
        )
    else:
        new_album = Customer(**data.model_dump())
        success = dbInsert(db, new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/id/{id:int}",
    summary="Update Customer by Customer Id",
    response_model=customerCreate,
    status_code=status.HTTP_201_CREATED,
)
async def update_id(
    id: int, data: customerCreate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Customer by Customer Id:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {id} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Customer, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.put(
    "/name/{name:str}",
    summary="Update Customer by Customer Name",
    response_model=customerUpdate,
    status_code=status.HTTP_201_CREATED,
)
async def update_name(
    name: str, data: customerUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    **Update Customer by Customer Name:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {name} not found"
        )
    else:
        new_album = data.model_dump()
        success = dbUpdate(db, Customer, result[0], new_album)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return data


@router.delete(
    "/id/{id:int}",
    summary="Delete Customer by Customer Id",
    response_model=List[customer],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_id(id: int, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Customer by Customer Id:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Id": id})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {id} not found"
        )
    else:
        success = dbDelete(db, Customer, **{"Id": id})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result


@router.delete(
    "/name/{name:str}",
    summary="Customer(s) by Customer Name",
    response_model=List[customer],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_name(name: str, db: Session = Depends(get_db)) -> Any:
    """
    **Delete Customer(s) by Customer Name:**
    - **Id**: Unique Id of Customer
    - **Lastname**: Customer Surname
    - **Firstname**: Customer Firstname
    - **Company**: Company Name (Where Applicable)
    - **Address**: Customer Postal Address
    - **City**: Customer Postal City
    - **State**: Customer Postal State
    - **Country**: Customer Postal Country
    - **Postalcode**: Customer Postal Code
    - **BillingAddress**: Customer Billing Address
    - **BillingCity**: Customer Billing City
    - **BillingState**: Customer Billing State
    - **BillingCountry**: Customer Billing Country
    - **BillingPostalcode**: Customer Billing Code
    - **Phone**: Customer Phone Number
    - **Email**: Customer Email Address
    - **SupportRepId**: Customer Support Representative Id
    """
    result = dbSelect(db, Customer, **{"Lastname": name})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer {name} not found"
        )
    else:
        success = dbDelete(db, Customer, **{"Lastname": name})
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database Error. Please check application logs",
            )
    return result
