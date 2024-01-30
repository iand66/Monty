from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal

class Base(BaseModel):
    Id: int

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

class customer(Base):
    '''
    Customers
    '''
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
    SupportRepId: str # Employee Name

class employee(Base):
    '''
    Employees
    '''
    Lastname: str
    Firstname: str
    Title: str
    ReportsTo: int # Employee
    Birthdate: str 
    Hiredate: str 
    Address: str
    City: str 
    State: str
    Country: str
    Postalcode: str
    Phone: str
    Fax: str
    Email: EmailStr

class invoice(Base):
    '''
    Invoices
    '''
    CustomerId: int 
    InvoiceDate: str
    BillingAddress: str
    BillingCity: str
    BillingState: str
    BillingCountry: str
    BillingPostalcode: str
    Total: Decimal

class invoiceitem(Base):
    '''
    Invoice Items
    '''
    InvoiceId: int
    TrackId: int
    UnitPrice: Decimal
    Quantity: int

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

class playlist(Base):
    '''
    Suggested Mixes
    '''
    PlaylistName: str

class playlisttrack(Base):
    '''
    Playlist Tracks
    '''
    PlaylistId: int
    TrackId: int

