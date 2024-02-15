# TODO DocStrings

from typing import Optional
from pydantic import BaseModel, EmailStr
from decimal import Decimal

class Base(BaseModel):
    pass

class album(Base):
    '''Available Albums'''
    Id: int
    AlbumTitle: str
    ArtistId: int 

class albumCreate(Base):
    '''Available Albums'''
    AlbumTitle: str
    ArtistId: int 

class albumUpdate(Base):
    '''Available Albums'''
    AlbumTitle: Optional[str] | None = None
    ArtistId: Optional[int] | None = None

class artist(Base):
    '''Recording Artists'''
    ArtistName: str

class genre(Base):
    '''Musical Style'''
    GenreName: str

class mediatype(Base):
    '''MediaType of Track'''
    MediaTypeName: str

class customer(Base):
    '''Customers'''
    Firstname: str 
    Lastname: str 
    Company: str 
    Address: str 
    City: str 
    State: str 
    Country: str 
    Postalcode: str 
    Phone: str 
    Fax: str 
    Email: EmailStr
    SupportRepId: str # TODO Employee name

class employee(Base):
    '''Employees'''
    Lastname: str
    Firstname: str
    Title: str
    ReportsTo: int # TODO Employee name
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

class invoice(Base):
    '''Invoices'''
    CustomerId: int # TODO Customer name
    InvoiceDate: str
    BillingAddress: str
    BillingCity: str
    BillingState: str
    BillingCountry: str
    BillingPostalcode: str
    Total: Decimal

class invoiceitem(Base):
    '''Invoice Items'''
    InvoiceId: int
    TrackId: int # TODO Track name
    UnitPrice: Decimal
    Quantity: int

class track(Base):
    '''Available Tracks per Album'''
    TrackName: str
    AlbumId: int # TODO Album name
    MediaTypeId: int # TODO Mediatype name
    GenreId: int # TODO Genre name
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: Decimal

class playlist(Base):
    '''Suggested Mixes'''
    PlaylistName: str

class playlisttrack(Base):
    '''Playlist Tracks'''
    PlaylistId: int # TODO Playlist name
    TrackId: int # TODO Track name

