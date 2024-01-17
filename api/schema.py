from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal

#TODO Pydantic datatypes?

class Base(BaseModel):
    Id: Optional[int] = None

class album(Base):
    '''
    Available Albums
    '''
    AlbumTitle: str
    ArtistId: int # ArtistName

class artist(Base):
    '''
    Recording Artists
    '''
    ArtistName: str

class customer(Base):
    '''
    Customers
    '''
    Lastname: str 
    Firstname: str 
    Company: str 
    Address: str 
    City: str 
    State: str 
    Country: str 
    Postalcode: str 
    Phone: str 
    Fax: str 
    Email: EmailStr
    SupportRepId: str # Employee Name

class employee(Base):
    '''
    Employees
    '''
    Lastname: str
    Firstname: str
    Title: str
    ReportsTo: int # Employee
    Birthdate: str # TODO Date
    Hiredate: str # TODO Date
    Address: str
    City: str 
    State: str
    Country: str
    Postalcode: str
    Phone: str
    Fax: str
    Email: EmailStr

class genre(Base):
    '''
    Musical Style
    '''
    GenreName: str

class mediatype(Base):
    '''
    MediaType of Track
    '''
    MediaTypeName: str

class track(Base):
    '''
    Available Tracks per Album
    '''
    TrackName: str
    AlbumId: int # Albums
    MediaTypeId: int # Mediatypes
    GenreId: int # Genres
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: Decimal